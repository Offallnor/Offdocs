---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/kartlegg-datakilder/begrepsmodeller"
hentet: "2026-11-14"
---

# Bli KI-klar med begrepsmodeller

Kunstig intelligens kan analysere store mengder informasjon og generere svar på sekunder. Likevel opplever mange virksomheter at KI gir ulike svar på samme spørsmål, misforstår fagbegreper eller mangler forståelse for hvordan data henger sammen. Problemet er ofte ikke selve KI-modellen, men at dataene mangler struktur, kontekst og felles definisjoner. Begrepsmodeller kan være en del av løsningen.

De store språkmodellene er gode til å gjenkjenne mønstre i språk og å generere tekst, men de har ikke en innebygd forståelse av virksomheten sine begreper, forretningsregler eller sammenhenger.

## KI trenger struktur og kontekst

Uten en strukturert kontekst kan de

- tolke begreper ulikt fra gang til gang
- ha begrenset forståelse av sammenhenger i data
- gi svar som ser riktige ut, men som ikke er konsistente eller etterprøvbare

KI trenger ikke bare data, men også mening og sammenheng. Begrepsmodeller, også kalt ontologier, kan være en del av løsningen. Ved å beskrive hva sentrale begreper betyr og hvordan de henger sammen gir de KI et tydeligere grunnlag for å tolke data riktig. Sammen med forretningsobjekter og forretningsnøkler kan de bidra til mer konsistente, forklarbare og gjenbrukbare KI-løsninger.

## Begrepsmodeller

Begrepsmodeller brukes til å definere begreper, objekter og relasjoner på en god måte. De bidrar til å etablere en felles forståelse ved å tydeliggjøre hva sentrale begreper betyr og hvordan de henger sammen.

Det er et verktøy for å strukturere informasjon og gjør det enklere å samarbeide, redusere misforståelser og sikre at alle jobber mot samme mål. I utvikling av KI-systemer samarbeider ofte domeneeksperter, jurister og tekniske miljøer. Disse kan ha ulik forståelse av begreper og bruke forskjellige ord for det samme.

Begrepene oppstår ikke i et vakuum, de utvikles gjennom virksomheten sine prosesser, tjenester og oppgaver. Det er derfor viktig at begrepsmodellen henger tett sammen med hvordan virksomheten faktisk jobber i praksis. Gode begrepsmodeller beskriver ikke bare data, de speiler hvordan virksomheten jobber.

Arbeidet med begrepsmodeller bør derfor gjøres i samarbeid mellom fagpersoner, jurister og tekniske miljøer innenfor domenet. Felles forståelse må fortsatt bygges av mennesker.

KI trenger struktur gjennom mening og sammenhenger hvor begrepsmodeller beskriver betydning, neste steg er at forretningsobjekter gjør strukturen operativ i data og systemer.

## Forretningsobjekter og forretningsnøkler

Et forretningsobjekt er en sentral “ting” i domenet du jobber med, noe du ønsker å beskrive, analysere eller ta beslutninger om. Eksempler kan være en person, en virksomhet, en søknad eller et kjøretøy.

I tråd med god datastyring er det viktig å definere forretningsobjekter tidlig fordi det gjør det lettere å strukturere data, sikre felles forståelse og legge grunnlaget for god datakvalitet og gjenbruk.

For at et forretningsobjekt skal kunne gjenkjennes entydig på tvers av systemer brukes en forretningsnøkkel.

Eksempel på forretningsobjekt og forretningsnøkkel

Et klassisk eksempel er kjøretøy som forretningsobjekt. Her brukes VIN-nummeret (Vehicle Identification Number) som forretningsnøkkel. VIN-nummeret er en unik kode på 17 tegn som identifiserer et kjøretøy. Nummeret består av bokstaver og tall og er bygget opp etter en internasjonal standard.

De ulike delene av VIN-nummeret gir informasjon om blant annet

- produsent og produksjonsland
- kjøretøytype og modell
- produksjonsår og fabrikk
- et unikt serienummer for kjøretøyet

Dette gjør VIN-nummeret til en god forretningsnøkkel fordi den identifiserer hvert kjøretøy unikt, brukes på tvers av systemer (register, forsikring, verksted osv.) og er stabil over tid.

Dette gjør det mulig å koble sammen data om samme kjøretøy fra ulike kilder på en pålitelig måte.

## Slik lager du begrepsmodeller

KI kan være et nyttig verktøy for å komme raskt i gang med begreps- og kunnskapsmodeller. Du kan bruke KI til å lage forslag til begreper, definisjoner og sammenhenger og et førsteutkast til struktur. Samtidig er det viktig å være klar over at KI ikke kjenner virksomhetens kontekst fullt ut. Begreper og definisjoner må derfor alltid kvalitetssikres og forankres i fagmiljøet.

- Involver fagpersoner. Domenekunnskap er avgjørende for å få riktige begreper og sammenhenger.
- Definer sentrale begreper, objekter og relasjoner i det området KI-systemet skal brukes. Sørg for at samme begrep betyr det samme på tvers av systemer.
- Sikre gjenbruk. Se til etablerte standarder og begreper innen eget domene der det finnes for å sikre konsistent bruk, enklere deling og gjenbruk av data.
- Knytt metadata tett til dataene. Beskriv hva dataene betyr, ikke bare hvordan de er lagret.
- Bygg gradvis. Du trenger ikke en fullstendig begrepsmodell fra start – utvikle den iterativt.

Ved å bruke etablerte standarder kan data fra ulike kilder kobles sammen uten store tilpasninger. Dette gjør systemet mer fleksibelt og enklere å videreutvikle samtidig som dataene kan gjenbrukes i andre løsninger. I tillegg reduseres risikoen for misforståelser, for eksempel knyttet til ulike enheter eller begreper.

Eksempel: Identifisere forretningsobjekter og forretningsnøkler

I et smart vanningssystem er plante et forretningsobjekt.

Dette er fordi systemet skal ta beslutninger basert på behovene til hver plante, for eksempel hvor mye vann den trenger. For å gjøre dette må planten beskrives med relevante egenskaper, som

- type plante
- vannbehov
- plassering
- jordtype

For at systemet skal kunne kjenne igjen samme plante over tid og på tvers av systemer, må hver plante ha en entydig identifikator (en forretningsnøkkel), for eksempel en plante-ID.
