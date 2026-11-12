#!/usr/bin/env python3
"""
Legger budsjettdokumenter fra budsjett/innboks/ inn i basen.

Filnavn bestemmer hva dokumentet er (ÅR er budsjettåret, f.eks. 2027 for Prop. 1 S 2026–2027):

    prop-1-s-ÅR-aid.docx                 Prop. 1 S for AID     -> budsjett/ÅR/prop-1-s-aid/
    gul-bok-ÅR.docx                      Prop. 1 S Gul bok      -> budsjett/ÅR/gul-bok/
    nasjonalbudsjettet-ÅR.docx           Meld. St. 1            -> budsjett/ÅR/nasjonalbudsjettet/
    prop-1-s-ÅR-tillegg-N.docx           Prop. 1 S Tillegg N    -> budsjett/ÅR/prop-1-s-tillegg-N/
    samledokument….docx                  stoppes og slettes: kan ha svar som ikke er publisert
                                         (svarene legges inn med verktoy/budsjett_sporsmal_json.py)
    gul-bok-bevilgninger-ÅR.xlsx|csv|tsv Datagrunnlag til Gul bok -> budsjett/ÅR/gul-bok-bevilgninger.tsv
    prp….rtf, …rtfz.zip, …epub           eldre utgaver fra regjeringen.no; gjøres om til Word med
                                         verktoy/budsjett_konverter.py og kjennes igjen på forsiden
    statsregnskapet….zip|csv             DFØs rådatauttrekk av statsregnskapet -> budsjett/ÅR/statsregnskap/
                                         for hvert år i filen (verktoy/statsregnskap.py)

Originalnavnet fra regjeringen.no for proposisjonen, prp[SESJON][NR][DEP]ddddocx.docx
(f.eks. prp202120220001asdddddocx.docx eller prp202620270001_kdddddocx.docx), godtas også.
Budsjettåret er siste år i sesjonen.

Word-filer kjennes også igjen på forsiden (stilene i-dep, i-hode, i-sesjon og i-termin i malen fra
regjeringen.no), så filnavnet spiller ingen rolle når forsiden er lesbar. Sier filnavnet og forsiden
noe ulikt, stoppes filen.

Basen kan være et annet repo: miljøvariabelen REGELVERK_ROT (se verktoy/basekonfig.py) sier hvor
innboksen og budsjett/ ligger. Hvilke departementers Prop. 1 S basen tar imot, og hvor
innboksen ligger, står i budsjett.json i basen. Uten den fila gjelder standardoppsettet under (AID).

Word-filene deles opp av verktoy/budsjett.py. Går oppdelingen bra, slettes filen fra
innboksen. Ellers blir den liggende, og en fil med samme navn og .FEIL.txt forklarer hvorfor.
Veiviseren budsjett/VEIVISER.md får en automatisk oversikt over hvilke år som ligger i basen.
"""

import csv
import re
import shutil
import sys
import tempfile
from pathlib import Path

import json

sys.path.insert(0, str(Path(__file__).resolve().parent))
from basekonfig import ROT  # noqa: E402

BUDSJETT = ROT / "budsjett"
RAPPORT = ROT / "budsjett-rapport.txt"
START = "<!-- AUTO-START budsjettår: genereres av verktoy/budsjett_innboks.py, ikke rediger for hånd -->"
SLUTT = "<!-- AUTO-SLUTT budsjettår -->"

MONSTRE = [
    ("prop", re.compile(r"^prop-1-s-(\d{4})-([a-zæøå]+)\.docx$", re.I)),
    ("gul", re.compile(r"^gul-bok-(\d{4})\.docx$", re.I)),
    # Tilleggsproposisjon, f.eks. Støre-regjeringens endring av Solberg-regjeringens forslag for 2022.
    # Gul bok-navnet godtas også, fordi tillegget ofte lastes ned sammen med Gul bok.
    ("tillegg", re.compile(r"^(?:prop-1-s|gul-bok)-(\d{4})-tillegg[- _]?(\d{1,2})\.docx$", re.I)),
    ("nb", re.compile(r"^nasjonalbudsjettet-(\d{4})\.docx$", re.I)),
    ("data", re.compile(r"^gul-bok-bevilgninger-(\d{4})\.(xlsx|csv|tsv)$", re.I)),
]
# Samledokument med svar på budsjettspørsmål fra Finansdepartementets system. År og runde står i dokumentet.
SAMLEDOKUMENT = re.compile(r"^samledokument.*\.docx$", re.I)
# DFØs nedlasting fra statsregnskapet.dfo.no/last-ned. Årene står i filen.
STATSREGNSKAP = re.compile(r"^statsregnskapet.*\.(zip|csv)$", re.I)
FORVENTET_KOLONNER = {"kap_nr", "post_nr", "beløp"}
# Originalnavn fra regjeringen.no: prp + sesjon (åtte sifre) + nummer (fire sifre) + departement + ddddocx
# (nyere filer har understrek foran departementskoden: prp202620270001_kdddddocx.docx)
ORIGINAL = re.compile(r"^prp(\d{4})(\d{4})(\d{4})_?([a-zæøå]+?)ddddocx\.docx$", re.I)

