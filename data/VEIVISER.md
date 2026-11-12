# Data og statistikk – veiviser

Denne mappen er en katalog over hvor tall og statistikk finnes, for arbeid, velferd og integrering og for barnehage, skole, høyere utdanning, fagskole, forskning og utdanningsstøtte, og hvilken tabell som svarer på hvilket spørsmål. Den inneholder ikke selve tallene. Tall hentes fra kilden, så de er oppdatert.

Start med `data/sporsmal.md` når spørsmålet er stilt i hverdagsspråk. Den kobler vanlige spørsmål til riktig kilde og tabell.

## Regler

1. **Hent tallene fra kilden, ikke fra katalogen.** Katalogen sier hvor du skal lete. Oppgi tabell, periode og når tabellen sist ble oppdatert.
2. **Sjekk om tallet allerede står i et autoritativt dokument i basen** før du leter andre steder. Satser og beløp i folketrygden fastsettes for eksempel i budsjettvedtaket (se `budsjett/VEIVISER.md`), og satser for utdanningsstøtte i forskriften om tildeling av utdanningsstøtte (se `regelverk/utdanningsstotteloven/VEIVISER.md`).
3. **Skill mellom kildene.** Samme begrep kan ha ulik definisjon hos ulike kilder. Studenttall fra SSB og fra DBH er for eksempel ikke talt på samme måte. Si hvilken kilde tallet kommer fra.
4. **Katalogen er kontrollert mot SSB 2026-10-17 (utdanning 2026-11-11).** Tabeller kan bli avsluttet eller erstattet. Finner du ikke tabellen, søk på nytt.

## Slik svarer du: kort svar og kvalitetssikringsversjon

Brukere av basen er også ledere og kommunikasjonsmedarbeidere som ikke selv kan kvalitetssikre tallene. Svar derfor i to lag.

**Standardsvar (kort).** Konklusjonen i 2–4 setninger med tallet, perioden og hva det måler. Kilde, eier og periode står i selve setningen («Nav, sykefraværsstatistikken, 2. kvartal 2026»), slik at svaret kan videresendes uten vedlegg. Tall du har regnet ut selv, og forbehold som kan gi et feil bilde, står også her. Nevn brudd i serien og andre avgrensninger bare når de berører perioden eller tallene i svaret. Brudd som ligger utenfor perioden det spørres om, hører hjemme i kvalitetssikringsversjonen om de skal med. Avslutt med én linje om at en kvalitetssikringsversjon finnes.

**Kvalitetssikringsversjon (på forespørsel).** Samme tall som standardsvaret, i denne rekkefølgen:
1. Svaret med nummererte kildehenvisninger [1], [2].
2. Kilder: eier, tabell med tittel og kode, ark og rad/kolonne tallet står i, lenke til eierens side, når tabellen er publisert og når den ble hentet (se `data/nav/indeks.tsv`).
3. Utregninger: formel og kildetall for alt du har regnet ut. Tall som eieren selv oppgir er merket «fra kilden».
4. Forbehold: brudd, avgrensninger og begreper som lett forveksles.
5. Til kvalitetssikrer: hva som er kontrollert maskinelt (konvertering tall for tall) og hva et menneske må vurdere (om tallet svarer på det som ble spurt om).

**Regler for begge.** Ikke slå sammen eller sammenlign tall fra ulike kilder uten å si at definisjonene kan avvike. Si «ikke dekket» når tallet ikke finnes i katalogen eller hos kilden. Tall hentes fra kilden hos eieren, som eier kvaliteten, og svaret viser alltid til eieren. Nevner du at en annen kilde har et annet tall for samme begrep (for eksempel AKU hos SSB og registrerte helt ledige hos Nav), vis tallet eller tilby det i samme setning.

## Kilder

