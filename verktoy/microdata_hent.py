#!/usr/bin/env python3
"""
Henter variabelkatalogen og brukerveiledningen fra microdata.no (SSB og Sikt) til data/microdata/.

Bruk:
    python3 verktoy/microdata_hent.py            # katalog og veiledning
    python3 verktoy/microdata_hent.py --katalog  # bare katalogen
    python3 verktoy/microdata_hent.py --manual   # bare veiledningen

Katalogen er åpen uten innlogging, men har ikke et dokumentert API. Skriptet bruker de samme
JSON-svarene som nettsiden microdata.no/discovery henter (Next.js, /_next/data/<byggid>/...).
Byggid leses fra nettsiden ved hver kjøring, fordi den endres når SSB og Sikt legger ut en ny
versjon av siden. Slutter dette å virke, er kopien i data/microdata/ det vi har.

Det som skrives:
  data/microdata/variabler.tsv         én rad per variabel i siste versjon av databanken
  data/microdata/variabler/<NAVN>.json variabelen slik katalogen gir den, med kodelister og historikk
                                        (kodelistene er lagret som endringer fra periode til periode)
  data/microdata/kodelister/<NAVN>.tsv gjeldende kodeliste (siste periode), regnet ut fra endringene
  data/microdata/manual/<sti>.md       hver side i brukerveiledningen (microdata.no/manual) som tekst
  data/microdata/status.tsv            når katalogen og veiledningen sist ble hentet og endret

En variabel hentes bare på nytt når «updatedAt» eller versjonen i katalogen er endret.
En side i veiledningen skrives bare på nytt når teksten er endret.
Variabler og sider som er borte hos kilden, slettes (de finnes i git-historikken).
"""
import datetime
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
MAPPE = ROT / "data" / "microdata"
VARMAPPE = MAPPE / "variabler"
KODEMAPPE = MAPPE / "kodelister"
MANMAPPE = MAPPE / "manual"
DISCOVERY = "https://microdata.no/discovery"
MANUAL = "https://microdata.no/manual/"
PAUSE = 0.3
UA = {"User-Agent": "regelverksbasen/1.0 (Offallnor/offdocs)"}
EPOKE = datetime.date(1970, 1, 1)


def les(url, forsok=4):
    req = urllib.request.Request(url, headers=UA)
    for i in range(forsok):
        time.sleep(PAUSE)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError) as e:
            if isinstance(e, urllib.error.HTTPError) and e.code == 404:
                raise
            if i == forsok - 1:
                raise
            time.sleep(10 * (i + 1))


def dato(dager):
    if dager is None:
        return ""
    return (EPOKE + datetime.timedelta(days=int(dager))).isoformat()


def skriv_hvis_endret(sti, tekst):
    sti.parent.mkdir(parents=True, exist_ok=True)
    data = tekst.encode("utf-8")
    if sti.exists() and sti.read_bytes() == data:
        return False
    sti.write_bytes(data)
    return True


# ---------------------------------------------------------------- katalog

def byggid():
    side = les(DISCOVERY + "/variables")
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', side, re.S)
    if not m:
        raise RuntimeError("Fant ikke __NEXT_DATA__ på microdata.no/discovery/variables")
    return json.loads(m.group(1))["buildId"]


def katalogsider(bid):
    alle, i = [], 0
    while True:
        d = json.loads(les(f"{DISCOVERY}/_next/data/{bid}/no/variables.json?pageIndex={i}"))
        data = d["pageProps"]["data"]
        alle += data["dataStructures"]
        if len(alle) >= data["totalCount"] or not data["dataStructures"]:
            return alle, data.get("dataStores", {}), data["totalCount"]
        i += 1


def finn_variabel(obj):
    """Detaljsiden har variabelen et sted i pageProps. Finn ordboken med measureVariable."""
    if isinstance(obj, dict):
        if "measureVariable" in obj and "name" in obj:
            return obj
        for k, v in obj.items():
            if k in ("versions", "_nextI18Next"):
                continue
            r = finn_variabel(v)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = finn_variabel(v)
            if r is not None:
                return r
    return None


