---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/finn-ut-hvilke-data-du-trenger/gjor-data-ki-klare-med-fair-prinsippene"
hentet: "2026-11-14"
---

# Gjør data KI-klare med FAIR-prinsippene

For at KI-systemer skal kunne gi pålitelige og nyttige resultater er det ikke nok å gi dem tilgang til store mengder data. Dataene må også være strukturerte, beskrevet og satt inn i en tydelig faglig og organisatorisk kontekst.

KI-modeller uten tilgang til godt beskrevne data, metadata og felles begreper vil ofte ha begrenset evne til å forstå hvordan virksomheten faktisk fungerer og hva data egentlig representerer. Resultatet kan bli analyser og svar som virker plausible, men som ikke kan brukes direkte i virksomhetens prosesser og beslutninger.

Det er derfor viktig å arbeide systematisk med

- begrepsbeskrivelser og semantiske modeller
- metadata og dokumentasjon
- standarder og informasjonsmodeller
- regler, roller og prosesser for dataforvaltning

Dette gjør det mulig å forstå, dele og bruke data på en konsistent måte på tvers av systemer og virksomheter. I noen sammenhenger brukes også ontologier for å beskrive begreper, relasjoner og regler på en maskinlesbar måte.

## FAIR-prinsippene

FAIR-prinsippene gir en felles ramme for god dataforvaltning, spesielt når data kommer fra ulike kilder og skal brukes på tvers av systemer og virksomheter. Prinsippene ble introdusert i 2016 som et svar på økende mengder data som er vanskelige å finne, forstå og gjenbruke.

FAIR står for:

- Findable – data og metadata skal være lette å finne og identifiseres entydig ved hjelp av unike og persistente identifikatorer og gode beskrivelser for både mennesker og maskiner.
- Accessible – data skal være tilgjengelige gjennom standardiserte og kontrollerte mekanismer.
- Interoperable – data skal være strukturert og beskrevet slik at de kan lastes ned, brukes, forstås og kombineres med andre data, både av mennesker og maskiner.
- Reusable – data skal ha tydelig dokumentasjon, kjent opprinnelse og klare betingelser for videre bruk.

## Standarder og FAIR-prinsippene

FAIR-prinsippene er ikke en teknisk standard i seg selv, men prinsipper for hvordan data bør beskrives, forvaltes og deles. I praksis støttes FAIR av et økosystem av standarder, spesifikasjoner og mekanismer som sammen gjør data lettere å finne, få tilgang til, forstå og gjenbruke.

Dette inkluderer blant annet:

- Metadatastandarder
- Persistente identifikatorer
- API-standarder
- Autentisering og tilgangsstyring
- Semantiske modeller og vokabularer
- Lisens- og bruksvilkår

Det finnes ingen enkelstandard som “løser FAIR”. Ulike standarder støtter ulike deler av FAIR-prinsippene.

### Findable – data skal kunne finnes og identifiseres

For at data skal kunne oppdages og referes til må både data og metadata kunne søkes opp og identifiseres entydig. Målet er at både mennesker og maskiner skal kunne finne data, forstå hva de beskriver og referere til dem på en stabil måte.

Dette støttes blant annet gjennom:

- Persistente identifikatorer som DOI, URI og Handle.
- Datakatalogstandarder som DCAT-AP.
- Metadatastandarder som Dublin Core og DateCite.
- Katalogtjenester, API-er og søkeindekser.

### Accessible – data skal kunne hentes ut

FAIR innebærer at data skal kunne hentes ut gjennom standardiserte kommunikasjonsprotokoller. Tilgang skal være åpen eller kontrollert, avhengig av sikkerhet, personvern og tilgangsregler.

Typiske mekanismer er:

- HTTPS og REST-API-er
- GraphQL og OData
- OAuth2 og OpenID Connect
- EIDAS og andre tillitsmekanismer

Dette er særlig viktig i europeiske dataområder og ved sikker datadeling mellom virksomheter.

FAIR innebærer også at metadata bør være tilgjengelige selv om selve datasettet ikke lenger er det. Derfor er metadataforvaltning og datakataloger sentrale komponenter.

### Interoperable – data skal kunne forstås og kombineres

Interoperabilitet handler om at systemer skal kunne forstå og bruke data på tvers av teknologier, organisasjoner og domener. Dette krever at semantikken er eksplisitt og maskinlesbar. Interoperabilitet er ofte den mest krevende delen av FAIR fordi det handler om mer enn teknisk integrasjon. Systemene må også forstå betydningen av dataene på samme måte.

Typiske standarder og teknologier er:

- SKOS og felles kontrollerte vokabularer.
- Felles informasjonsmodeller og andre felles begrepsmodeller.
- RDF og JSON-LD.
- OWL og ontologier.
- SHACL og valideringsregler.
- SPARQL og semantiske spørringer.

### Reusable – data skal kunne brukes på nytt

For at data skal kunne gjenbrukes må de være tilstrekkelig dokumentert og ha tydelige regler for bruk.

Dette omfatter blant annet:

- Lisensinformasjon som Creative Commons og SPDX.
- Proveniens og sporbarhet gjennom W3C PROV og PROV-O.
- Metadata om kvalitet, opprinnelse og kontekst gjennom W3C DQV.
- Domenestandarder som HL7 FHIR, INSPIRE og GS1.

Dette blir stadig viktigere i arbeidet med kunstig intelligens og KI-governance der det er nødvendig å kunne dokumentere hvor data kommer fra, hvordan de er behandlet og hvilke begrensninger som gjelder.

FAIR handler ikke om at alle data skal være åpne, men om at de skal være så tilgjengelige og gjenbrukbare som mulig innenfor gjeldende regler for blant annet personvern og sikkerhet.