# Hvilke departementers Prop. 1 S basen tar imot. Overstyres av budsjett.json i basen, som enten har
# ett oppsett (som STANDARD_OPPSETT) eller {"innboks": ..., "proposisjoner": [oppsett, oppsett, ...]}.
STANDARD_OPPSETT = {
    "mappe": "prop-1-s-aid",            # budsjett/ÅR/<mappe>/
    "navn": "Prop. 1 S for AID",        # i oversikten i budsjett/VEIVISER.md
    "kode": "aid",                       # i filnavnet prop-1-s-ÅR-<kode>.docx
    "koder": ["aid", "asd"],             # departementskoder i originalnavnet, asd fram til 2022
    # Deler av departementsnavnet på forsiden (små bokstaver)
    "departement": ["arbeids- og inkluderingsdepartement", "arbeids- og sosialdepartement"],
    "innboks": "budsjett/innboks",       # mappen filene lastes opp i, relativt til basen
}


def les_oppsett():
    """Gir (innboks, liste med oppsett per proposisjon)."""
    fil = ROT / "budsjett.json"
    if not fil.exists():
        return STANDARD_OPPSETT["innboks"], [dict(STANDARD_OPPSETT)]
    data = json.loads(fil.read_text(encoding="utf-8"))
    if "proposisjoner" in data:
        return data.get("innboks", STANDARD_OPPSETT["innboks"]), [dict(STANDARD_OPPSETT, **o) for o in data["proposisjoner"]]
    oppsett = dict(STANDARD_OPPSETT, **data)
    return oppsett["innboks"], [oppsett]


INNBOKS_NAVN, PROPOSISJONER = les_oppsett()
INNBOKS = ROT / INNBOKS_NAVN
KJENTE_NAVN = " eller ".join(o["navn"] for o in PROPOSISJONER)
KJENTE_FILNAVN = ", ".join(f"prop-1-s-ÅR-{o['kode']}.docx" for o in PROPOSISJONER)


def prop_fra_kode(kode):
    """Oppsettet for departementskoden i filnavnet, eller None."""
    kode = kode.lower()
    return next((o for o in PROPOSISJONER if kode in o["koder"] + [o["kode"]]), None)


def sjekk_aar(aar):
    if not 1990 <= aar <= 2100:
        raise ValueError(f"budsjettåret {aar} ser feil ut")
    return aar


def klassifiser(navn):
    """Gir (type, budsjettår, tilleggsnummer eller None). For samledokumenter er budsjettåret None."""
    if SAMLEDOKUMENT.match(navn):
        return "sporsmal", None, None
    if STATSREGNSKAP.match(navn):
        return "regnskap", None, None
    for type_, m in MONSTRE:
        r = m.match(navn)
        if r:
            if type_ == "prop":
                o = prop_fra_kode(r.group(2))
                if o is None:
                    raise ValueError(f"filnavnet sier departementskoden «{r.group(2)}». Denne basen tar bare imot "
                                     f"{KJENTE_NAVN} ({KJENTE_FILNAVN})")
                return type_, sjekk_aar(int(r.group(1))), o["mappe"]
            return type_, sjekk_aar(int(r.group(1))), (int(r.group(2)) if type_ == "tillegg" else None)
    r = ORIGINAL.match(navn)
    if r:
        fra, til, nr, dep = int(r.group(1)), int(r.group(2)), int(r.group(3)), r.group(4).lower()
        if til != fra + 1:
            raise ValueError(f"sesjonen {fra}–{til} i filnavnet ser feil ut")
        o = prop_fra_kode(dep)
        if nr != 1 or o is None or dep not in o["koder"]:
            raise ValueError(
                f"filnavnet ser ut som Prop. {nr} S fra departementskoden «{dep}». Bare {KJENTE_NAVN} kjennes igjen på "
                "originalnavnet. Døp om filen etter mønsteret i README.md"
            )
        return "prop", sjekk_aar(til), o["mappe"]
    raise ValueError(
        f"filnavnet passer ikke, og forsiden ble ikke kjent igjen. Bruk {KJENTE_FILNAVN}, prop-1-s-ÅR-tillegg-N.docx, gul-bok-ÅR.docx, "
        "nasjonalbudsjettet-ÅR.docx, gul-bok-bevilgninger-ÅR.xlsx (ÅR er budsjettåret, f.eks. 2027) eller "
        "statsregnskapet….zip fra DFØ. "
        f"Originalnavnet fra regjeringen.no for {KJENTE_NAVN} (prp…ddddocx.docx) virker også"
    )


