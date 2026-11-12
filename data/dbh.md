# DBH – statistikk om universiteter, høyskoler og fagskoler

DBH (Database for statistikk om høyere utdanning) og DBH-HYU (fagskoler) driftes av HK-dir. API-et er åpent uten innlogging. Spørringene og fellene under er kontrollert mot API-et 2026-11-11. Hent tallene direkte fra API-et når brukeren spør. Tallene ligger ikke i basen.

## Før du henter

- **Krever kodeverktøyet og at domenet `dbh.hkdir.no` er tillatt** i brukerens innstillinger for kodeverktøyet (listen over tillatte domener). Får du nettverksfeil eller 403, si det til brukeren og be dem legge til domenet. Svar ikke fra hukommelsen.
- **Vilkår.** Oppgi «DBH, HK-dir» og tabellnummeret som kilde. HK-dir krever at tall generert med KI merkes som KI-generert, så si i svaret at tallene er hentet og satt sammen av Claude.
- **Små tall er skjermet.** I tabeller merket `Gdpr=1` i tabell 001 vises ikke tall under 3. Summer kan derfor avvike litt fra DBHs egne rapporter.

## Slik finner du tabellen

1. **Les innholdsfortegnelsen** (tabell 001) med en vanlig GET. Den lister alle tabellene med emne, nummer, navn, om tallene er skjermet (`Gdpr`), om tabellen kan summeres (`Math=1`) og alle variablene:
   ```
   curl -s "https://dbh.hkdir.no/api/Tabeller/bulk-csv?rptNr=001"
   ```
2. **Variabelbeskrivelser** står i tabell 002 (samme adresse med `rptNr=002`).
3. **Definisjoner og brudd** står i DBHs tabelldokumentasjon, https://dbh.hkdir.no/datainnhold/tabell-dokumentasjon/NNN (for eksempel /123). Siden lastes med JavaScript, så den kan bare leses i en nettleser. Kan du ikke lese den, gi brukeren lenken når en definisjon betyr noe for svaret.
4. **Endringer i API-et** (nye felt, nye grenser) står i tabell 916 (`rptNr=916`).

## Slik henter du

Tabeller med `Math=1` hentes med POST og `groupBy`. Lister (`Math=0`) hentes med `variabler` i stedet for `groupBy`, for eksempel `"variabler":["*"]`, eller hele som CSV (se under). Sjekk `Math` i tabell 001 før du henter: eksempelet under virker ikke for en listetabell som 902. Minst ett filter er påkrevd.

```
curl -s -X POST https://dbh.hkdir.no/api/Tabeller/hentJSONTabellData \
  -H "Content-Type: application/json" \
  -d '{"tabell_id":123,"api_versjon":1,"statuslinje":"N","kodetekst":"J","desimal_separator":".",
       "groupBy":["Årstall","Semester"],"sortBy":["Årstall","Semester"],
       "filter":[{"variabel":"Årstall","selection":{"filter":"top","values":["3"]}}]}'
```

- `"kodetekst":"J"` gir navn ved siden av koder (for eksempel `Institusjonsnavn`, `Nivånavn`, `Semesternavn`).
- Filtertyper: `item` (liste med verdier), `top` (de siste n årene), `between` (fra–til), `all` (`["*"]`), `like`, `lessthan`, `greaterthan`. Alle unntatt `item` kan ha `exclude`.
- `sortBy` må være en delmengde av `groupBy`.
- Tallene kommer som regel som tekst. Gjør dem om før du regner.
- Listetabeller uten skjerming (`Bulk tabell=1`) kan hentes hele som CSV med `bulk-csv?rptNr=NNN`, for eksempel tabell 211 (institusjoner) og 902 (økonomi).
- Kodetabeller (for eksempel 469) er ikke bulktabeller. Hent dem med POST og `"variabler":["*"]`.
- Tabellene 60, 208, 308, 379 og 571 gir høyst seks år per spørring.

## Kjente feller

