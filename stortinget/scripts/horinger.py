#!/usr/bin/env python3
"""
Komitéhøringer fra data.stortinget.no: hvilke saker som har høring, dato, sted, frister,
om høringen er skriftlig, og høringsprogrammet (hvem som fikk ordet, og når).
Skriftlige innspill tas ikke med; de ligger på sakssiden på stortinget.no.

Hvilke komiteer som hentes, styres av STORTINGET_KOMITEER (kommaseparert komité-id,
standard ARBSOS), og hvor dataene skrives av STORTINGET_ROT (mappen stortinget/).

Bruk:
  python3 horinger.py                      # inneværende sesjon
  python3 horinger.py --sesjon forrige
  python3 horinger.py --fra 2011-2012      # alle sesjoner fra og med 2011-2012 (engangsjobb)
  python3 horinger.py --dry-run

Programmet hentes for hver høring som er ny eller endret, og for høringer som ikke er avholdt.
Output: ett JSON-objekt på stdout som oppsummerer endringene.
"""
import argparse
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from felles import NS, t, hent_xml, resolve_sesjon, sesjon_for_dato, last_json, skriv_json  # noqa: E402

# Mappen stortinget/. STORTINGET_ROT lar en annen base bruke skriptene mot sin egen mappe.
BASE = os.environ.get('STORTINGET_ROT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data', 'horinger')
KOMITEER = {k.strip() for k in os.environ.get('STORTINGET_KOMITEER', 'ARBSOS').split(',') if k.strip()}
SAK_URL = "https://www.stortinget.no/no/Saker-og-publikasjoner/Saker/Sak/?p={}"


def liste(el, liste_tag, element_tag):
    l = el.find(f"{NS}{liste_tag}")
    return [] if l is None else l.findall(f"{NS}{element_tag}")


def horing_record(h, sesjon):
    komite = h.find(f"{NS}komite")
    saker = [{
        'sak_id': t(s, 'sak_id'),
        'tittel': t(s, 'sak_tittel'),
        'korttittel': t(s, 'sak_korttittel'),
        'henvisning': t(s, 'sak_henvisning'),
        'sak_url': SAK_URL.format(t(s, 'sak_id')) if t(s, 'sak_id') else None,
    } for s in liste(h, 'horing_sak_info_liste', 'horing_sak_info')]
    tidspunkt = [{'tidspunkt': t(x, 'tidspunkt'), 'sted': t(x, 'sted')}
                 for x in liste(h, 'horingstidspunkt_liste', 'horingstidspunkt')]
    return {
        'id': t(h, 'id'),
        'sesjon': sesjon,
        'komite_id': t(komite, 'id') if komite is not None else None,
        'komite': t(komite, 'navn') if komite is not None else None,
        'type': t(h, 'type'),
        'skriftlig': (t(h, 'skriftlig') or '').lower() == 'true',
        'horing_status': t(h, 'horing_status'),
        'start_dato': t(h, 'start_dato'),
        'tidspunkt': tidspunkt,
        'anmodningsfrist': t(h, 'anmodningsfrist_dato_tid'),
        'innspillsfrist': t(h, 'innspillsfrist'),
        'saker': saker,
        # Høringen har ingen egen fast adresse i dataene; programmet og innspillene står på sakssiden.
        'lenke': saker[0]['sak_url'] if saker else None,
    }


def hent_program(horing_id):
    """Høringsprogrammet som en liste av innslag, ett per linje i programmet. None ved feil.
    Innslag med deltakere har tekst som «ORGANISASJON;Navn, tittel;Navn, tittel». Organisasjonen
    legges i feltet aktor, personene i personer."""
    try:
        root = hent_xml(f"https://data.stortinget.no/eksport/horingsprogram?horingid={horing_id}")
    except RuntimeError:
        return None
    ut = []
    for dag in root.iter(f"{NS}horingsprogram"):
        dato = (t(dag, 'dato') or '')[:10]
        for el in liste(dag, 'horingsprogram_element_liste', 'horingsprogram_element'):
            deler = [' '.join(d.split()) for d in (t(el, 'tekst') or '').split(';')]
            innslag = {'dato': dato, 'tid': t(el, 'tidsangivelse') or None, 'tekst': deler[0]}
            if len(deler) > 1:
                innslag['aktor'] = deler[0]
                innslag['personer'] = [d for d in deler[1:] if d]
            ut.append(innslag)
    return ut


def oppdater(sesjoner, dry_run=False):
    gamle = {x['id']: x for x in last_json(DATA)}
    nye = endret = 0
    for sesjon in sesjoner:
        root = hent_xml(f"https://data.stortinget.no/eksport/horinger?sesjonid={sesjon}")
        for h in root.iter(f"{NS}horing"):
            rec = horing_record(h, sesjon)
            if rec['komite_id'] not in KOMITEER or not rec['id']:
                continue
            gammel = gamle.get(rec['id'])
            ferdig = (rec['horing_status'] or '').lower() == 'avholdt'
            if gammel and gammel.get('program') is not None and ferdig \
                    and {k: v for k, v in gammel.items() if k != 'program'} == rec:
                continue
            rec['program'] = hent_program(rec['id'])
            if rec['program'] is None and gammel:
                rec['program'] = gammel.get('program')
            if gammel is None:
                nye += 1
            elif gammel != rec:
                endret += 1
            else:
                continue
            gamle[rec['id']] = rec
    if not dry_run and (nye or endret):
        skriv_json(DATA, list(gamle.values()))
    return {'horinger': {'nye': nye, 'endret': endret, 'total': len(gamle)}}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--sesjon', default='inneværende')
    p.add_argument('--fra', help='Første sesjon i en engangsjobb, f.eks. 2011-2012. Kjører til og med inneværende.')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()
    if args.fra:
        start, slutt = int(args.fra[:4]), int(sesjon_for_dato(date.today())[:4])
        sesjoner = [f'{a}-{a + 1}' for a in range(start, slutt + 1)]
    else:
        sesjoner = [resolve_sesjon(args.sesjon)]
    print(f"Høringer for {', '.join(sesjoner)} ({', '.join(sorted(KOMITEER))}){' (dry-run)' if args.dry_run else ''}...",
          file=sys.stderr)
    print(json.dumps(oppdater(sesjoner, args.dry_run), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