## FAIR og kunstig intelligens

FAIR-prinsippene er et viktig grunnlag for å gjøre data klare for deling, gjenbruk og bruk i kunstig intelligens. FAIR alene er imidlertid ikke nok for å lykkes med kunstig intelligens. Data må også være pålitelige.

Med pålitelige data mener vi data som har god kvalitet, er dokumentert, oppdaterte og håndtert på en måte som skaper tillit. Her er ISO-25012 relevant. ISO-25012 er en internasjonal standard for datakvalitet som beskriver hvilke egenskaper data bør ha for å være egnet til bruk. Standarden omfatter blant annet kvalitetsdimensjoner som nøyaktighet, fullstendighet, konsistens, aktualitet og tilgjengelighet. For KI-systemer er disse dimensjonene viktig fordi kvaliteten på dataene i stor grad påvirker kvaliteten på resultatene.

Data som både følger FAIR-prinsippene og er pålitelige er et godt grunnlag for utvikling, trening og bruk av kunstig intelligens.

I offentlig sektor støttes FAIR-prinsippene blant annet gjennom arbeid med felles datakataloger, API-er, semantisk interoperabilitet og bruk av felles begrepsbeskrivelser.

For KI-systemer er det ikke tilstrekkelig at data eksisterer. Dataene må kunne identifiseres, forstås, kobles sammen og brukes i riktig kontekst. Derfor er det viktig å forstå forskjellen mellom data, datasett og metadata og hvordan disse beskrives og forvaltes i praksis.

## Hva er data,datasett og metadata?

For å arbeide systematisk med FAIR-prinsippene er det viktig å forstå forskjellen mellom data, datasett og metadata.

Data er observasjoner eller fakta, for eksempel målinger fra sensorer, svar i et skjema eller tekst i dokumenter. Rådata kommer direkte fra kilden og kan inneholde feil, mangler eller ulike formater. Før data kan brukes i analyser og KI-systemer må de derfor klargjøres og struktureres. Når data tolkes og settes inn i en relevant sammenheng blir de til informasjon som kan gi innsikt og danne grunnlag for beslutninger.

Et datasett er en avgrenset samling av data som brukes til et bestemt formål.

For at et datasett skal kunne forstås og brukes riktig må det beskrives med metadata. Metadata er informasjon om dataene, for eksempel hva de inneholder, hva de betyr, hvor de kommer fra, hvordan de er samlet inn og hvilke regler som gjelder for bruk.

Et datasett består derfor av både data og metadata. Sammen gjør dette dataene forståelige og brukbare på tvers av systemer og virksomheter.

## Metadata og maskinlesbarhet

Metadata bør følge dataene tett og være maskinlesbare. Når informasjon om innhold, struktur, opprinnelse og bruk følger med dataene blir det enklere å finne, forstå, kombinere og gjenbruke dem. Dette er særlig viktig for KI-systemer som ofte kombinerer data fra mange ulike kilder og kontekster.

I praksis betyr dette at kvaliteten ikke bare må ligge i systemene der dataene lagres, men i selve dataene og beskrivelsene av dem.

FAIR kan i praksis forstås som et rammeverk for operasjonalisert interoperabilitet. Prinsippene henger sammen med arbeid innen

- semantisk interoperabilitet
- API-strategier
- tillitstjenester
- europeiske datarom
- KI-governance

I offentlig sektor støttes dette blant annet gjennom felles datakataloger, begrepsbeskrivelser, standardiserte API-er og felles spesifikasjoner for datadeling.

FAIR er derfor ikke lenger bare relevant for forskningsdata, men er i ferd med å bli en grunnmodell for sikker og skalerbar datadeling i Europa.

## FAIR gjelder ikke bare data – men hele KI-økosystemet

FAIR-prinsippene ble opprinnelig utviklet for å gjøre forskningsdata lettere å finne, dele, forstå og gjenbruke. I arbeidet med kunstig intelligens brukes FAIR nå i økende grad som et bredere rammeverk for hele KI-økosystemet. Dette omfatter ikke bare datasett, men også:

- KI-modeller
- Algoritmer
- Programvare
- Workflows og pipelines
- Metadata og digitale objekter generelt

Bakgrunnen er at moderne KI-systemer er avhengig av langt mer enn tilgang til data alene. For å kunne utvikle, evaluere og bruke KI på en trygg og skalerbar måte må også modeller, prosesser og programvare være dokumenterte, sporbare og interoperable. Dette er viktig for å kunne utvikle pålitelige KI-løsninger som kan deles, evalueres og brukes på tvers av organisasjoner, sektorer og teknologiske miljøer.

[Artikkelen FAIR for AI: An interdisciplinary and international community building perspective](https://arxiv.org/pdf/2210.08973) peker på at KI-modeller bør beskrives med metadata på samme måte som datasett. Dette kan blant annet omfatte

- hvordan modellen er trent
- hvilke data som er brukt
- begrensninger og usikkerhet
- bias og kjente svakheter
- versjoner og endringer
- sporbarhet

Arbeidet med å beskrive KI-modeller gjennom metadata støttes også av standarder som MLDCAT-AP, som gir en felles struktur for å dokumentere maskinlæringsmodeller, treningsdata og evalueringer på en måte som fremmer sporbarhet, gjenbruk og interoperabilitet.

Dette er viktig for å kunne forstå hvordan KI-systemer fungerer, hvilke begrensninger de har og om de kan brukes i nye sammenhenger.

FAIR kan derfor forstås som en viktig del av grunnlaget for ansvarlig, interoperabel og skalerbar bruk av kunstig intelligens.

[Les artikkelen fra 2016 som introduserte FAIR-prinsippene.](https://www.nature.com/articles/sdata201618.pdf)
