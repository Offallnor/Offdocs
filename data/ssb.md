# SSB – hvilken tabell svarer på hva

Tabellene er kontrollert mot SSB 2026-10-17 (utdanning og forskning 2026-11-11) (id, tittel, periode og oppdateringsdato er lest fra SSBs API). Hent data med SSB-tilkoblingen (arbeidsmåte, filtersyntaks og feilsøking: `data/ssb-bruk.md`): søk med `ssb_search`, les variablene med `ssb_table_metadata`, hent med `ssb_get_data`, og filtrer alltid på tid.

**Feil i SSB-tilkoblingen (kontrollert 2026-11-11):** Spør du om flere perioder og flere statistikkvariabler (`ContentsCode`, for eksempel både prosent og personer) i samme kall med standardformatet json-stat2, kan rader falle bort og tall få feil periode, uten feilmelding. Eksempel: tabell 14867 med 2014-2020 og 2019-2025 ga bare 2014-2020, og elevtallet for 2019-2025 ble merket 2014-2020. Bruk `format: "csv"`, eller hent én `ContentsCode` per kall.

## Søketips (kontrollert)

- Korte søkeord virker bra: `sysselsatte`, `title:Konsumprisindeks`, `title:Innvandrere`. Lange setninger og lange `title:`-uttrykk ga ingen treff.
- Hvert søk gir mange tabeller med overlappende innhold. Velg etter periode, hyppighet og oppdeling, ikke bare etter tittelen.
- «(K)» i tittelen betyr kommunefordelt, «(F)» fylkesfordelt, «(B)» bydelsfordelt.
- Mange tabeller fra 2015 er KOSTRA-tabeller (kommunenes og fylkeskommunenes rapportering). De har nøkkeltall og utgifter per kommune.
- Skoleår og studieår vises som intervall, for eksempel «2024-2025».
- For utdanning gir `title:` med ett eller to ord best treff: `title:barnehager`, `title:videregående`, `title:doktorgrader`.

## Arbeidsmarked

| Spørsmål | Tabell | Periode | Merknad |
|---|---|---|---|
| Arbeidsstyrke, sysselsatte og arbeidsledige, månedlig, 15–74 år | **13760** | 2006M01–2026M08 | Oppdelt på kjønn og tre aldersgrupper. Brudd- og sesongjusterte tall. |
| Samme, kvartalsvis | 14483 | 2009K1–2026K2 | Etter arbeidsstyrkestatus, kjønn og alder. |
| Hvor mange går mellom sysselsatt, arbeidsledig og utenfor | 11433 | 2006K2–2026K2 | Sesongjusterte strømmer. |
| Innvandreres arbeidsstyrkestatus | 14714 | 2021K1–2026K2 | Etter landbakgrunn, kjønn og alder. |

**Slik leser du 13760.** Statistikkvariabelen `ArbledProsArbstyrk` gir arbeidsledige i prosent av arbeidsstyrken. Velg `Justering`: `S` er sesongjustert, `T` trend, `IS` ikke sesongjustert, `3MGG` sesongjustert tremåneders glidende gjennomsnitt. **Siste måned mangler for 3MGG.** Eksempel hentet 2026-10-17: sesongjustert ledighet for begge kjønn, 15–74 år, 2026M08 var 4,5 prosent, mens 3MGG for samme måned var tom.

## Lønn

| Spørsmål | Tabell | Periode |
|---|---|---|
| Lønn og sysselsetting etter næring, årlig, lang serie | 09174 | 1970–2025 |
| Lønn og sysselsetting etter næring, kvartalsvis | 09175 | 1995K1–2026K2 |
| Lønnstakere, jobber og lønn etter næring (88 grupper) | 12314 | 2016K1–2026K2 |
| Etter kjønn og alder, arbeidssted | 11652 | 2016K1–2026K2 |
| Etter innvandringskategori | 12315 | 2016K1–2026K2 |

## Sykefravær

Kvartalstall for lønnstakere. Tittelen sier om tabellen viser «egen- og/eller legemeldt» eller bare «legemeldt». De er ikke samme tall.

| Spørsmål | Tabell | Omfang |
|---|---|---|
| Etter type sykefravær og kjønn, sesong- og influensajustert | 12439 | 2000K2–2026K2 |
| Etter næring (17 grupper) og kjønn | 12440 | 2000K2–2026K2 |
| Årlig, etter næring og kjønn | 12441 | 2001–2025 |
| Etter varighet | 12946 | 2015K1–2026K2 |
| Legemeldt, etter fylke, næring og kjønn | 12447 | 2008K1–2026K2 |
| Legemeldt, etter bostedskommune | 12451 | 2000K2–2026K2 |
| Legemeldt og lønn, etter utdanning og alder | 13333 | 2015K1–2026K2 |

## Priser

| Spørsmål | Tabell | Merknad |
|---|---|---|
| KPI etter vare- og tjenestegruppe, månedlig | 14700 | 2000M01–2026M09. Basisår 2025=100. |
| KPI sesongjustert og KPI-JAE | 14708 | 1985M01–2026M09 |
| KPI, lang historisk serie | 14710 (månedlig), 14709 (årlig) | Fra 1920. |
| KPI, årlig | 14701 | 2000–2025 |