FORSIDESTILER = ("i-dep", "is-dep", "i-hode", "i-sesjon", "i-termin", "i-tit")


def les_forside(sti: Path):
    """Teksten i forsidestilene fra malen på regjeringen.no, f.eks. {"i-hode": "Prop. 1 S", "i-termin": "FOR BUDSJETTÅRET 2027"}.

    Gir None når filen ikke kan leses som Word eller ikke har forsiden fra malen.
    """
    try:
        import docx

        dok = docx.Document(str(sti))
    except Exception:  # noqa: BLE001
        return None
    forside = {}
    for i, avsnitt in enumerate(dok.paragraphs):
        if i > 80:
            break
        stil = avsnitt.style.name if avsnitt.style is not None else ""
        tekst = re.sub(r"\s+", " ", avsnitt.text.replace("\xa0", " ")).strip()
        if stil in FORSIDESTILER and tekst and stil not in forside:
            forside["i-dep" if stil == "is-dep" else stil] = tekst
    return forside if "i-hode" in forside else None


def klassifiser_forside(forside):
    """Gir (type, budsjettår, tilleggsnummer) fra forsiden, eller None når dokumentet ikke kjennes igjen."""
    hode = forside.get("i-hode", "")
    termin = re.search(r"budsjett\S*\s+(\d{4})", forside.get("i-termin", ""), re.I)
    sesjon = re.search(r"(\d{4})\s*[–-]\s*(\d{4})", forside.get("i-sesjon", ""))
    aar = int(termin.group(1)) if termin else int(sesjon.group(2)) if sesjon else None
    if aar is None:
        return None
    sjekk_aar(aar)
    dep = forside.get("i-dep", "").lower()
    if re.match(r"Meld\. St\. 1\b", hode) and "nasjonalbudsjett" in forside.get("i-tit", "").lower():
        return "nb", aar, None
    r = re.match(r"Prop\. 1 S Tillegg (\d{1,2})\b", hode)
    if r:
        return "tillegg", aar, int(r.group(1))
    if re.fullmatch(r"Prop\. 1 S", hode):
        if "finansdepartement" in dep and forside.get("i-tit", "").lower().startswith("statsbudsjettet"):
            return "gul", aar, None
        for o in PROPOSISJONER:
            if any(d in dep for d in o["departement"]):
                return "prop", aar, o["mappe"]
        raise ValueError(f"forsiden viser Prop. 1 S fra «{forside.get('i-dep', 'ukjent departement')}». "
                         f"Denne basen tar bare imot {KJENTE_NAVN}")
    return None


def bestem(sti: Path):
    """Gir (type, budsjettår, tilleggsnummer) fra forsiden når den kjennes igjen, ellers fra filnavnet."""
    try:
        fra_navn = klassifiser(sti.name)
    except ValueError as e:
        fra_navn, navnefeil = None, e
    if sti.suffix.lower() != ".docx" or (fra_navn and fra_navn[0] == "sporsmal"):
        if fra_navn is None:
            raise navnefeil
        return fra_navn
    forside = les_forside(sti)
    fra_forside = klassifiser_forside(forside) if forside else None
    if fra_forside is None:
        if fra_navn is None:
            raise navnefeil
        return fra_navn
    if fra_navn and fra_navn != fra_forside:
        raise ValueError(f"filnavnet og forsiden sier ulike ting: filnavnet {fra_navn[:2]}, forsiden {fra_forside[:2]} "
                         "(type, budsjettår). Sjekk at det er riktig fil")
    return fra_forside


