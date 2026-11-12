"""Lager en nøkkel over endringer i kapittel- og poststrukturen i statsbudsjettet fra år til år.

Strukturen for et budsjettår er postene som finnes i statsregnskapet, Stortingets vedtak eller Gul bok
det året (budsjett/ÅR/statsregnskap/poster.tsv, budsjett/ÅR/stortinget/vedtak.tsv og
budsjett/ÅR/gul-bok-bevilgninger.tsv i denne basen). Det gjelder alle departementer. Nøkkelen viser:

- ny: posten finnes ikke de to foregående årene
- borte: posten finnes ikke dette året eller året etter
- nytt_postnavn / nytt_kapittelnavn / nytt_departement: samme kapittel og post, men annet navn eller departement
- flyttet: forslag til hvor en ny post kommer fra, ut fra en post som ble borte samme år med likt eller
  nesten likt navn (sikkerhet «sikker» ved likt post- og kapittelnavn, ellers «mulig»)
- omtalt: proposisjonsteksten i basen sier at midler er «flytta/flyttet frå/fra/til kap. X, post Y»
  (sikkerhet «omtalt», med fil og sitat i kilde)

Postnummer som brukes på nytt for noe annet, vises som nytt_postnavn. Les derfor navnene.

Med REGELVERK_ROT=/sti/til/base lages nøkkelen for kapitlene under "kapitler" i budsjett.json der,
og proposisjonsteksten leses fra den basen. Utdata: budsjett/poststruktur.tsv.

Bruk: python3 verktoy/poststruktur.py
"""
import csv
import difflib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from basekonfig import ROT  # noqa: E402

KILDE = Path(__file__).resolve().parent.parent / "budsjett"
MAL = ROT / "budsjett"
KOLONNER = ["aar", "hendelse", "kap", "post", "kapnavn", "postnavn", "departement",
            "fra_kap", "fra_post", "fra_kapnavn", "fra_postnavn", "fra_departement", "sikkerhet", "kilde"]
TILLEGG = re.compile(r",\s*(kan (overføres|nyttes|benyttes)|overslagsbevilgning|kan overførast|kan nyttast"
                     r"|overslagsløyving).*$", re.I)


