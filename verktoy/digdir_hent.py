#!/usr/bin/env python3
"""Henter digitaliseringsveiledere fra Digitaliseringsdirektoratet (digdir.no) til veiledere/digitalisering/.

Digdirs sider er flate: et kapittel ligger ikke under veilederens sti, men har egen adresse med
nummer (f.eks. /digital-samhandling/prinsipp-1-ta-utgangspunkt-i-brukernes-behov/1055). Hver veileder
i DOKUMENTER har derfor en startside og et mønster for hvilke lenker i selve innholdet på startsiden
som er kapitler. Lenker i menyer og bunntekst telles ikke med.

1. Henter startsiden (og eventuelle listesider), finner kapitlene og henter dem.
2. Sammenligner teksten med sjekksummen i veiledere/digitalisering.tsv. Bare veiledere der teksten
   er endret, skrives på nytt.
3. Hver veileder legges i veiledere/digitalisering/<mappe>/ med oversikt.md (startsiden og
   innholdslisten) og én fil per kapittel. veiledere/digitalisering/oversikt.md lister alle.

Digitaliseringsrundskrivet ligger på regjeringen.no, som stenger ute automatisk henting. Det hentes
fra Digdirs åpne kopi i GitHub-repoet digdir/nasjonal-arkitektur (MIT-lisens), og det står i filen.

robots.txt på digdir.no tillater innholdssidene. Skriptet bruker samme åpne User-Agent og pause
som verktoy/nettsider_hent.py, og låner HTML-til-Markdown derfra.
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import sys
import urllib.error
from pathlib import Path

from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nettsider_hent as nh  # noqa: E402
from basekonfig import ROT  # noqa: E402

BASE = "https://www.digdir.no"
UTGIVER = "Digitaliseringsdirektoratet (Digdir)"
MAPPE = ROT / "veiledere" / "digitalisering"
STATUS = ROT / "veiledere" / "digitalisering.tsv"
RAPPORT = ROT / "digdir-rapport.txt"
KOLONNER = ["mappe", "tittel", "kilde", "sider", "sjekksum", "lagt_inn"]
INNHOLD = ["main", "#main-content", "article"]
# Støy på digdir.no. Strengere enn i nettsider_hent.py, som også fjerner "navigation" og "header":
# her står kapitlene som navigation-card og overskriftene i section__header.
STØY = re.compile(r"breadcrumb|share|social|feedback|cookie|skip|menu|tilbakemelding|print|footer|secondary-nav"
                  r"|brand-banner|search", re.I)

# Felles arkitektur for samhandling (inngangssiden 2150 og delene den samler) og digitaliseringsrundskrivet.
# "folg": regulært uttrykk for kapitlene, testet mot stien. "dybde": hvor mange ledd lenker følges.
# "lister": flere listesider (f.eks. side 2 av en oversikt) som bare brukes til å finne kapitler.
DOKUMENTER = [
    {"mappe": "nasjonal-arkitektur", "gruppe": "Felles arkitektur for samhandling",
     "start": "/digital-samhandling/nasjonal-arkitektur-standarder-og-informasjonsforvaltning/2150"},
    {"mappe": "arkitekturprinsipper", "gruppe": "Felles arkitektur for samhandling",
     "start": "/digital-samhandling/overordnede-arkitekturprinsipper/1065",
     "folg": r"^/digital-samhandling/(prinsipp-\d[^/]*|endringshistorikk-og-versjonslogg|foringar-bruk-av-arkitekturprinsippa)/\d+$",
     "ekstra": ["/digital-samhandling/foringar-bruk-av-arkitekturprinsippa/1066"]},
    {"mappe": "rammeverk-digital-samhandling", "gruppe": "Felles arkitektur for samhandling",
     "start": "/digital-samhandling/rammeverk-digital-samhandling/2148",
     "ekstra": ["/digital-samhandling/slik-anvender-du-rammeverket-digital-samhandling-i-praksis/1689"]},
    {"mappe": "felles-okosystem", "gruppe": "Felles arkitektur for samhandling",
     "start": "/digital-samhandling/felles-okosystem/4165", "dybde": 2,
     "folg": r"^/digital-samhandling/(hva-er-felles-okosystem|innledning|modell-felles-okosystem|kart-tjenestekjeder"
             r"|arkitektur-hendelser-i-felles-okosystem|samspill-i-felles-okosystem|eksempler-pa-behov-og-scenarier"
             r"|leseliste-og-kilder)/\d+$",
     "ekstra": ["/digital-samhandling/innledning/4169", "/digital-samhandling/kart-tjenestekjeder/4168",
                "/digital-samhandling/arkitektur-hendelser-i-felles-okosystem/4691",
                "/digital-samhandling/arkitektur-hendelser-i-felles-okosystem/4692",
                "/digital-samhandling/samspill-i-felles-okosystem/4693",
                "/digital-samhandling/eksempler-pa-behov-og-scenarier/4694",
                "/digital-samhandling/leseliste-og-kilder/4696"]},
    {"mappe": "krav-og-anbefalinger", "gruppe": "Felles arkitektur for samhandling",
     "start": "/digitalisering-og-samordning/oversikt-over-krav-og-anbefalinger-innenfor-digitalisering/2617",
     "lister": ["?page=1", "?page=2"],
     "folg": r"^/(krav-og-anbefalinger|digitalisering-og-samordning|felleslosninger|informasjonssikkerhet)/[a-z0-9-]+/\d+$",
     "utelat": r"/(oversikt-over-krav|krav-og-anbefalingar-innan|introduksjon-til-krav|rad-om-digitaliseringsarbeid"
               r"|samordning-og-koordinering|fremtidens-digitale-norge|anbefaling-produktorganisering)"},
    {"mappe": "referansekatalogen", "gruppe": "Felles arkitektur for samhandling",
     "start": "/standarder/referansekatalogen-it-standardar/1480",
     "folg": r"^/standarder/[a-z0-9-]+/\d+$",
     "utelat": r"/(referansekatalogen-it-standardar|hoyringar|gamle-versjonar|arkitektur-og-standardiseringsradet"
               r"|msp-og-internasjonalt|utgreiing-av-nye-krav|standardar)/"},
]
RUNDSKRIV = {
    "mappe": "digitaliseringsrundskrivet", "gruppe": "Digitaliseringsrundskrivet",
    "kilde": "https://raw.githubusercontent.com/digdir/nasjonal-arkitektur/main/arkitekturassistent/Digitaliseringsrundskrivet.md",
    "side": "https://github.com/digdir/nasjonal-arkitektur/blob/main/arkitekturassistent/Digitaliseringsrundskrivet.md",
}


def les(sti: str) -> tuple:
    """(tittel, markdown, [lenkestier i innholdet]) for én side på digdir.no, eller (None, None, [])."""
    url = sti if sti.startswith("http") else BASE + sti
    try:
        html = nh.hent(url)
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            print(f"  finnes ikke: {url}")
            return None, None, []
        raise
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find("h1")
    tittel = re.sub(r"\s+", " ", h1.get_text(" ", strip=True)) if h1 else sti.rstrip("/").rsplit("/", 1)[-1]
    innhold = next((e for v in INNHOLD if (e := soup.select_one(v))), None) or soup.body
    for t in innhold.find_all(["nav", "aside", "header", "footer", "form", "script", "style", "noscript"]):
        t.decompose()
    for t in innhold.find_all(True):
        if t.attrs is None:
            continue
        merker = " ".join(t.get("class", [])) + " " + (t.get("id") or "")
        if STØY.search(merker) and t.name not in ("main", "article", "body"):
            t.decompose()
    lenker = []
    for a in innhold.find_all("a", href=True):
        h = a["href"].split("#")[0].split("?")[0].removeprefix(BASE)
        if h.startswith("/") and h not in lenker:
            lenker.append(h)
    md = re.split(r"\n#+ Kontakt\s*\n", nh.markdown(innhold))[0].rstrip()  # kontaktpersoner tas ikke med
    return tittel, md, lenker


def kapitler(dok: dict, lenker: list) -> list:
    """Stiene til kapitlene, i rekkefølgen de står på startsiden, uten startsiden selv."""
    if "folg" not in dok:
        return list(dok.get("ekstra", []))
    folg, utelat = re.compile(dok["folg"]), re.compile(dok["utelat"]) if dok.get("utelat") else None
    ut = []
    for h in lenker + dok.get("ekstra", []):
        if h != dok["start"] and folg.search(h) and not (utelat and utelat.search(h)) and h not in ut:
            ut.append(h)
    return ut


def les_dokument(dok: dict) -> tuple:
    """(tittel, forside, [(sti, tittel, markdown)])"""
    tittel, forside, lenker = les(dok["start"])
    if tittel is None:
        raise RuntimeError(f"startsiden finnes ikke: {dok['start']}")
    for liste in dok.get("lister", []):
        _, _, flere = les(dok["start"] + liste)
        lenker += [h for h in flere if h not in lenker]
    kø, sett, sider = kapitler(dok, lenker), set(), []
    for _ in range(dok.get("dybde", 1)):
        neste = []
        for sti in kø:
            if sti in sett:
                continue
            sett.add(sti)
            t, md, under = les(sti)
            if t is None:
                continue
            if md.strip() == forside.strip() or any(md == m for _, _, m in sider):
                continue  # samme tekst som startsiden eller et annet kapittel (videresending)
            if t.startswith(tittel + " "):
                t = t[len(tittel) + 1:]
            sider.append((sti, t, md))
            neste += [h for h in kapitler(dok, under) if h not in sett]
        kø = neste
    return tittel, forside, sider


def filnavn(nr: int, sti: str) -> str:
    slug = sti.rstrip("/").split("/")[-2]
    return f"{nr:02d}-{re.sub(r'[^0-9a-z]+', '-', slug.lower()).strip('-')[:70]}.md"


def hode(tittel: str, kilde: str, dato: str) -> str:
    return "\n".join(["---", f'veileder: "{tittel}"', f'utgiver: "{UTGIVER}"', f'kilde: "{kilde}"',
                      f'hentet: "{dato}"', "---"])


def skriv(dok: dict, tittel: str, forside: str, sider: list, dato: str) -> None:
    mappe = MAPPE / dok["mappe"]
    if mappe.exists():
        shutil.rmtree(mappe)
    mappe.mkdir(parents=True)
    innhold = []
    for nr, (sti, t, md) in enumerate(sider, 1):
        fil = filnavn(nr, sti)
        (mappe / fil).write_text(f"{hode(tittel, BASE + sti, dato)}\n\n# {t}\n\n{md}\n", encoding="utf-8")
        innhold.append(f"- {t} – `{fil}`")
    (mappe / "oversikt.md").write_text(
        f"{hode(tittel, BASE + dok['start'], dato)}\n\n# {tittel}\n\n"
        f"Tekst fra Digitaliseringsdirektoratet, hentet fra [digdir.no]({BASE + dok['start']}) {dato}. "
        "Den er veiledning, ikke lov eller forskrift. Hvilke krav som er pålagt statlige virksomheter, står i "
        "digitaliseringsrundskrivet.\n\n"
        + (forside + "\n\n" if forside else "")
        + ("## Kapitler\n\n" + "\n".join(innhold) + "\n" if innhold else ""), encoding="utf-8")


def skriv_rundskriv(tekst: str, dato: str) -> str:
    mappe = MAPPE / RUNDSKRIV["mappe"]
    if mappe.exists():
        shutil.rmtree(mappe)
    mappe.mkdir(parents=True)
    tittel = "Digitaliseringsrundskrivet"
    m = re.search(r"\*\*Nr:\*\*\s*([A-Z]-\d+/\d+)", tekst)
    nr = m.group(1) if m else ""
    d = re.search(r"Dato:\s*([0-9.]+)", tekst)
    tittel_full = f"{tittel} ({nr}, {d.group(1)})" if nr and d else tittel
    (mappe / "rundskrivet.md").write_text(
        f"{hode(tittel_full, RUNDSKRIV['side'], dato)}\n\n"
        "> Rundskrivet er publisert på regjeringen.no. Teksten her er Digdirs kopi i "
        "GitHub-repoet digdir/nasjonal-arkitektur, fordi regjeringen.no ikke slipper til automatisk henting. "
        "Kontroller mot regjeringen.no ved tvil om ordlyden, og om det er kommet en nyere utgave.\n\n"
        + tekst.strip() + "\n", encoding="utf-8")
    (mappe / "oversikt.md").write_text(
        f"{hode(tittel_full, RUNDSKRIV['side'], dato)}\n\n# {tittel_full}\n\n"
        "Sammenstilling av pålegg og anbefalinger om digitalisering i offentlig sektor. Gjelder for "
        "departementene, statens ordinære forvaltningsorganer, forvaltningsorganer med særskilte fullmakter "
        "og forvaltningsbedrifter. Rundskrivet skiller mellom krav, anbefalinger og veiledning.\n\n"
        "Teksten er Digdirs kopi i GitHub, ikke hentet direkte fra regjeringen.no.\n\n"
        "## Fil\n\n- Hele rundskrivet – `rundskrivet.md`\n", encoding="utf-8")
    return tittel_full


def les_status() -> dict:
    if not STATUS.exists():
        return {}
    linjer = STATUS.read_text(encoding="utf-8").splitlines()
    return {r["mappe"]: r for r in (dict(zip(KOLONNER, l.split("\t"))) for l in linjer[1:] if l)}


def skriv_status(status: dict) -> None:
    linjer = ["\t".join(KOLONNER)] + ["\t".join(status[m].get(k, "") for k in KOLONNER) for m in sorted(status)]
    STATUS.write_text("\n".join(linjer) + "\n", encoding="utf-8")


def skriv_oversikt(status: dict) -> None:
    grupper = {}
    for dok in DOKUMENTER + [RUNDSKRIV]:
        rad = status.get(dok["mappe"])
        if rad and (MAPPE / dok["mappe"]).exists():
            grupper.setdefault(dok["gruppe"], []).append(rad)
    linjer = ["# Digitaliseringsveiledere", "",
              "Veiledning om digitalisering i offentlig sektor fra Digitaliseringsdirektoratet (Digdir), og "
              "digitaliseringsrundskrivet. Veilederne er ikke lov eller forskrift. Rundskrivet gir pålegg til "
              "statlige virksomheter. Hver veileder har en mappe med `oversikt.md` og én fil per kapittel.", ""]
    for gruppe in ["Digitaliseringsrundskrivet", "Felles arkitektur for samhandling"]:
        if gruppe not in grupper:
            continue
        linjer += [f"## {gruppe}", "", "| Veileder | Sider | Hentet | Sti |", "|---|---|---|---|"]
        for rad in grupper[gruppe]:
            linjer.append(f"| {rad['tittel'].replace('|', '/')} | {rad['sider']} | {rad['lagt_inn']} | "
                          f"`veiledere/digitalisering/{rad['mappe']}/oversikt.md` |")
        linjer.append("")
    (MAPPE / "oversikt.md").write_text("\n".join(linjer), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tving", action="store_true", help="skriv alt på nytt")
    args = ap.parse_args()
    nh.BASE = BASE
    dato = datetime.date.today().isoformat()
    status = les_status()
    logg = {"Ny": [], "Endret": []}
    feil = []
    MAPPE.mkdir(parents=True, exist_ok=True)

    for dok in DOKUMENTER:
        try:
            tittel, forside, sider = les_dokument(dok)
        except Exception as e:  # noqa: BLE001
            print(f"FEIL {dok['mappe']}: {e}")
            feil.append(dok["mappe"])
            continue
        sjekksum = hashlib.sha256(json.dumps([tittel, forside, sider], ensure_ascii=False).encode()).hexdigest()[:16]
        gammel = status.get(dok["mappe"])
        rad = {"mappe": dok["mappe"], "tittel": tittel.replace("\t", " "), "kilde": BASE + dok["start"],
               "sider": str(len(sider) + 1)}
        print(f"{dok['mappe']}: {tittel} ({len(sider) + 1} sider)")
        if gammel and gammel.get("sjekksum") == sjekksum and (MAPPE / dok["mappe"]).exists() and not args.tving:
            status[dok["mappe"]] = {**gammel, **rad}
            continue
        skriv(dok, tittel, forside, sider, dato)
        status[dok["mappe"]] = {**rad, "sjekksum": sjekksum, "lagt_inn": dato}
        logg["Endret" if gammel else "Ny"].append(f"{tittel} ({len(sider) + 1} sider)")

    try:
        tekst = nh.hent(RUNDSKRIV["kilde"])
        sjekksum = hashlib.sha256(tekst.encode()).hexdigest()[:16]
        gammel = status.get(RUNDSKRIV["mappe"])
        if not (gammel and gammel.get("sjekksum") == sjekksum and (MAPPE / RUNDSKRIV["mappe"]).exists()
                and not args.tving):
            tittel = skriv_rundskriv(tekst, dato)
            status[RUNDSKRIV["mappe"]] = {"mappe": RUNDSKRIV["mappe"], "tittel": tittel, "kilde": RUNDSKRIV["side"],
                                          "sider": "1", "sjekksum": sjekksum, "lagt_inn": dato}
            logg["Endret" if gammel else "Ny"].append(tittel)
    except Exception as e:  # noqa: BLE001
        print(f"FEIL digitaliseringsrundskrivet: {e}")
        feil.append(RUNDSKRIV["mappe"])

    skriv_status(status)
    skriv_oversikt(status)
    if any(logg.values()):
        melding = [f"Digitaliseringsveiledere: {len(logg['Ny'])} nye, {len(logg['Endret'])} endret", ""]
        melding += [f"- {typ}: {l}" for typ, linjer in logg.items() for l in linjer]
        RAPPORT.write_text("\n".join(melding) + "\n", encoding="utf-8")
        print("\n".join(melding))
    if feil:
        print("FEIL:", ", ".join(feil))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
