---
veileder: "Referansekatalogen for IT-standardar"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/standarder/peikarar-til-offentlege-ressursar-pa-nett/1492"
hentet: "2026-11-14"
---

# Referansekatalogen for IT-standardar Peikarar til offentlege ressursar på nett

Dette bruksområdet inneheld standardar som definerer struktur på peikarar (URI) til offentlege ressursar på nett. Med «offentlege ressursar på nett» meiner vi ressursar som offentlege verksemder forvaltar som er adresserte med HTTP eller HTTPS-protokollen.

Laga: 14. mai 2020

Sist endra: 21. april 2022

Anbefalingane som gjeld her er avgrensa til peikarar der responsen skal ha eit maskinlesbart format.

Med «maskinlesbart format» meiner vi eit format som er strukturert slik at programvare enkelt kan identifisere, kjenne att og trekke ut gitte opplysningar.

Det er **anbefalt**å utforme peikarar til offentlege ressursar på nett som IRI-ar (sjå Relevante standardar nedanfor), ei utviding av URI-standarden, og som gjer det mogleg å nytte eit utvida teiknsett. URI-standarden tillater berre teikn basert på ASCII, medan IRI-standarden tillater teikn basert på Universal Character Set (unicode/ISO 10646) som inkluderer kinesisk, japansk, kyrillisk osb.

I tillegg skal utforminga av IRI-ane følge dei 10 reglane definert i rapporten til EU sitt ISA-program (sjå under aktuelle standardar). Den norske profilen endrar den første regelen, ved berre å anbefale bruk av første og siste ledd i føreslått sti. Deretter overlet den til kvar verksemd å velje om ytterlegare ledd skal nyttast, men vert fleire ledd brukt skal dette gjerast i tråd med ISA-reglane. Det gir eit mønster som følger i første regel: http(s)://{domene}/{valgfritt(type)}/{valgfritt(concept)}/{objektidentifikator}

## Heimel

Innført 12.12.2016.

## Rettleiar

Det er ikkje laga rettleiarar enno.

- [Uniform Resource Identifier (URI)](https://www.rfc-editor.org/info/rfc3986)
- [Internationalized Resource Identifier (IRI)](https://www.rfc-editor.org/info/rfc3987)
- [Utformingen av IRI-er – 10 regler definert i EUs ISA-programs rapport (PDF)](http://joinup.ec.europa.eu/sites/default/files/document/2013-02/D7.1.3%20-%20Study%20on%20persistent%20URIs.pdf)
- [Hva maskinlesbarhet innebærer – EUs PSI direktivet artikkel 2.6](http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02003L0098-20130717&amp;from=EN)
- [Hva maskinlesbarhet innebærer i Norge – Stortinget Prop. 111 L (2015-2016) (PDF)](http://www.regjeringen.no/contentassets/1f000ec218004c9e92c3b4ae452160f3/nn-no/pdfs/prp201520160111000dddpdfs.pdf)
