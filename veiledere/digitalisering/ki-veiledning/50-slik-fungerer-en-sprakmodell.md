---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/slik-fungerer-en-sprakmodell"
hentet: "2026-11-14"
---

# Slik fungerer en språkmodell

Publisert4. juni 2026

Generativ KI er designet for å skape nytt innhold basert på mønstre den har lært, for eksempel tekst, kode, bilder eller lyd. En form for generativ KI som mange er kjent med er språkmodellen.

En språkmodell fungerer ved å beregne sannsynligheten for hvilket ord som kommer videre, basert på alle de ordene som har kommet før. Den har ikke kunnskap i tradisjonell forstand, men kjenner igjen mønstre i de enorme tekstmengdene den er trent på.

## Du kan bygge en tjeneste på en språkmodell

En språkmodell kan brukes direkte gjennom å skrive og snakke med et grensesnitt, slik som mange er vant til fra for eksempel ChatGPT eller Claude. Men du kan også bygge egne tjenester med utgangspunkt i en språkmodell. Du kan for eksempel lage en chatbot tilpasset din virksomhet eller et system som svarer på spørsmål basert på egne dokumenter, som på [arkivverket.no](http://arkivverket.no/).

Uavhengig av hvordan du bruker en språkmodell, er det nyttig å forstå hvordan den fungerer og hva du kan gjøre for å få best mulig nytte av den.

## Du får sannsynlige svar

Siden mye av treningsdataen faktisk inneholder korrekt informasjon, ender språkmodellen ofte, men ikke alltid, opp med å gi riktige svar. Svaret du får når du spør en språkmodell er ikke sant, det er sannsynlig.

I praksis betyr dette at du aldri kan garantere at et svar er korrekt, og at du bør tilpasse hvor mye vekt du legger på svaret etter hvordan svaret skal brukes. For trivielle, dagligdagse spørsmål er det sannsynlige svaret ofte godt nok. For beslutninger med større konsekvenser, for eksempel medisinske, juridiske eller økonomiske, må svaret fra språkmodellen sjekkes opp mot pålitelige kilder.

## Slik trenes språkmodellen

Før en språkmodell kan brukes, må den trenes opp med kjent informasjon for å kunne analysere nytt innhold.

### Modellen får tilgang til data

Første steg kalles fortrening. Da får modellen milliarder av tekstdokumenter som bøker, artikler eller kode. Så får modellen en tekstbit og prøver å gjette neste ord. For eksempel leser modellen setningen "Katten satte seg på..." og prøver å gjette neste ord. Den ser at "matten" eller "sofa" er sannsynlig, men "flyet" ikke er det.

Gjennom mange slike små gjetninger justeres modellens parametre gradvis, og den fanger opp hvordan mønstre i språk, fakta og resonnement henger sammen. Resultatet av fortreningen kalles ofte en grunnmodell eller basismodell. Den er veldig god på språk, men ikke særlig hjelpsom.

### Finjustering

Neste steg er å finjustere modellen slik at den blir mer hjelpsom. Da trenes den videre på et mindre, utvalgt datasett bestående av eksempler som er nyttige for bruksområdet til modellen. Dette kan for eksempel være gode samtaler mellom brukere og modellen.

Disse eksemplene er ofte skrevet eller kvalitetssikret av mennesker. Målet er at modellen skal lære formen på en hjelpsom samtale, og ikke bare språkmønstre generelt.

### Forsterket læring med menneskelig tilbakemelding

I det tredje steget bidrar menneskelige vurderinger til å forme modellens oppførsel. Modellen produserer flere mulige svar på samme spørsmål, og mennesker rangerer hvilke svar som er best. Disse rangeringene brukes til å justere modellen slik at den lærer å produsere svar som mennesker foretrekker.

## Systeminstrukser

Systeminstrukser er ikke en del av treningen, men en innstilling som styrer modellens oppførsel. Det er viktig å skille mellom modellen og produktet den brukes i. Modellen er selve det nevrale nettverket, mens produktet er grensesnittet brukerne møter. ChatGPT er for eksempel et produkt fra OpenAI som bruker modeller fra GPT-familien. Mistral Vibe er for eksempel et produkt som bruker modeller fra Mistral AI.

Når modellen skal brukes i et produkt, gir leverandøren den ofte systeminstrukser. De beskriver rollen modellen skal ha, for eksempel “du er en hjelpsom lærer”, og regler som modellen skal følge. Hvis du utvikler en tjeneste med en språkmodell, kan du gi den egne systeminstrukser i tillegg til dem fra leverandøren.

Hvordan “leser” en språkmodell?

En datamaskin jobber ikke med ord direkte, men med tall. Derfor må tekst først oversettes til noe modellen kan regne på. Først deles teksten opp i små biter kalt tokens. Et token kan være et helt ord, en del av et ord, eller bare et tegn. Setningen “Katten sover” kan for eksempel bli til tokenene “Katt, “en”, “sov” og “er”.

Hvert token oversettes deretter til en vektor, grovt sagt en rekke tall som til sammen representerer tokenet. Denne vektoren kalles en innbygging (embedding). Tokens som brukes på lignende måter, får lignende vektorer, slik at eksempelvis “katt” og “hund” har lignende vektorer, mens “katt” og “kvantefysikk” ligger langt fra hverandre.

Disse innbyggingene formes underveis i treningen, og er det som lar modellen gjøre språk om til matematikk.

## Modellen kan hallusinere

Av og til gir modellen deg et svar som ikke er sant. Det kalles «hallusinering». Dette skjer som oftest fordi du spør om noe som veldig sjeldent er i dataene den er trent på. Derfor kjenner den ikke så godt til det du spør om.

Istedenfor å si at den «ikke vet», så vil den beregne hvilke ord som statistisk passer best sammen for å danne en setning som ser riktig ut, uten at den nødvendigvis er det.

Modellen tar altså ikke feil på samme måte som mennesker gjør det. Snarere er problemet at modellen ikke har evne til å vite hva den ikke vet. Derfor vil den svare like selvsikkert på noe den kan mye om som på noe den egentlig ikke har grunnlag for å svare på, og det kan derfor være vanskelig for brukerne å se forskjellen.

## Reduser hallusinering

Det er ikke mulig å eliminere hallusinering fullstendig, men det er flere måter å redusere sannsynligheten for at det skal skje.

### Bruk systeminstruksen

Man kan skrive inn regler for dette i systeminstruksen, som for eksempel: «Du er en hjelpsom lærer og en nøyaktig assistent. Du må aldri finne på ting. Hvis du ikke vet svaret, må du svare «Jeg vet ikke». Du må alltid basere svaret ditt på dokumentene jeg gir deg.»

Slike instrukser vil sannsynligvis gi bedre resultater, men vi har ingen garanti for at modellen faktisk følger dem.

Du kan også bruke systemintruksen til å kreve å få referanser til svarene slik at du kan faktasjekke hvilke kilder den refererer til. Ikke så rent sjelden vil oppdiktede svar bli forsøkt bekreftet av oppdiktete kilder, så er du usikker på svaret modellen gir, kan dette være en måte å sjekke det på.

### Begrens kildene modellen bruker

Du kan «binde modellen» til pålitelige kilder av informasjon ved hjelp av en metode kalt Retrieval Augmented Generation (RAG). Da velger du hvilke kilder modellen skal hente informasjon fra, og tilgjengeliggjør det for modellen. «Retrieval» refererer til at den henter informasjon fra materiale som du har gjort tilgjengelig for den. Når modellen skal lage et svar bruker den relevant informasjon kun fra de kildene du har valgt.

Kunnskapsassistenten er en KI-chat bygget på RAG-arktitektur. Svarene den gir er basert på et avgrenset utdrag av Kudos-databasen. [Les mer om Kunnskapsassistenten](https://ki.norge.no/eksempler/digdir-kunnskapsassistenten).

### Temperatur

En annen måte å øke sannsynligheten for å få korrekt svar, er å justere «temperaturen» i modellen. Temperatur refererer her hvor stor frihet modellen har til å velge blant utvalget av neste ord/tokens. Velger man lav temperatur, må modellen gå for den som er rangert høyest, som er gitt størst sannsynlighet. Velger man høy temperatur, så har modellen større frihet til å velge mellom ordene/tokens med størst sannsynlighet.

## Kontekstvinduet påvirker kvaliteten

Hvis du opplever at du får dårlige svar fra en språkmodell, eller at den ikke klarer å sammenstille informasjon fra mange dokumenter samtidig, kan det være at det har noe med kontekstvinduet å gjøre.

Kontektsvinduet kan du tenke på som «arbeidsminnet» til modellen. Det definerer hvor mye informasjon den kjenner til og klarer å holde samlet samtidig. I kontekstvinduet ligger alt du har skrevet tidligere i samtalen, innhold modellen har generert i samtalen, dokumenter du enten har lastet opp eller tilgjengeliggjort og systeminstruksene.

Dette vinduet kan være stort, altså at det er plass til mye informasjon, eller det kan være smalt, altså at det er plass til bare en liten mengde informasjon. Det er ikke uendelig plass i kontekstvinduet, og det kan bli fullt. Mange modeller fungerer slik at det som kom først inn, må ut først. Det betyr at spørsmål, dokumenter og systeminstrukser fra tidlig i samtalen forsvinner først.

For å løse dette kan du for eksempel bytte til en modell med større kontektsvindu, eller dele opp arbeidet i bolker.

## Gjøre informasjon tilgjengelig

Det er flere måter å gjøre informasjon tilgjengelig for språkmodellen. Noe kan alle gjøre, noe må gjøres av en med teknisk kompetanse.

Du kan laste opp dokumenter eller koble KI-modeller på eksisterende infrastruktur og datastrømmer. Det gjør at du slipper å laste opp relevante dokumenter og data manuelt og flere ganger.

For eksempel kan du tilgjengeliggjøre informasjon og regler om ferieavvikling i din virksomhet fra Sharepoint. Da kan en ansatt stille spørsmål om ferieavvikling, og modellen kan finne ansattinstruksen og se informasjon om hvilke ferieregler som gjelder. I neste steg kan den gi den ansatte en god forklaring, inkludert lokale bestemmelser i virksomheten, i stedet for å bare ta utgangspunkt i for eksempel ferieloven.

## Slik kobler du data på modellen

Hvis du vil koble modellen til virksomhetens data, kan du velge mellom to hovedmetoder, API og MCP.

API, (Application Programming Interface), er den tradisjonelle måten å koble KI til data. Hver datakilde, for eksempel offentlig registere eller felles SharePoint i virksomheten, får en unik tilkobling. Man må skrive kode som spør: "gi meg data fra det offentlige registeret", "gi meg data fra Sharepoint" og så videre.

Ulempen med denne tilnærmingen er at hvis du trenger data fra mange ulike systemer, så må du ha tilsvarende antall koblinger. Når et system oppdateres, må koden for tilkoblingen oppdateres manuelt. Bruk av API gjør også at modellen ikke ser "hele bildet", den ser bare de dataene som er kodet inn for en spesifikk oppgave. Fordelen med API er at det er en etablert og kjent standard, som har vært tilgjengelig i lang tid og som finnes i de fleste systemer.

MCP (Model Context Protocol) er en ny, åpen standard som fungerer som en «USB-port» for KI. Den lar modellen koble seg til ulike datakilder som lokale mapper, databaser eller API-er, ved hjelp av en standardisert driver. Dette gjør det enklere å koble sammen mange systemer. Modellen får dermed en bedre forståelse av hele virksomhetens, ikke bare fragmenterte biter. Dette er viktig for å unngå feil i saksbehandling der informasjon ligger spredd i flere systemer.

MCP kan brukes der man ønsker å bygge KI agenter som jobber på tvers av mange systemer uten omfattende manuell programmering. Men før man investerer i MCP, må man sørge for god kvalitet på data og god dataforvaltning i virksomheten. Ved MCP så får man bedre oversikt og tilgang på egne data, men det gjør ikke at data i seg selv er strukturerte og av god kvalitet.