def erstatt_mappe(ny: Path, mal: Path):
    if mal.exists():
        shutil.rmtree(mal)
    mal.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(ny), str(mal))


def del_opp_word(sti: Path, type_, aar, tillegg=None):
    import budsjett

    ut = Path(tempfile.mkdtemp()) / "ut"
    if type_ == "prop":
        filer, poster = budsjett.del_opp(str(sti), ut, sti.name)
        if len(filer) < 5 or not poster:
            raise ValueError(
                f"fant bare {len(filer)} filer og {len(poster)} poster. Stilnavnene i Word-filen svarer ikke til "
                "dem verktoy/budsjett.py forventer, så dokumentet er trolig fra en annen utgave"
            )
        erstatt_mappe(ut, BUDSJETT / str(aar) / tillegg)  # for prop er tillegg mappen til proposisjonen
        return f"{len(filer)} filer, {len(poster)} poster"
    filer, _ = budsjett.del_opp_generell(str(sti), ut, sti.name)
    if len(filer) < 3:
        raise ValueError(f"fant bare {len(filer)} deler. Stilnavnene i Word-filen svarer ikke til dem verktoy/budsjett.py forventer")
    mappe = {"gul": "gul-bok", "nb": "nasjonalbudsjettet", "tillegg": f"prop-1-s-tillegg-{tillegg}"}[type_]
    erstatt_mappe(ut, BUDSJETT / str(aar) / mappe)
    return f"{len(filer)} filer"


def les_rader(sti: Path):
    if sti.suffix.lower() == ".xlsx":
        import openpyxl

        wb = openpyxl.load_workbook(sti, read_only=True, data_only=True)
        # Gul bok-filene har først et ark «Forklaring», så «Data»: ta arket med de forventede kolonnene
        ark = next((a for a in wb.worksheets
                    if FORVENTET_KOLONNER <= {str(c).strip() for c in next(a.iter_rows(max_row=1, values_only=True), ())}),
                   wb.worksheets[0])
        return [["" if c is None else c for c in rad] for rad in ark.iter_rows(values_only=True)]
    tekst = sti.read_text(encoding="utf-8-sig")
    skille = max([";", "\t", ","], key=lambda s: tekst.split("\n", 1)[0].count(s))
    return [rad for rad in csv.reader(tekst.splitlines(), delimiter=skille)]


def lag_tsv(sti: Path, aar):
    rader = [r for r in les_rader(sti) if any(str(c).strip() for c in r)]
    if not rader:
        raise ValueError("filen er tom")
    overskrift = [str(c).strip() for c in rader[0]]
    mangler = FORVENTET_KOLONNER - set(overskrift)
    if mangler:
        raise ValueError(f"første rad mangler kolonnene {', '.join(sorted(mangler))}. Fant: {', '.join(overskrift[:12])}")
    mal = BUDSJETT / str(aar) / "gul-bok-bevilgninger.tsv"
    mal.parent.mkdir(parents=True, exist_ok=True)

    def celle(c):
        if isinstance(c, float) and c.is_integer():
            c = int(c)
        return str(c).replace("\t", " ").replace("\n", " ").strip()

    with open(mal, "w", encoding="utf-8", newline="") as f:
        for r in rader:
            f.write("\t".join(celle(c) for c in r) + "\n")
    return f"{len(rader) - 1} rader"


