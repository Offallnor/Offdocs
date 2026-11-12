#!/usr/bin/env python3
"""
Henter grunnbeløpet i folketrygden (G) for alle år fra nav.no/grunnbelopet og lagrer det i data/grunnbelop.tsv.

Bruk:
    python3 verktoy/grunnbelop_hent.py [--tor] [--fil side.html]

Navs side har én tabell per regulering (dato, G, G per måned, gjennomsnitt per år og omregningsfaktor).
Kontroller før filen skrives:
  1. Minst 70 reguleringer, og hver har dato og G.
  2. G øker for hver regulering.
  3. Siste G er lik grunnbeløpet i grunnbeløpsforskriften § 1 i regelverksbasen.
Feil gir exit-kode 1 og ingen ny fil. Med --tor skrives ingenting. --fil leser en lagret side i stedet for nav.no.
Rapporten skrives til grunnbelop-rapport.txt.
"""
import datetime
import html
import re
import sys
import urllib.request
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
UT = ROT / "data" / "grunnbelop.tsv"
FORSKRIFT = ROT / "regelverk" / "folketrygdloven" / "forskrifter" / "grunnbelop-og-satser" / "par-1.md"
KILDE = "https://www.nav.no/grunnbelopet"
RAPPORT = ROT / "grunnbelop-rapport.txt"
UA = "Mozilla/5.0 (regelverksbasen; datakatalog)"

MND = {"januar": 1, "februar": 2, "mars": 3, "april": 4, "mai": 5, "juni": 6, "juli": 7,
       "august": 8, "september": 9, "oktober": 10, "november": 11, "desember": 12}


def rens(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()


def dato(t):
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", t)
    if m:
        return datetime.date(int(m[3]), int(m[2]), int(m[1]))
    m = re.fullmatch(r"(\d{1,2})\. (\w+) (\d{4})", t.lower())
    if m and m[2] in MND:
        return datetime.date(int(m[3]), MND[m[2]], int(m[1]))
    raise ValueError(f"ukjent dato: {t!r}")


def kroner(t):
    t = re.sub(r"\s*(kroner|kr)\.?$", "", t).replace(" ", "")
    return int(t) if t else None


def les(side):
    rader = []
    for tabell in re.findall(r"<table.*?</table>", side, re.S):
        celler = {}
        for tr in re.findall(r"<tr.*?</tr>", tabell, re.S):
            c = [rens(x) for x in re.findall(r"<t[hd].*?</t[hd]>", tr, re.S)]
            if len(c) == 2 and c[0] not in celler:
                celler[c[0]] = c[1]
        if "Dato og år" not in celler or "Grunnbeløpet (G)" not in celler:
            continue
        rader.append({
            "dato": dato(celler["Dato og år"]),
            "grunnbelop": kroner(celler["Grunnbeløpet (G)"]),
            "per_maaned": kroner(celler.get("Grunnbeløp per måned", "")),
            "gjennomsnitt_aar": kroner(celler.get("Gjennomsnitt per år", "")),
            "omregningsfaktor": celler.get("Omregningsfaktor", "").replace(",", ".") or None,
        })
    return sorted(rader, key=lambda r: r["dato"])


def kontroller(rader):
    feil = []
    if len(rader) < 70:
        feil.append(f"bare {len(rader)} reguleringer funnet, ventet minst 70")
    for a, b in zip(rader, rader[1:]):
        if not b["grunnbelop"] or not a["grunnbelop"] or b["grunnbelop"] <= a["grunnbelop"]:
            feil.append(f"G øker ikke fra {a['dato']} ({a['grunnbelop']}) til {b['dato']} ({b['grunnbelop']})")
    if FORSKRIFT.exists() and rader:
        m = re.search(r"fastsettes til ([\d  ]+) kroner", FORSKRIFT.read_text(encoding="utf-8"))
        if m:
            g = int(re.sub(r"\D", "", m[1]))
            if g != rader[-1]["grunnbelop"]:
                feil.append(f"siste G hos Nav ({rader[-1]['grunnbelop']}, {rader[-1]['dato']}) er ikke lik "
                            f"grunnbeløpsforskriften § 1 ({g})")
    return feil


def skriv(rader):
    linjer = [
        "# Kilde: Nav",
        "# Tabell: Grunnbeløpet i folketrygden (G), alle reguleringer",
        f"# Kildeside: {KILDE}",
        f"# Hentet: {datetime.date.today().isoformat()}",
        "# dato: datoen G gjelder fra. gjennomsnitt_aar: gjennomsnittlig G i kalenderåret (tom når det er flere"
        " reguleringer samme år, da står gjennomsnittet på siste regulering). omregningsfaktor: forholdet til"
        " forrige G, slik Nav oppgir det.",
        "dato\tgrunnbelop\tper_maaned\tgjennomsnitt_aar\tomregningsfaktor",
    ]
    for r in reversed(rader):
        linjer.append("\t".join("" if r[k] is None else str(r[k]) for k in
                                ("dato", "grunnbelop", "per_maaned", "gjennomsnitt_aar", "omregningsfaktor")))
    ny = "\n".join(linjer) + "\n"
    if UT.exists():
        gammel = UT.read_text(encoding="utf-8").splitlines()
        if [l for l in gammel if not l.startswith("# Hentet:")] == [l for l in ny.splitlines() if not l.startswith("# Hentet:")]:
            return False
    UT.write_text(ny, encoding="utf-8")
    return True


def main():
    tor = "--tor" in sys.argv
    if "--fil" in sys.argv:
        side = Path(sys.argv[sys.argv.index("--fil") + 1]).read_text(encoding="utf-8")
    else:
        req = urllib.request.Request(KILDE, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            side = r.read().decode("utf-8", "replace")
    rader = les(side)
    feil = kontroller(rader)
    if feil:
        RAPPORT.write_text("Grunnbeløpet: ikke lagt inn\n" + "\n".join(f"- {f}" for f in feil) + "\n", encoding="utf-8")
        print(RAPPORT.read_text(encoding="utf-8"))
        sys.exit(1)
    endret = False if tor else skriv(rader)
    tekst = (f"Grunnbeløpet: {len(rader)} reguleringer, siste {rader[-1]['dato']} ({rader[-1]['grunnbelop']} kroner). "
             + ("Endret." if endret else "Uendret." if not tor else "Prøvekjøring, ingenting skrevet."))
    RAPPORT.write_text(tekst + "\n", encoding="utf-8")
    print(tekst)


if __name__ == "__main__":
    main()
