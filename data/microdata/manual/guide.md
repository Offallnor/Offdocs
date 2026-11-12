<!-- kilde: https://microdata.no/manual/guide/ -->
<!-- Brukerveiledningen for microdata.no (SSB og Sikt), hentet automatisk. -->

# En enkel innføring i microdata.no

For å komme i gang med microdata.no, vil vi vise hvordan man lager en typisk statistikk gjennom noen av de mest grunnleggende kommandoene i verktøyet. Statistikkeksempelet vårt viser gjennomsnittsinntekten i Oslo, Bergen og Trondheim, og kjønnsfordelingen av gjennomsnittsinntekten i disse kommunene.

***Gjennomsnittsinntekt i Oslo, Bergen og Trondheim***

[bilde](https://microdata.no/manual/assets/images/image164-9516dcfa2a3e0fb9aa403d12a8416357.png)

***Gjennomsnittsinntekt i Oslo fordelt på kjønn***

[bilde](https://microdata.no/manual/assets/images/image165-20ef4de591c7c3ef43f4a461c51d5a14.png)

***Gjennomsnittsinntekt i Bergen fordelt på kjønn***

[bilde](https://microdata.no/manual/assets/images/image166-60ca1b192cdd3640a69f5371faecb737.png)

***Gjennomsnittsinntekt i Trondheim fordelt på kjønn***

[bilde](https://microdata.no/manual/assets/images/image167-4ae4a39b1cd2e7b4844e59c8cd901cbe.png)

Nedenfor vil vi punkt for punkt gå gjennom alle trinnene som trengs for å kunne lage en slik statistikk.

### Opprette kobling til databank

```
 require no.ssb.fdb:38 as db

```

Den første kommandoen som brukes er `require`, som kobler opp til SSBs databank, der alle variablene ligger. Den refereres til som `db` i skriptet og er nødvendig for å få tilgang til variabler for å videre bruke disse i et datasett.

### Databank-versjon

Det siste tallet i `no.ssb.fdb:38` står for versjonsnummeret. Siste versjon inneholder nyeste oppdateringer av variabler og årganger. Man får beskjed dersom man bruker en eldre versjon enn den nyeste:

[bilde](data:image/png;base64,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)

### Oppretting av datasett

```
 create-dataset persondata

```

Denne kommandoen oppretter et nytt, tomt datasett gitt det valgfrie navnet `persondata`. Man får også opp dette datasettet på høyresiden av vinduet etter kommandoen er kjørt. For å fylle datasettet med innhold, kan du importere variabler fra databanken ved hjelp av `import`-kommandoen. Dette gjør det mulig å hente inn ønskede data til ditt nye datasett.

[bilde](https://microdata.no/manual/assets/images/image168-e436e2b8079a920036809eb3545409ba.png)

### Første importerte variabel

```
 import db/INNTEKT_WLONN 2022-12-31 as lønn22

```

Denne kommandoen importerer variabelen `INNTEKT_WLONN` fra databasen per 31. desember 2022 og gir den navnet `lønn22`, som representerer individers lønnsinntekt for 2022. Den dukker også opp i datasettet på høyresiden når kommandoen er kjørt.

[bilde](https://microdata.no/manual/assets/images/image169-f0ce51d8d520793abfee83c1b22d5bf3.png)

Dette er den første variabelen som blir importert og bestemmer derfor populasjonen i datasettet. Datasettet inneholder de som hadde lønnsinntekter i 2022. Denne variabelen har temporalitetstypen akkumulert, som betyr at datoene representerer årsinntekt per siste dag i året (31.12.xxxx). Man kan velge hvilken som helst dato innenfor det aktuelle året dersom man har akkumulerte verdier målt over et år. Verdiene man får ut vil bli de samme (akkumulert årsverdi).

Slik ser datasettet ut etter at første variabel er importert (illustrasjon):

| **personID** | **lønn22** |
|---|---|
| 1 | 450 000 |
| 2 | 320 000 |
| 3 | 150 000 |
| 4 | 700 000 |

### Andre importerte variabel

```
 import db/BEFOLKNING_KOMMNR_FORMELL 2023-01-01 as bostedskommune

```

Etter lønnsvariabelen `lønn22`, importeres en variabel som angir individers bostedskommune. Denne kommandoen importerer variabelen `BEFOLKNING_KOMMNR_FORMELL` per 1. januar 2023. Den inneholder alle som er bosatte per 1.1.2023. Denne variabelen har temporalitetstype tverrsnitt, som betyr at alle som er registrert bosatt i en kommune i folkeregisteret per 1.1.xxxx, inkluderes. Variabler med denne typen temporalitet vil typisk måles over faste gjentakende datoer, i dette tilfellet 1/1 hvert år. Om man velger en annen dato, vil man ikke få ut noen opplysninger.

[bilde](https://microdata.no/manual/assets/images/image170-f2d6d0af6ec3374e4f49e25e2c223514.png)

### Hvordan import av nye variabler påvirker eksisterende datasett

Når du importerer nye variabler i datasettet ditt, blir alle rader fra det eksisterende datasettet beholdt (alle med verdi på `lønn22`, den første importerte variabelen). De nye variablene legges til basert på matchende rader mellom det eksisterende datasettet og de nye dataene. For eksempel, hvis du først har importert variabelen `lønn22` (lønn for 2022), og deretter importerer variabelen `bostedskommune`, vil informasjon om bostedskommune bli lagt til for alle personer som allerede har en verdi for `lønn22`. Denne metoden kalles en **left join**. Slik ser datasettet ut etter at `bostedskommune` er importert (illustrasjon):

| **personID** | **lønn22** | **bostedskommune** |
|---|---|---|
| 1 | 450 000 | "0301" (Oslo) |
| 2 | 320 000 | "4601" (Bergen) |
| 3 | 150 000 | "0301" (Oslo) |
| 4 | 700 000 | "5001" (Trondheim) |

### Filtrering

Siden eksempelet vårt viser gjennomsnittlig inntektsfordeling i Oslo, Bergen og Trondheim, kan man filtrere datasettet slik at man kun beholder disse kommunene i datasettet. Da bruker man kommandoen `keep if`, og spesifiserer tallkodene for de tre kommunene separert med `|` (eller). Tallkodene finnes i variabelbeskrivelsen. Variabelen er alfanumerisk, og man må derfor bruke anførselstegn når man angir verdien.

Det er også mulig å bruke en filtrering direkte i statistikkkommandoen ved å legge til en if-betingelse bakerst (men før eventuelle opsjoner man har mulighet til å angi etter et komma). Da slipper man å bruke en slik `keep if` kommando.

```
 keep if bostedskommune == "0301" | bostedskommune == "4601" | bostedskommune == "5001"

```

Etter denne kommandoen er kjørt, er det kun individer som er bosatt i Oslo, Bergen og Trondheim per 1. januar 2023 i datasettet, og individer som er bosatt i andre kommuner enn disse, er fjernet.

### Analyse

For å finne gjennomsnittsinntekten i Oslo, Bergen og Trondheim, kan vi bruke kommandoen `barchart` med variablene `lønn22` og `bostedskommune`. Denne kommandoen genererer et søylediagram som viser gjennomsnittsinntekten for de som er bosatt i Bergen, Trondheim og Oslo siden det er disse som er inkludert i datasettet.

```
 barchart (mean) lønn22, over(bostedskommune) horizontal

```

`barchart(mean) lønn22` spesifiserer at man ønsker å lage et søylediagram som viser gjennomsnittsverdien `(mean)` av variabelen `lønn22`

`over(bostedskommune)` grupperer dataene etter bostedskommune, slik at gjennomsnittsinntekten beregnes separat for hver av de spesifiserte kommunenene.

`horizontal` angir at søylediagrammet skal være horisontalt. Uten denne opsjonen ville diagrammet vært vertikalt som standard.

Kommandoen gir dette resultatet:

[bilde](https://microdata.no/manual/assets/images/image164-9516dcfa2a3e0fb9aa403d12a8416357.png)

### Innebygd hjelpefunksjon

Kommandoen `help` gir detaljert informasjon om kommandoer og bruken. For eksempel, ved å skrive `help barchart`, får man en forklaring på hvordan `barchart`-kommandoen fungerer, inkludert syntaks og eksempler.

`help barchart` gir dette resultatet:

[bilde](https://microdata.no/manual/assets/images/image171-4d08adeeee6b303884259eb2326134a9.png)

### Importering av flere variabler

```
 import db/BEFOLKNING_KJOENN as kjønn

```

Dersom man ønsker å importere flere variabler, kan dette gjøres når som helst i skriptet. For å se kjønnsfordelingen på gjennomsnittsinntekt i bostedskommuner, kan man importere kjønn og bruke denne i analysen. Variabelen kjønn har verdien "1" for mann, og "2" for kvinne. Denne variabelen har temporalitetstypen fast, og man trenger derfor ikke spesifisere dato. Denne variabelen dukker også opp i samme datasett som man ser i vinduet til høyre etter kommandoen er kjørt.

[bilde](https://microdata.no/manual/assets/images/image172-4ee7dcc3cb02bc96918049273131e1f8.png)

Slik ser datasettet ut etter `kjønn` er importert (illustrasjon):

| **personID** | **lønn22** | **bostedskommune** | **kjønn** |
|---|---|---|---|
| 1 | 450 000 | "0301" (Oslo) | "2" (Kvinne) |
| 2 | 320 000 | "4601" (Bergen) | "1" (Mann) |
| 3 | 150 000 | "0301" (Oslo) | "1" (Mann) |
| 4 | 700 000 | "5001" (Trondheim) | "2" (Kvinne) |

### Gjennomsnittsinntekt i Oslo, Bergen og Trondheim fordelt på kjønn

Her brukes `barchart`-kommandoen for å lage et søylediagram per kommune, fordelt på kjønn

#### Gjennomsnittsinntekt i Oslo fordelt på kjønn

```
 barchart (mean) lønn22 if inlist(bostedskommune, "0301"), over(kjønn) horizontal

```

`inlist()`: Denne betingelsen filtrerer dataen slik at kun observasjoner med den bestemte bostedskommunen inkluderes i analysen.

[bilde](https://microdata.no/manual/assets/images/image165-20ef4de591c7c3ef43f4a461c51d5a14.png)

#### Gjennomsnittsinntekt i Bergen fordelt på kjønn

```
 barchart (mean) lønn22 if inlist(bostedskommune, "4601"), over(kjønn) horizontal

```

[bilde](https://microdata.no/manual/assets/images/image166-60ca1b192cdd3640a69f5371faecb737.png)

#### Gjennomsnittsinntekt i Trondheim fordelt på kjønn

```
 barchart (mean) lønn22 if inlist(bostedskommune, "5001"), over(kjønn) horizontal

```

[bilde](https://microdata.no/manual/assets/images/image167-4ae4a39b1cd2e7b4844e59c8cd901cbe.png)

### Hele skriptet

```
 require no.ssb.fdb:38 as db
create-dataset persondata

import db/INNTEKT_WLONN 2022-12-31 as lønn22
import db/BEFOLKNING_KOMMNR_FORMELL 2023-01-01 as bostedskommune
keep if bostedskommune == "0301" | bostedskommune == "4601" | bostedskommune==  "5001"

//Gjennomsnittsinntekt for Oslo, Bergen og Trondheim
barchart (mean) lønn22, over(bostedskommune) horizontal
help barchart

import db/BEFOLKNING_KJOENN as kjønn
barchart (mean) lønn22 if inlist(bostedskommune, "0301"), over(kjønn) horizontal
barchart (mean) lønn22 if inlist(bostedskommune, "4601"), over(kjønn) horizontal
barchart (mean) lønn22 if inlist(bostedskommune, "5001"), over(kjønn) horizontal

```