Basisåret er endret til 2025=100. Eldre tall som er oppgitt med annet basisår, kan ikke sammenlignes uten omregning.

## Innvandring

| Spørsmål | Tabell | Periode |
|---|---|---|
| Innvandrere etter kjønn og landbakgrunn | 05184 | 1970–2026 |
| Innvandrere etter landbakgrunn og botid (fylke) | 10598 | 2005–2026 |
| Utdanningsnivå for innvandrere | 09623 | 2004–2025 |

## Befolkning

| Spørsmål | Tabell | Periode |
|---|---|---|
| Endringer i befolkningen i løpet av året | 05803 | 1735–2026 |
| Alders- og kjønnsfordeling | 10211 (enkeltalder), 05810 (aldersgrupper) | 1845/1846–2026 |
| Etter kommunestørrelse, alder og kjønn | 12871 | 2017–2026 |
| Grunnkrets | 04317 | 1999–2026 |

## Sosialhjelp

| Spørsmål | Tabell | Periode |
|---|---|---|
| Stønadssatser for sosialhjelp og vedtakstidspunkt (kommune) | 12131 | 2015–2025 |
| Stønadstilfeller etter alder (fylke) | 08900 | 2010–2025 |
| Brutto utbetalt sosialhjelp etter stønadens art og kommunestørrelse | 05973 | 1997–2025 |
| Mottakere etter alder og antall kommuner | 05082 | 1997–2025 |

## Trygdeytelser

SSB har få tabeller om mottakere av arbeidsavklaringspenger og uføretrygd, og flere av dem er gamle. Antall mottakere og utbetalinger per ytelse hører til Navs statistikk, som ikke er dekket ennå (se `data/VEIVISER.md`).

| Tabell | Innhold | Periode |
|---|---|---|
| 13080 | Måneder som mottaker av arbeidsavklaringspenger og sysselsatt lønnstaker | 2018–2025 |
| 11867 | Uføretrygdede og lønnstakere, etter måneder som sysselsatt lønnstaker | 2015–2025 |
| 11079, 11108–11113 | Eldre tabeller om AAP og uføre, oppdatert sist i 2016 | 2006–2014 |

## Barnehage

| Spørsmål | Tabell | Periode |
|---|---|---|
| Nøkkeltall per kommune: andel barn i barnehage, barn per årsverk (bemanning), andel barnehagelærere, spesialpedagogisk hjelp, utgifter | **13502** | 2015–2025 |
| Barn i barnehage etter alder, oppholdstid og eierforhold | 09169 | 1999–2025 |
| Samme, nyere inndeling | 14522 | 2015–2025 |
| Antall barnehager etter eierforhold | 09220 | 1987–2025 |
| Årsverk etter stillingstype og eierforhold | 09339 | 2000–2025 |
| Minoritetsspråklige barn i barnehage, 1–5 år | 12272 | 2015–2025 |
| Barn med styrket tilbud | 12376 | 2015–2025 |
| Utgifter, nøkkeltall | 12379 | 2015–2025 |

## Grunnskole og SFO

| Spørsmål | Tabell | Periode |
|---|---|---|
| Nøkkeltall per kommune | **12255** | 2015–2025 |
| Antall kommunale skoler og elever | 11971 | 2015–2025 |
| Elever etter målform (nynorsk/bokmål) | 03743 | 2002–2025 |
| Skolestørrelse | 09537 | 2005–2025 |
| Årstimer til undervisning | 11974 | 2015–2025 |
| Lærere etter kompetanse | 12919 (kommune), 12993 (fylke, med stillingsprosent) | 2015–2025 |
| Lærere etter kjønn og alder | 12282 | 2015–2025 |
| Ansatte etter yrke | 12065 | 2015–2025 |
| Barn i SFO | 11975 | 2015–2025 |
| Hva elevene gjør etter grunnskolen | 13348 (fylke), 13349 (etter foreldrenes utdanning) | 2018–2024 |

Karakterer, nasjonale prøver, Elevundersøkelsen og elevtall per skole er Utdanningsdirektoratets statistikk, ikke SSBs. Se `data/udir.md`.

## Videregående opplæring

| Spørsmål | Tabell | Periode |
|---|---|---|
| Hvor mange fullfører og består (seksårsgjennomføring) | **14863–14870** | startkull 2014 til 2019 |
| – etter alder | 14863 | |
| – etter todelt utdanningsprogram (studieforberedende/yrkesfag) og kjønn | 14867 | |
| – etter detaljert utdanningsprogram | 14868 | |
| – etter foreldrenes utdanningsnivå | 14869, 14870 | |
| Gjennomføring blant lærlinger | 13014 | 2006–2012 til 2019–2025 |
| Elever, lærlinger og lærekandidater etter kjønn, alder og skoleslag | 08947 | 2006–2025 |
| – etter utdanningsprogram (fylke) | 09378 | 2010–2025 |
| – etter innvandringskategori | 13159 | 2012–2025 |
| Lærlinger etter utdanningsprogram | 05364 | 2003–2025 |
| Fullførte utdanninger etter resultat | 09336 | 2010-2011 til 2024-2025 |
| Nøkkeltall per fylke | 12609 | 2015–2025 |
| Søkere | 12199 | 2015–2025 |
| Oppfølgingstjenesten | 11966 | 2015–2025 |
| Utgifter i fylkeskommunen | 11902, 12188 | 2015–2025 |