def kodeliste_naa(rep):
    """Regner ut gjeldende kodeliste fra første liste og endringene (delta) i hver periode.
    Endringene leses slik: først fjernes posisjonene i «remove» (fra forrige liste), så bytter
    «replace» ut posisjoner i lista som er igjen, og til slutt settes «insert» inn på oppgitt
    posisjon i den nye lista. Rekkefølgen er funnet ved å sjekke at ingen kode blir dobbel
    (kommune- og landkodelistene). Gir None når en endring ikke går opp (for eksempel
    «reorder», som ikke er tolket) eller en kode blir dobbel."""
    liste = None
    for r in rep:
        vd = r.get("valueDomain") or {}
        if "codeList" in vd:
            liste = [dict(x) for x in vd["codeList"]]
            continue
        delta = vd.get("delta")
        if delta is None or liste is None:
            continue
        if delta.get("reorder"):
            return None
        fjern = set(delta.get("remove") or [])
        if any(i >= len(liste) for i in fjern):
            return None
        liste = [x for i, x in enumerate(liste) if i not in fjern]
        for pos, x in ((int(k), v) for k, v in (delta.get("replace") or {}).items()):
            if pos >= len(liste):
                return None
            liste[pos] = x
        for pos, x in sorted(((int(k), v) for k, v in (delta.get("insert") or {}).items())):
            if pos > len(liste):
                return None
            liste.insert(pos, x)
        koder = [x.get("code") for x in liste]
        if len(koder) != len(set(koder)):
            return None
    return liste


def rad(ds, detalj):
    mv = ds["measureVariable"]
    rep = (detalj or ds)["measureVariable"].get("representedVariables") or []
    siste = rep[-1] if rep else {}
    vd = siste.get("valueDomain") or {}
    ident = ", ".join(v.get("keyType", {}).get("label", "") for v in ds.get("identifierVariables", []))
    kl = kodeliste_naa(rep) if detalj else None
    tc = ds.get("temporalCoverage") or {}
    return [
        ds["name"], mv.get("label", ""), ident, ds.get("temporality", ""), mv.get("dataType", ""),
        vd.get("unitOfMeasure", ""), dato(tc.get("start")), dato(tc.get("stop")),
        "; ".join(ds.get("subjectFields") or []),
        "" if kl is None else str(len(kl)),
        datetime.datetime.fromtimestamp(ds["updatedAt"], datetime.UTC).date().isoformat() if ds.get("updatedAt") else "",
        ds.get("version", ""),
        re.sub(r"\s+", " ", siste.get("description", "")).strip(),
    ]


def ren(tekst):
    return str(tekst).replace("\t", " ").replace("\n", " ").replace("\r", " ")