def les_tsv(sti):
    with open(sti, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def rens(navn):
    return TILLEGG.sub("", (navn or "").strip()).strip()


def filter_kapitler():
    sti = ROT / "budsjett.json"
    if not sti.exists() or MAL.resolve() == KILDE.resolve():
        return lambda kap: True
    oppsett = json.loads(sti.read_text(encoding="utf-8"))
    sett = []
    for d in oppsett.get("kapitler", []):
        fra, _, til = str(d).partition("-")
        sett.append((int(fra), int(til or fra)))
    if not sett:
        return lambda kap: True
    return lambda kap: any(a <= kap <= b for a, b in sett)


def struktur():
    """{år: {(kap, post): {"kapnavn", "postnavn", "departement"}}}, regnskap først, så Gul bok, så vedtak."""
    aar = {}
    for mappe in sorted(p for p in KILDE.iterdir() if p.is_dir() and p.name.isdigit()):
        poster = {}
        vedtak = mappe / "stortinget" / "vedtak.tsv"
        if vedtak.exists():
            for r in les_tsv(vedtak):
                if r["kap"].isdigit() and r["post"].isdigit():
                    poster[(int(r["kap"]), int(r["post"]))] = {
                        "kapnavn": r["kapnavn"], "postnavn": rens(r["postnavn"]), "departement": ""}
        gul = mappe / "gul-bok-bevilgninger.tsv"
        if gul.exists():
            for r in les_tsv(gul):
                if r["kap_nr"].isdigit() and r["post_nr"].isdigit():
                    poster[(int(r["kap_nr"]), int(r["post_nr"]))] = {
                        "kapnavn": r["kap_navn"], "postnavn": rens(r["post_navn"]), "departement": r["fdep_navn"]}
        regnskap = mappe / "statsregnskap" / "poster.tsv"
        if regnskap.exists():
            for r in les_tsv(regnskap):
                if r["kap"].isdigit() and r["post"].isdigit():
                    poster[(int(r["kap"]), int(r["post"]))] = {
                        "kapnavn": r["kap_navn"], "postnavn": rens(r["post_navn"]), "departement": r["fdep_navn"]}
        if poster:
            aar[int(mappe.name)] = poster
    return aar


def likhet(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def rad(aar, hendelse, kp, info, fra=None, fra_info=None, sikkerhet="", kilde=""):
    fra_info = fra_info or {}
    return {"aar": aar, "hendelse": hendelse, "kap": kp[0], "post": f"{kp[1]:02d}",
            "kapnavn": info.get("kapnavn", ""), "postnavn": info.get("postnavn", ""),
            "departement": info.get("departement", ""),
            "fra_kap": fra[0] if fra else "", "fra_post": f"{fra[1]:02d}" if fra else "",
            "fra_kapnavn": fra_info.get("kapnavn", ""), "fra_postnavn": fra_info.get("postnavn", ""),
            "fra_departement": fra_info.get("departement", ""), "sikkerhet": sikkerhet, "kilde": kilde}


def endringer(aar, med):
    ut = []
    alle = sorted(aar)
    for i, y in enumerate(alle[1:], 1):
        naa, forr = aar[y], aar[alle[i - 1]]
        forr2 = aar[alle[i - 2]] if i >= 2 else {}
        neste = aar[alle[i + 1]] if i + 1 < len(alle) else None
        nye = [k for k in naa if k not in forr and k not in forr2 and med(k[0])]
        # Posten er borte når den mangler dette året og året etter (et år uten føringer teller ikke).
        borte = [k for k in forr if k not in naa and (neste is None or k not in neste) and med(k[0])]
        for k in sorted(set(naa) & set(forr)):
            if not med(k[0]):
                continue
            a, b = forr[k], naa[k]
            if a["postnavn"] and b["postnavn"] and likhet(a["postnavn"], b["postnavn"]) < 0.8:
                ut.append(rad(y, "nytt_postnavn", k, b, k, a))
            elif a["kapnavn"] and b["kapnavn"] and likhet(a["kapnavn"], b["kapnavn"]) < 0.8 and k[1] == min(
                    p for kk, p in naa if kk == k[0]):
                ut.append(rad(y, "nytt_kapittelnavn", k, b, k, a))
            if a["departement"] and b["departement"] and a["departement"] != b["departement"] and k[1] == min(
                    p for kk, p in naa if kk == k[0]):
                ut.append(rad(y, "nytt_departement", k, b, k, a))
        brukt = set()
        for k in sorted(nye):
            info = naa[k]
            ut.append(rad(y, "ny", k, info))
            beste, poeng = None, 0
            for b in borte:
                if b in brukt:
                    continue
                fi = forr[b]
                p = likhet(info["postnavn"], fi["postnavn"]) * 0.6 + likhet(info["kapnavn"], fi["kapnavn"]) * 0.4
                if p > poeng:
                    beste, poeng = b, p
            if beste and poeng >= 0.75 and likhet(info["kapnavn"], forr[beste]["kapnavn"]) >= 0.6:
                fi = forr[beste]
                sikker = info["postnavn"].lower() == fi["postnavn"].lower() and \
                    info["kapnavn"].lower() == fi["kapnavn"].lower()
                ut.append(rad(y, "flyttet", k, info, beste, fi, "sikker" if sikker else "mulig"))
                brukt.add(beste)
        for k in sorted(borte):
            ut.append(rad(y, "borte", k, forr[k]))
    return ut


FLYTT = re.compile(r"([^.|]{0,200}?\bflytt\w*\s+(frå|fra|til)\s+(?:kap\.\s*(\d{1,4})(?:,?\s*post\s*(\d{1,2}))?"
                   r"|post\s*(\d{1,2}))[^.|]{0,120})", re.I)


def omtaler(aar, med):
    """Flytteomtaler i proposisjonene i basen: «flytta frå kap. X, post Y» i omtalen av kap. Z."""
    ut = []
    for fil in sorted(MAL.glob("[0-9][0-9][0-9][0-9]/prop-1-s-*/kap-*.md")):
        y = int(fil.parts[-3])
        m = re.match(r"kap-(\d+)\.md$", fil.name)
        if not m:
            continue
        kap = int(m.group(1))
        tekst = fil.read_text(encoding="utf-8")
        post_her = None
        for linje in tekst.splitlines():
            p = re.match(r"#{2,4}\s*Post\s+(\d{1,2})\b", linje)
            if p:
                post_her = int(p.group(1))
                continue
            for treff in FLYTT.finditer(linje):
                andre_kap = int(treff.group(3)) if treff.group(3) else kap
                andre_post = treff.group(4) or treff.group(5)
                andre_post = int(andre_post) if andre_post else None
                if not (med(kap) or med(andre_kap)) or andre_kap == kap and andre_post == post_her:
                    continue
                sitat = re.sub(r"\s+", " ", treff.group(1)).strip()
                her = (kap, post_her if post_her is not None else 0)
                der = (andre_kap, andre_post if andre_post is not None else 0)
                til, fra = (her, der) if treff.group(2).lower() in ("frå", "fra") else (der, her)
                info = aar.get(y, {}).get(til, {})
                fra_info = aar.get(y - 1, {}).get(fra, {}) or aar.get(y, {}).get(fra, {})
                r = rad(y, "omtalt", til, info, fra, fra_info, "omtalt",
                        f"{fil.relative_to(ROT)}: «{sitat}»")
                if til[1] == 0:
                    r["post"] = ""
                if fra[1] == 0:
                    r["fra_post"] = ""
                ut.append(r)
    return ut


def main():
    med = filter_kapitler()
    aar = struktur()
    rader = endringer(aar, med) + omtaler(aar, med)
    rekke = {"ny": 0, "flyttet": 1, "omtalt": 2, "borte": 3, "nytt_postnavn": 4, "nytt_kapittelnavn": 5,
             "nytt_departement": 6}
    rader.sort(key=lambda r: (r["aar"], int(r["kap"]), r["post"], rekke[r["hendelse"]]))
    sti = MAL / "poststruktur.tsv"
    sti.parent.mkdir(parents=True, exist_ok=True)
    with open(sti, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLONNER, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rader)
    teller = {}
    for r in rader:
        teller[r["hendelse"]] = teller.get(r["hendelse"], 0) + 1
    print(f"{sti.relative_to(ROT)}: {len(rader)} rader", teller)


if __name__ == "__main__":
    main()
