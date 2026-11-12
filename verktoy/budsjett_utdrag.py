"""Lager utdrag av Stortingets budsjettvedtak og statsregnskapet for kapitlene til en annen base.

Denne basen har vedtakene (budsjett/ÅR/stortinget/) og statsregnskapet (budsjett/ÅR/statsregnskap/)
for alle departementer. En base for et annet område kan få radene for sine kapitler uten å hente
dataene selv. Kapitlene står under "kapitler" i budsjett.json i den andre basen, f.eks.
["200-299", "2410", "3200-3299", "5310", "5617"].

Bruk: REGELVERK_ROT=/sti/til/base python3 verktoy/budsjett_utdrag.py

Filene i den andre basen erstattes hver gang. Kolonnene er de samme som her.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from basekonfig import ROT  # noqa: E402

KILDE = Path(__file__).resolve().parent.parent / "budsjett"
MAL = ROT / "budsjett"
# fil -> kolonnen med kapittelnummer (None: radene velges ut fra andre filer)
FILER = {
    "stortinget": {"vedtak.tsv": "kap", "partiforslag.tsv": "kap", "kilder.tsv": None},
    "statsregnskap": {"poster.tsv": "kap", "maaned.tsv": "kap", "artskonto.tsv": "kap", "virksomhet.tsv": "kap"},
}


def kapitler(oppsett):
    sett = []
    for d in oppsett.get("kapitler", []):
        fra, _, til = str(d).partition("-")
        sett.append((int(fra), int(til or fra)))
    if not sett:
        raise SystemExit('budsjett.json i basen mangler "kapitler"')
    return lambda kap: kap.isdigit() and any(a <= int(kap) <= b for a, b in sett)


def les(sti):
    linjer = sti.read_text(encoding="utf-8").splitlines()
    return linjer[0], [l.split("\t") for l in linjer[1:] if l]


def skriv(sti, hode, rader):
    sti.parent.mkdir(parents=True, exist_ok=True)
    sti.write_text(hode + "\n" + "".join("\t".join(r) + "\n" for r in rader), encoding="utf-8")


def main():
    if MAL.resolve() == KILDE.resolve():
        raise SystemExit("REGELVERK_ROT må peke på en annen base")
    oppsett = json.loads((ROT / "budsjett.json").read_text(encoding="utf-8"))
    hører_til = kapitler(oppsett)
    rapport = []
    for aar in sorted(p for p in KILDE.iterdir() if p.is_dir() and p.name.isdigit()):
        for mappe, filer in FILER.items():
            if not (aar / mappe).is_dir():
                continue
            brukte_innst = set()
            antall = 0
            for navn, kol in filer.items():
                kilde = aar / mappe / navn
                if not kilde.exists():
                    continue
                hode, rader = les(kilde)
                koler = hode.split("\t")
                if kol:
                    i = koler.index(kol)
                    valgt = [r for r in rader if len(r) > i and hører_til(r[i])]
                    if "innstilling" in koler:
                        j = koler.index("innstilling")
                        brukte_innst |= {r[j] for r in valgt}
                    antall += len(valgt) if navn in ("vedtak.tsv", "poster.tsv") else 0
                else:
                    j = koler.index("innstilling")
                    valgt = [r for r in rader if r[j] in brukte_innst]
                skriv(MAL / aar.name / mappe / navn, hode, valgt)
            rapport.append(f"{aar.name} {mappe}: {antall} rader")
    status = KILDE / "statsregnskap.tsv"
    if status.exists():
        skriv(MAL / "statsregnskap.tsv", *les(status))
    from budsjett_innboks import oppdater_veiviser
    oppdater_veiviser()
    print("\n".join(rapport))


if __name__ == "__main__":
    main()
