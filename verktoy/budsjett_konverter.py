"""Gjør eldre utgaver av budsjettdokumenter fra regjeringen.no om til Word, så verktoy/budsjett.py kan dele dem opp.

Regjeringen.no har Word-filer (docx) fra omtrent 2020. Eldre proposisjoner finnes som:

- RTF i zip (…rtfz.zip), omtrent 2015–2019. RTF-filen har de samme stilnavnene som Word-malen og gjøres om
  med LibreOffice (soffice).
- EPUB, omtrent 2013–2014. EPUB-filen er XHTML med klassenavn som svarer til stilene i Word-malen
  (K-TIT-BUDKAP for budsjettkapittel, K-TIT-POST for post osv.). Den bygges om til en Word-fil med
  de stilnavnene budsjett.py venter.

Bruk: python3 verktoy/budsjett_konverter.py <fil> <utmappe>   (skriver <utmappe>/<filnavn>.docx)
"""
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ENDELSER = (".rtf", ".zip", ".epub")
XHTML = "{http://www.w3.org/1999/xhtml}"
OPF = "{http://www.idpf.org/2007/opf}"

# Klassenavn i EPUB -> stilnavn i Word-malen
OVERSKRIFTER = {
    "K-TIT-PUBLIKASJONSTITTEL": "i-hode",
    "K-TERMIN-FORSIDE": "i-termin",
    "K-TIT-KAPITTEL": "Heading 1",
    "K-TIT-PROGKAT": "b-progkat",
    "K-TIT-BUDKAP": "b-budkaptit",
    "K-TIT-POST": "b-post",
    "K-TIT-MTIT": "avsnitt-tittel",
    "K-TIT-MUTIT": "avsnitt-undertittel",
    "K-TIT-MUTIT2": "avsnitt-under-undertittel",
    "K-TIT-UNDERTIT": "Heading 2",
    "K-TIT-SEKSJON": "Heading 2",
    "K-TIT-RAMME": "avsnitt-tittel",
    "K-TIT-VEDLEGG": "vedlegg-tit",
    "K-TIT-FULLMAKTTIT": "Fullmakttit",
    "K-TIT-VEDTAKDEL": "a-vedtak-del",
    "K-TIT-TILRSTAD": "a-tilraar",
    "K-TIT-VEDTAKFORSLAG": "a-vedtak-tit",
    "K-TIT-FIGGRP": "figur-tittel",
    "K-TITLE": "Tabellnavn",
}
ROMERTALL = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V"}


def til_docx(sti: Path, utmappe: Path) -> Path:
    """Word-fil laget fra sti (RTF, zip med RTF eller Word, eller EPUB)."""
    utmappe.mkdir(parents=True, exist_ok=True)
    ut = utmappe / (sti.stem + ".docx")
    endelse = sti.suffix.lower()
    if endelse == ".zip":
        with zipfile.ZipFile(sti) as z:
            inni = [n for n in z.namelist() if n.lower().endswith((".rtf", ".docx")) and not n.startswith("__MACOSX")]
            if len(inni) != 1:
                raise ValueError(f"zip-filen skal ha nøyaktig én RTF- eller Word-fil, men har {len(inni)}")
            tmp = Path(tempfile.mkdtemp())
            fil = tmp / Path(inni[0]).name
            fil.write_bytes(z.read(inni[0]))
        if fil.suffix.lower() == ".docx":
            shutil.copy(fil, ut)
            return ut
        return rtf_til_docx(fil, ut)
    if endelse == ".rtf":
        return rtf_til_docx(sti, ut)
    if endelse == ".epub":
        return epub_til_docx(sti, ut)
    raise ValueError(f"kan ikke gjøre om {endelse}-filer")


def rtf_til_docx(sti: Path, ut: Path) -> Path:
    if not shutil.which("soffice"):
        raise ValueError("LibreOffice (soffice) mangler, så RTF-filen kan ikke gjøres om til Word")
    tmp = Path(tempfile.mkdtemp())
    subprocess.run(["soffice", "--headless", "--convert-to", "docx", "--outdir", str(tmp), str(sti)],
                   check=True, capture_output=True, timeout=900)
    laget = tmp / (sti.stem + ".docx")
    if not laget.exists():
        raise ValueError("LibreOffice laget ingen Word-fil av RTF-filen")
    shutil.move(str(laget), ut)
    return ut