**Slik leser du gjennomføringstabellene.** Et kull følges i seks år fra start. Intervallet «2019-2025» er elevene som startet i videregående høsten 2019, så det nyeste tallet er flere år gammelt når det publiseres. Si hvilket startkull tallet gjelder. Variabelen `FullforingVGO` har sju verdier. «Fullført med studie- eller yrkeskompetanse» er summen av normert tid (`1a`) og mer enn normert tid (`2a`). Planlagt grunnkompetanse (`4b`) telles ofte med i «fullført og bestått», så si hva du har tatt med. I 14867 er regionene den gamle fylkesinndelingen (før 2020) pluss fylker som ikke ble endret (kontrollert 2026-11-11).

## Fagskole (høyere yrkesfaglig utdanning)

| Spørsmål | Tabell | Periode |
|---|---|---|
| Studenter etter fagfelt, eierforhold og varighet | **14259** | 2011–2025 |
| Studenter etter alder og kjønn | 10864 | 2013–2025 |
| Studenter etter innvandringskategori | 10863 | 2013–2025 |
| Fullførte fagskoleutdanninger | 11636 | 2015-2016 til 2024-2025 |
| Sysselsatt samme høst etter fullført utdanning | 13675 | 2018-2019 til 2024-2025 |

## Universiteter og høyskoler

| Spørsmål | Tabell | Periode |
|---|---|---|
| Studenter etter fagfelt og kjønn | **05576** | 2000–2025 |
| Studenter etter alder | 14217 | 2018–2025 |
| Fullførte utdanninger etter nivå og fagfelt | **03824** | 1993-1994 til 2024-2025 |
| – etter nivå og alder | 07997 | 1998-1999 til 2024-2025 |
| – etter innvandringskategori | 08916 | 2000-2001 til 2024-2025 |
| – etter studium | 14850 | 2024-2025 |
| Avlagte doktorgrader etter lærested | 13521 | 1980–2025 |
| – etter fagområde | 13522, 13523 | 1990–2025 |
| Gjennomføring i doktorgradsutdanningen | 14956 | 2019–2024 til 2020–2025 |

Tall per institusjon, studiepoeng, opptak og ansatte i UH-sektoren er i DBH (HK-dir). Se `data/dbh.md`.

## Befolkningens utdanningsnivå

| Spørsmål | Tabell | Periode |
|---|---|---|
| Utdanningsnivå etter fylke, alder og kjønn (16 år og over) | **08921** | 1980–2025 |
| Utdanningsnivå etter foreldrenes utdanningsnivå | 12935 | 2018–2025 |
| Sysselsatte etter utdanningsnivå og fagfelt | 11930 | 2008–2025 |
| Ungdom utenfor arbeid og utdanning (NEET) etter utdanningsnivå | 12423 | 2008–2025 |
| Deltakelse i utdanning og opplæring blant voksne | 06699 | 2007–2022 |
| Lærerutdannede og hvor de jobber | 14577 | 2021–2025 |

## Forskning og utvikling (FoU)

| Spørsmål | Tabell | Periode |
|---|---|---|
| FoU-utgifter, -årsverk og -personale etter sektor | **11010** | 1970–2025 |
| Statlige bevilgninger til FoU etter departement | 13662 | 2000–2026 |
| – etter formål | 13663 | 2000–2026 |
| – etter mottaker | 13664 | 2000–2026 |
| Grunnforskning, anvendt forskning og utviklingsarbeid | 13870 | 1991–2023 |
| FoU-årsverk i UH-sektoren etter lærested og fagområde | 13911 | 2011–2024 |
| FoU-årsverk i instituttsektoren | 13519 | 2001–2025 |
| FoU-personale etter kjønn | 13520 | 1970–2025 |

FoU-statistikken lages av SSB (næringslivet) og NIFU (UH- og instituttsektoren). Tallene for UH- og instituttsektoren er NIFUs, selv om de ligger hos SSB.

## Det vi ikke fant

- Ungdom utenfor opplæring og arbeid: søket ga ingen relevant tabell. Prøv andre søkeord eller spør SSB.
- Hovedtabell for registerbasert sysselsetting: søk på tittelen ga ingen treff. Bruk 13760 for månedlige tall og 14483 for kvartalstall.
- Elevtall per skole, karakterer og nasjonale prøver: ikke SSB-tabeller.
- Studielån og stipend: ikke SSB-tabeller. Lånekassen publiserer selv.