def hent_katalog(rapport):
    VARMAPPE.mkdir(parents=True, exist_ok=True)
    KODEMAPPE.mkdir(parents=True, exist_ok=True)
    bid = byggid()
    liste, lagre, totalt = katalogsider(bid)
    if len(liste) < totalt or totalt < 100:
        raise RuntimeError(f"Katalogen ga {len(liste)} av {totalt} variabler. Stopper uten å skrive.")
    rader, nye, endret, feil = [], 0, 0, []
    navn_naa = set()
    for ds in sorted(liste, key=lambda x: x["name"]):
        navn = ds["name"]
        navn_naa.add(navn)
        sti = VARMAPPE / f"{navn}.json"
        gammel = json.loads(sti.read_text(encoding="utf-8")) if sti.exists() else None
        detalj = gammel
        if not gammel or gammel.get("updatedAt") != ds.get("updatedAt") or gammel.get("version") != ds.get("version"):
            hoved = ds["version"].split(".")[0]
            url = f"{DISCOVERY}/_next/data/{bid}/no/variable/{ds['dataStore']}/{hoved}/{urllib.parse.quote(navn)}.json"
            try:
                d = json.loads(les(url))
                detalj = finn_variabel(d.get("pageProps", {}))
                if detalj is None:
                    raise RuntimeError("fant ikke variabelen i svaret")
                detalj = {k: v for k, v in detalj.items() if k != "versions"}
                for k in ("updatedAt", "version", "dataStore", "id"):
                    detalj.setdefault(k, ds.get(k))
                skriv_hvis_endret(sti, json.dumps(detalj, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
                if gammel:
                    endret += 1
                else:
                    nye += 1
            except Exception as e:  # noqa: BLE001 – én feil skal ikke stoppe resten
                feil.append(f"{navn}: {e}")
                detalj = gammel
        r = rad(ds, detalj)
        rader.append(r)
        kl = kodeliste_naa(detalj["measureVariable"].get("representedVariables") or []) if detalj else None
        ksti = KODEMAPPE / f"{navn}.tsv"
        if kl:
            tekst = "kode\tkategori\n" + "".join(f"{ren(x.get('code', ''))}\t{ren(x.get('category', ''))}\n" for x in kl)
            skriv_hvis_endret(ksti, tekst)
        elif ksti.exists() and detalj and kl is None and "codeList" not in json.dumps(detalj):
            ksti.unlink()
    borte = sorted(p.stem for p in VARMAPPE.glob("*.json") if p.stem not in navn_naa)
    for n in borte:
        (VARMAPPE / f"{n}.json").unlink()
        k = KODEMAPPE / f"{n}.tsv"
        if k.exists():
            k.unlink()
    hode = ["navn", "etikett", "enhet", "temporalitet", "datatype", "maaleenhet", "fra", "til",
            "emner", "antall_koder", "oppdatert", "versjon", "beskrivelse"]
    tekst = "\t".join(hode) + "\n" + "".join("\t".join(ren(c) for c in r) + "\n" for r in rader)
    skriv_hvis_endret(MAPPE / "variabler.tsv", tekst)
    lagerinfo = "; ".join(f"{k} {v.get('version', '')}" for k, v in lagre.items())
    rapport.append(f"katalog: {len(rader)} variabler ({lagerinfo}), {nye} nye, {endret} endret, {len(borte)} borte, {len(feil)} feil")
    rapport += [f"  borte: {n}" for n in borte]
    rapport += [f"  feil: {f}" for f in feil]
    return not feil, nye + endret + len(borte) > 0


# ---------------------------------------------------------------- veiledning

class TilTekst(HTMLParser):
    """Gjør <article> i Docusaurus-sidene om til enkel Markdown."""
    HOPP = {"nav", "button", "svg", "script", "style", "footer"}
    TOMME = {"br", "img", "hr", "input", "meta", "link", "source", "wbr", "col", "area"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ut, self.hopp, self.pre, self.liste, self.lenke = [], 0, 0, [], None
        self.celler, self.tabell, self.kodespan = None, None, 0

    def skriv(self, s):
        if self.celler is not None:
            self.celler[-1] += s
        else:
            self.ut.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        klasse = a.get("class", "") or ""
        if self.hopp or tag in self.HOPP or "hash-link" in klasse:
            if tag not in self.TOMME:
                self.hopp += 1
            return
        if tag in ("h1", "h2", "h3", "h4", "h5"):
            self.skriv("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.skriv("\n\n")
        elif tag == "br":
            self.skriv("\n")
        elif tag == "pre":
            self.pre += 1
            self.skriv("\n\n```\n")
        elif tag == "code" and not self.pre:
            self.skriv("`")
        elif tag == "span" and "rosecodeblock" in klasse:
            self.kodespan += 1
            self.skriv("\n`")
        elif tag == "span" and "token-line" in klasse and self.pre:
            pass
        elif tag in ("strong", "b"):
            self.skriv("**")
        elif tag in ("em", "i"):
            self.skriv("*")
        elif tag in ("ul", "ol"):
            self.liste.append([tag, 0])
            self.skriv("\n")
        elif tag == "li":
            dyp = "  " * (len(self.liste) - 1)
            if self.liste and self.liste[-1][0] == "ol":
                self.liste[-1][1] += 1
                self.skriv(f"\n{dyp}{self.liste[-1][1]}. ")
            else:
                self.skriv(f"\n{dyp}- ")
        elif tag == "a":
            self.lenke = a.get("href")
        elif tag == "table":
            self.tabell = []
        elif tag == "tr":
            self.celler = []
        elif tag in ("td", "th") and self.celler is not None:
            self.celler.append("")
        elif tag == "img":
            alt = (a.get("alt") or "").strip()
            src = a.get("src") or ""
            if src.startswith("/"):
                src = "https://microdata.no" + src
            self.skriv(f"[bilde{': ' + alt if alt else ''}]({src})")

    def handle_endtag(self, tag):
        if self.hopp:
            if tag not in self.TOMME:
                self.hopp -= 1
            return
        if tag == "pre":
            self.pre -= 1
            self.skriv("\n```\n")
        elif tag == "code" and not self.pre:
            self.skriv("`")
        elif tag == "span" and self.kodespan:
            self.kodespan -= 1
            self.skriv("`")
        elif tag == "span" and self.pre:
            pass
        elif tag in ("strong", "b"):
            self.skriv("**")
        elif tag in ("em", "i"):
            self.skriv("*")
        elif tag in ("ul", "ol") and self.liste:
            self.liste.pop()
            self.skriv("\n")
        elif tag == "a":
            self.lenke = None
        elif tag == "tr" and self.celler is not None and self.tabell is not None:
            self.tabell.append([re.sub(r"\s+", " ", c).strip().replace("|", "\\|") for c in self.celler])
            self.celler = None
        elif tag == "table" and self.tabell is not None:
            rader = [r for r in self.tabell if r]
            if rader:
                n = max(len(r) for r in rader)
                rader = [r + [""] * (n - len(r)) for r in rader]
                self.ut.append("\n\n| " + " | ".join(rader[0]) + " |\n|" + "---|" * n + "\n")
                self.ut += ["| " + " | ".join(r) + " |\n" for r in rader[1:]]
            self.tabell = None

    def handle_data(self, data):
        if self.hopp:
            return
        if not self.pre:
            data = re.sub(r"\s+", " ", data)
        self.skriv(data.replace("​", ""))

    def tekst(self):
        t = "".join(self.ut).replace("\r\n", "\n").replace("\r", "\n")
        t = re.sub(r"[ \t]+\n", "\n", t)
        t = re.sub(r"\n{3,}", "\n\n", t)
        return t.strip() + "\n"


def manual_tekst(side):
    a, b = side.find("<article"), side.rfind("</article>")
    if a < 0 or b < 0:
        return None
    p = TilTekst()
    p.feed(side[a:b])
    return p.tekst()


def filnavn(sti):
    deler = [urllib.parse.unquote(d) for d in sti.strip("/").split("/") if d]
    ut = []
    for d in deler:
        d = d.lower().replace("∕", "-")
        d = re.sub(r"[^a-z0-9æøå.]+", "-", d).strip("-")
        ut.append(d or "x")
    return Path(*ut) if ut else Path("index")


def hent_manual(rapport):
    MANMAPPE.mkdir(parents=True, exist_ok=True)
    kart = les(MANUAL + "sitemap.xml")
    urler = []
    for loc in re.findall(r"<loc>([^<]+)</loc>", kart):
        sti = urllib.parse.urlsplit(html.unescape(loc)).path
        if not sti.startswith("/manual"):
            continue
        rest = sti[len("/manual"):].strip("/")
        if rest.startswith("en/") or rest == "en" or rest.startswith("test"):
            continue
        urler.append(rest)
    urler = sorted(set(urler))
    if len(urler) < 50:
        raise RuntimeError(f"Nettstedskartet ga bare {len(urler)} sider. Stopper uten å skrive.")
    skrevet, feil, finnes = 0, [], set()
    for rest in urler:
        url = MANUAL + urllib.parse.quote(urllib.parse.unquote(rest), safe="/") + ("/" if rest else "")
        mal = MANMAPPE / (str(filnavn(rest)) + ".md") if rest else MANMAPPE / "index.md"
        finnes.add(mal.resolve())
        try:
            tekst = manual_tekst(les(url))
        except Exception as e:  # noqa: BLE001
            feil.append(f"{rest}: {e}")
            continue
        if not tekst:
            feil.append(f"{rest}: fant ikke <article>")
            continue
        hode = f"<!-- kilde: {url} -->\n<!-- Brukerveiledningen for microdata.no (SSB og Sikt), hentet automatisk. -->\n\n"
        if skriv_hvis_endret(mal, hode + tekst):
            skrevet += 1
    borte = [p for p in MANMAPPE.rglob("*.md") if p.resolve() not in finnes]
    # Sletter ikke sider når mange feilet, så en midlertidig feil ikke tømmer kopien.
    if len(feil) < 5:
        for p in borte:
            p.unlink()
    rapport.append(f"veiledning: {len(urler)} sider, {skrevet} skrevet, {len(borte)} borte, {len(feil)} feil")
    rapport += [f"  feil: {f}" for f in feil]
    return not feil, skrevet + len(borte) > 0


def oppdater_status(navn, endret):
    sti = MAPPE / "status.tsv"
    rader = {}
    if sti.exists():
        for linje in sti.read_text(encoding="utf-8").splitlines()[1:]:
            d = linje.split("\t")
            if len(d) == 3:
                rader[d[0]] = d
    idag = datetime.date.today().isoformat()
    forrige = rader.get(navn, [navn, "", ""])
    rader[navn] = [navn, idag, idag if endret or not forrige[2] else forrige[2]]
    tekst = "del\tsist_hentet\tsist_endret\n" + "".join("\t".join(r) + "\n" for _, r in sorted(rader.items()))
    sti.write_text(tekst, encoding="utf-8")


def main():
    args = set(sys.argv[1:])
    gjor_k = not args or "--katalog" in args
    gjor_m = not args or "--manual" in args
    rapport, ok = [], True
    for gjor, navn, fn in ((gjor_k, "katalog", hent_katalog), (gjor_m, "veiledning", hent_manual)):
        if not gjor:
            continue
        try:
            del_ok, endret = fn(rapport)
            ok &= del_ok
            oppdater_status(navn, endret)
        except Exception as e:  # noqa: BLE001
            rapport.append(f"{navn}: FEIL {e}")
            ok = False
    print("\n".join(rapport))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