def tekst(el, skille=" "):
    """Teksten i et element, med <br> som skille."""
    deler = [el.text or ""]
    for barn in el:
        if barn.tag == XHTML + "br":
            deler.append(skille)
        else:
            deler.append(tekst(barn, skille))
        deler.append(barn.tail or "")
    return "".join(deler)


def rens(t):
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()


def klasser(el):
    return (el.get("class") or "").split()


def epub_til_docx(sti: Path, ut: Path) -> Path:
    import docx
    from docx.enum.style import WD_STYLE_TYPE

    dok = docx.Document()
    stiler = {s.name for s in dok.styles}

    def avsnitt(stil, t):
        t = rens(t)
        if not t:
            return
        if stil not in stiler:
            dok.styles.add_style(stil, WD_STYLE_TYPE.PARAGRAPH)
            stiler.add(stil)
        dok.add_paragraph(t, style=stil)

    def tabell(el):
        rader = []
        for tr in el.iter(XHTML + "tr"):
            rader.append([rens(tekst(c)) for c in tr if c.tag in (XHTML + "td", XHTML + "th")])
        rader = [r for r in rader if any(r)]
        if not rader:
            return
        bredde = max(len(r) for r in rader)
        t = dok.add_table(rows=len(rader), cols=bredde)
        for i, r in enumerate(rader):
            for j, c in enumerate(r):
                t.cell(i, j).text = c

    def gå(el):
        navn = el.tag.replace(XHTML, "")
        k = klasser(el)
        if navn == "table":
            tabell(el)
            return
        if "K-PDFLINK" in k:
            return
        if navn in ("h1", "h2", "h3", "h4", "h5", "h6"):
            if "K-TIT-DEL" in k:
                m = re.match(r"\s*Del\s+(\d+)\s*\|\s*(.*)", tekst(el, "|"), re.S)
                if m:
                    avsnitt("del-nr", f"Del {ROMERTALL.get(m.group(1), m.group(1))}")
                    avsnitt("del-tittel", m.group(2))
                    return
            if "K-TIT-SESJON" in k:
                avsnitt("i-sesjon", (el.text or "").strip() or tekst(el, "|").split("|")[0])
                return
            if "K-TIT-UNDERTIT" in k and "FORSIDE" in k:
                avsnitt("i-undertit", tekst(el))
                return
            stil = next((OVERSKRIFTER[c] for c in k if c in OVERSKRIFTER), "Heading 3")
            t = tekst(el)
            if stil == "Heading 1":
                t = re.sub(r"^\s*\d+(\.\d+)*\s+", "", rens(t))  # nummereringen er automatisk i Word
            avsnitt(stil, t)
            return
        if navn == "p":
            if "K-TILRADNING" in k:
                # Forsiden i EPUB har ikke departementet for seg selv; det står i tilrådingen.
                avsnitt("i-dep", tekst(el))
                avsnitt("i-statsr.dato", tekst(el))
                return
            avsnitt("Normal", tekst(el))
            return
        if navn == "li":
            # Teksten i selve punktet, og underpunkter for seg
            egen = (el.text or "") + "".join(
                tekst(b) + (b.tail or "") for b in el if b.tag.replace(XHTML, "") not in ("ul", "ol", "p", "div"))
            ps = [b for b in el if b.tag == XHTML + "p"]
            avsnitt("List", egen + " ".join(tekst(p) for p in ps))
            for b in el:
                if b.tag.replace(XHTML, "") in ("ul", "ol", "div"):
                    gå(b)
            return
        for barn in el:
            gå(barn)

    with zipfile.ZipFile(sti) as z:
        container = ET.fromstring(z.read("META-INF/container.xml"))
        opf_sti = container.find(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile").get("full-path")
        opf = ET.fromstring(z.read(opf_sti))
        mappe = opf_sti.rsplit("/", 1)[0] + "/" if "/" in opf_sti else ""
        filer = {i.get("id"): i.get("href") for i in opf.iter(OPF + "item")}
        for ref in opf.iter(OPF + "itemref"):
            href = filer.get(ref.get("idref"), "")
            if not href.endswith((".xhtml", ".html", ".htm")) or ref.get("idref") in ("omslag", "fot"):
                continue
            rot = ET.fromstring(z.read(mappe + href))
            kropp = rot.find(XHTML + "body")
            if kropp is not None:
                gå(kropp)
    dok.save(str(ut))
    return ut


if __name__ == "__main__":
    print(til_docx(Path(sys.argv[1]), Path(sys.argv[2])))