def oppdater_veiviser():
    deler = []
    for mappe in sorted((p for p in BUDSJETT.iterdir() if p.is_dir() and p.name.isdigit()), reverse=True):
        funn = []
        kjente = [(o["mappe"], o["navn"]) for o in PROPOSISJONER]
        kjente += [(p.name, f"Prop. 1 S Tillegg {p.name.rsplit('-', 1)[1]} (alle departementer)")
                   for p in sorted(mappe.glob("prop-1-s-tillegg-*")) if p.is_dir()]
        kjente += [("gul-bok", "Gul bok"), ("nasjonalbudsjettet", "Nasjonalbudsjettet"), ("stortinget", "Stortingets vedtak"),
                   ("alternative-budsjett", "partienes alternative budsjetter")]
        for navn, tekst in kjente:
            if (mappe / navn).is_dir():
                funn.append(f"{tekst} (`budsjett/{mappe.name}/{navn}/`)")
        for runde in sorted((mappe / "sporsmal").glob("*/sporsmal.tsv")):
            antall = sum(1 for _ in runde.open(encoding="utf-8")) - 1
            navn = {"stb": "statsbudsjettet", "rnb": "revidert nasjonalbudsjett"}.get(runde.parent.name, runde.parent.name)
            funn.append(f"svar på budsjettspørsmål, {navn} ({antall} svar, `budsjett/{mappe.name}/sporsmal/{runde.parent.name}/`)")
        if (mappe / "statsregnskap").is_dir():
            funn.append(f"statsregnskapet (`budsjett/{mappe.name}/statsregnskap/`)")
        if (mappe / "gul-bok-bevilgninger.tsv").exists():
            funn.append(f"datagrunnlag (`budsjett/{mappe.name}/gul-bok-bevilgninger.tsv`)")
        deler.append(f"- **{mappe.name}:** " + (", ".join(funn) if funn else "ingen dokumenter"))
    blokk = (
        f"{START}\n## Budsjettår i basen\n\n"
        "Hvert budsjettår har sin egen mappe. Tall (datagrunnlaget) kan gå lenger tilbake enn tekst (proposisjonene). "
        "Oppgi alltid budsjettår og dokument i svaret, og husk at Prop. 1 S er forslag, ikke vedtatt budsjett.\n\n"
        + "\n".join(deler)
        + f"\n{SLUTT}\n"
    )
    veiviser = BUDSJETT / "VEIVISER.md"
    s = veiviser.read_text(encoding="utf-8")
    if START in s and SLUTT in s:
        a, b = s.index(START), s.index(SLUTT) + len(SLUTT)
        s = s[:a] + blokk.rstrip("\n") + s[b:]
    else:
        m = re.search(r"^## Budsjettår \d{4}", s, re.M)
        if not m:
            raise ValueError("fant ikke stedet i budsjett/VEIVISER.md der oversikten skal stå")
        s = s[: m.start()] + blokk + "\n" + s[m.start():]
    veiviser.write_text(s, encoding="utf-8")


def main():
    if not INNBOKS.is_dir():
        print("Ingen innboks.")
        return 0
    filer = sorted(p for p in INNBOKS.iterdir() if p.is_file() and p.name != "README.md" and not p.name.endswith(".FEIL.txt"))
    if not filer:
        print("Innboksen er tom.")
        return 0
    ok, feil = [], []
    for sti in filer:
        feilfil = sti.with_name(sti.name + ".FEIL.txt")
        try:
            word = sti
            if sti.suffix.lower() in (".rtf", ".zip", ".epub") and not STATSREGNSKAP.match(sti.name):
                # Eldre utgaver fra regjeringen.no (RTF i zip, EPUB) gjøres om til Word først
                from budsjett_konverter import til_docx
                word = til_docx(sti, Path(tempfile.mkdtemp()))
            type_, aar, tillegg = bestem(word)
            if type_ == "sporsmal":
                sti.unlink()
                raise ValueError(
                    "samledokumenter skal ikke lastes opp her. De kan ha svar som ikke er publisert, og alt i dette "
                    "repoet er åpent. Filen er slettet, men ligger i historikken. Si fra til redaktøren. Svarene "
                    "legges inn fra regjeringen.no med verktoy/budsjett_sporsmal_json.py"
                )
            elif type_ == "regnskap":
                from statsregnskap import legg_inn
                res = legg_inn(sti)
            elif type_ == "data":
                res = lag_tsv(sti, aar)
            else:
                res = del_opp_word(word, type_, aar, tillegg)
        except Exception as e:  # noqa: BLE001
            feilfil.write_text(f"{sti.name} ble ikke lagt inn.\n\nÅrsak: {e}\n\nRett opp og last opp filen på nytt. Denne filen forsvinner når filen er lagt inn.\n", encoding="utf-8")
            feil.append(f"{sti.name}: {e}")
            continue
        sti.unlink()
        if feilfil.exists():
            feilfil.unlink()
        ok.append(f"{sti.name}: {res}")
    if ok:
        oppdater_veiviser()
    tittel = f"Budsjett fra innboksen: {len(ok)} lagt inn, {len(feil)} stoppet"
    RAPPORT.write_text(tittel + "\n\n" + "\n".join(["Lagt inn:"] + [f"- {x}" for x in ok] + (["", "Stoppet:"] + [f"- {x}" for x in feil] if feil else [])) + "\n", encoding="utf-8")
    print(RAPPORT.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