- **Semester.** Studenttall registreres for vår (`Semester` 1) og høst (3). Summerer du over et år, telles de fleste studentene to ganger. Bruk høstsemesteret for antall studenter i et år, og si det. Eksempel: tabell 123 gir 325 644 registrerte studenter høsten 2026, mens summen av vår og høst 2026 er 623 193.
- **Inneværende år er ufullstendig** i tabeller som teller hele året, som ferdige kandidater (104) og doktorgrader (101). Sammenlign hele år.
- **Søknader er ikke søkere.** Tabell 379 teller søknadsalternativer (hver søker har flere), tilbud, aksept og oppmøte. Antall personer som søkte, står ikke der, og finnes ikke i DBH. Samordna opptak publiserer søkertall (personer) for opptaket gjennom Samordna opptak. Si det, og gi ikke søknadsalternativer som søkertall.
- **Opptakstype.** I søkertabellene skiller `Opptakstype` mellom Samordna opptak (`N`) og lokalt opptak (`L`). Si hvilket opptak tallet gjelder, eller ta med begge.
- **Årsverk, ikke personer.** Tabell 225 gir årsverk. Antall ansatte (hodetelling) står i tabell 222.
- **Økonomi i tusen kroner.** Beløpene i tabell 902 er i tusen kroner. Tallene kommer fra institusjonenes regnskapsrapportering, og DBH definerer ikke «Statstilskudd» nærmere (tabelldokumentasjonen for 902 og variabelbeskrivelsen i tabell 002). Tallet ligger nær, men ikke på, rammeløyvinga over kap. 260 i Prop. 1 S. For 2025 er DBH-tallet høyere for nesten alle statlige institusjoner, med opptil 3 prosent (OsloMet 92 mill. kroner, NTNU 42 mill. kroner), mens de private stort sett er like. Si at tallet er statstilskuddet slik institusjonen har rapportert det til DBH. Gjelder spørsmålet rammeløyvinga fra Kunnskapsdepartementet, bruk vedlegget i Prop. 1 S. Det siste året kan endres. Bevilgningen per institusjon står i tabellen i Prop. 1 S, se budsjettdelen.
- **Studentkategori og doktorgrad.** Tabell 123 har to studentkategorier: `S` (studenter med studierett) og `P` (personer uten studierett). Si hvilke kategorier som er med. Personer i doktorgradsprogrammer er ikke med i tabell 123. Bruk tabell 101 for doktorgrader. Kilde: DBHs tabelldokumentasjon for tabell 123, lest 2026-11-11.
- **Institusjoner slås sammen.** Tabell 211 viser hvilken institusjon en nedlagt eller sammenslått institusjon nå er en del av (`Institusjonskode (sammenslått)`). Bruk den når du sammenligner over tid.
- **SSB og DBH teller ulikt.** Studenttall fra SSB (se `data/ssb.md`) og fra DBH har ulik telledato og avgrensning. Si hvilken kilde du bruker, og bland dem ikke.

## De vanligste tabellene

| Spørsmål | Tabell | Merknad |
|---|---|---|
| Hvor mange studenter (per institusjon, nivå, studieprogram)? | **123** Registrerte studenter | Filtrer på `Semester` 3 (høst). `Nivåkode` gir årsstudium, bachelor, master m.m. |
| Hvor mange nye studenter? | 110 Nye studenter | |
| Hvor mange søknader, tilbud og oppmøtte? | 379 Søkertall og møtte | Søknadsalternativer, ikke personer. |
| Hvor mange studieplasser, og hva var poenggrensen? | 370 Studieplasser | |
| Opptakspoeng | 571 Gjennomsnittlige opptakspoeng for søkere | |
| Hvor mange fullførte en grad? | **104** Ferdige kandidater | Hele år. |
| Hvor mange fullfører på normert tid, og hvor mange faller fra? | 705 (sektor), 704 (institusjon), 706–707 (studium og studieprogram) | Les tabelldokumentasjonen for kolonnene `Fullført normert1/2`. |
| Studiepoeng | 900 Studiepoeng | |
| Karakterer | 308 Karakterer | |
| Utenlandske studenter og utveksling | 135, 142 | |
| Doktorgrader | 101 Avlagte doktorgrader, 115 Personer i doktorgradsprogrammer | |
| Ansatte i UH-sektoren | 225 (årsverk), 222 (hodetelling), 219 (alder) | |
| Inntekter, statstilskudd og eksterne midler per institusjon | 902 Økonomiske nøkkeltall | Tusen kroner. |
| Kandidater i finansieringssystemet | 907, 908 | |
| Vitenskapelig publisering | 373 | |
| Fagskolestudenter | 947 Fagskolestudenter – aktive studenter | Feltet heter `Antall studenter`, ikke `Antall totalt`. |
| Søknader til fagskoler | 555 | |
| Videreutdanning for lærere | 543 (barnehage), 544 (grunnskole) | |
| Institusjoner med type og eier | 211 Institusjon | Bulk-CSV. |