| Kilde | Fil | Status |
|---|---|---|
| Statistisk sentralbyrå (SSB) | `data/ssb.md` | Dekket for hovedtemaene, også barnehage, grunnskole, videregående, fagskole, universiteter og høyskoler, utdanningsnivå og FoU. Hentes med SSB-tilkoblingen, se arbeidsmåte og filtersyntaks i `data/ssb-bruk.md`. |
| Nav | `data/nav.md` | Sykefravær (alle kvartal i samme fil, kolonnen `kvartal`), dagpenger, AAP, uføretrygd, nedsatt arbeidsevne, alderspensjon, helt ledige, ledige stillinger, tiltaksdeltakere og arbeidsindikator lagt inn som TSV. AFP i privat sektor, gjenlevendeytelser, krigspensjon, supplerende stønad, kontantstøtte, utbetalinger, utenforskap og trygdesvindel er lagt inn. Barnetrygd, foreldrepenger og sosialhjelp finnes ikke som xlsx hos Nav. Navs pressemeldinger om statistikken ligger som tekst fra januar 2024. |
| Eurostat | `data/eurostat.md` | Sammenligning mellom Norge, Norden og EU på arbeidsmarked, fattigdom, offentlige utgifter, utdanningsnivå, tidlig skoleslutt, voksnes deltakelse i opplæring, utgifter til utdanning, elever per lærer og FoU. Fast pakke som TSV, oppdateres hver mandag. |
| OECD | `data/oecd.md` | Sammenligning med andre land på arbeidsmarkedspolitikk, ytelsesnivå, aktivitetskrav, stillingsvern, pensjon, sosiale utgifter, skatt på arbeid og organisering, og utdanning (Education at a Glance: utgifter, klassestørrelse, utdanningsnivå, sysselsetting etter utdanning), også med USA, Storbritannia og OECD-snittet. Fast pakke som TSV, oppdateres hver mandag. |
| Grunnbeløpet i folketrygden (G), Nav | `data/grunnbelop.tsv` | G for alle reguleringer fra 1967, med gjennomsnittlig G per år og omregningsfaktor. Hentes fra nav.no hver mandag og kontrolleres mot grunnbeløpsforskriften i regelverksbasen. Brukes til å regne beløp om til G, også i analyser i microdata.no. |
| microdata.no (SSB og Sikt) | `data/microdata.md` | Variabelkatalog og brukerveiledning for egne analyser av registerdata. Brukeren kjører analysen selv. Claude foreslår analyse og skriptutkast. Kopi oppdateres hver mandag. Utdanningsvariablene begynner på `NUDB_` (Nasjonal utdanningsdatabase) og `LAANEKASSEN_`. |
| Utdanningsdirektoratet (Udir) | `data/udir.md` | Elevundersøkelsen hentes fra Udirs åpne API. Karakterer, nasjonale prøver, fravær, søkere og førsteinntak er ikke tilgjengelige for Claude, og brukeren vises til Udirs sider. Bruk SSB der SSB har tallet. |
| DBH (HK-dir) | `data/dbh.md` | Studenter, søknader, kandidater, gjennomføring, studiepoeng, ansatte og økonomi per universitet, høyskole og fagskole. Hentes direkte fra DBHs åpne API med kodeverktøyet. Krever at `dbh.hkdir.no` er tillatt i brukerens innstillinger. |
| Lånekassen | `data/lanekassen.md` | Statistikksidene er Power BI og kan ikke leses av Claude. Nøkkeltall står i årsrapporten «Utdanningsstøtten». Krever at `lanekassen.no` er tillatt i brukerens innstillinger. |
| Samordna opptak (HK-dir) | – | Ikke hentet. Søkertall (etter søknadsfristen i april), tilbudstall (etter hovedopptaket i juli), poenggrenser og sluttstatistikker publiseres på https://www.samordnaopptak.no/om/tall-og-statistikk/. Gi lenken og oppgi Samordna opptak som kilde. Siden kan bare leses når `www.samordnaopptak.no` er tillatt i brukerens innstillinger. DBH har bare søknadsalternativer, ikke søkere som personer, se `data/dbh.md`. |

## Åpent

- **Nav:** Utvalgte tabeller er lagt inn (se `data/nav.md`). Nav gir tall som xlsx-filer som Claude ikke kan laste ned, så flere tabeller må legges inn av saksbehandlerne. Nav-filer legges i `data/innboks/` og konverteres automatisk. Det mangler en vurdering av hvilke Nav-tabeller som brukes mest.
- **Andre kilder** (IMDi, Arbeidstilsynet, Statens pensjonskasse, Fafo, NIFU m.fl.) er ikke vurdert.
- **Udir:** be om flere tabeller i det åpne API-et (karakterer, nasjonale prøver, fravær, elevtall).
- **OECD:** lærerlønn og undervisningstid krever at `verktoy/oecd_hent.py` kan lese tabeller uten tidsdimensjon.
