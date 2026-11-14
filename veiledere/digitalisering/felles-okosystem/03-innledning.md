---
veileder: "Felles økosystem"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/digital-samhandling/innledning/4169"
hentet: "2026-11-14"
---

# Innledning

Opprettet: 03. januar 2023

Sist endret: 08. desember 2023

«Arkitektur for hendelser i Felles Økosystem» er et grunnlag for å utveksle og agere på hendelser på tvers av virksomheter og tjenester. Det er således ikke en teknisk løsningsarkitektur, men vil peke på konseptet og en beste praksis for utveksling av hendelsesinformasjon slik at sammenhengende tjenester kan realiseres.

Hovedprinsippene for en hendelsesdrevet arkitektur er at en hendelse blir sendt ut i det øyeblikk det skjer en endring i en tilstand. Det er en «Push» av hendelser fra tilbyder/produsent av hendelser, som en eller flere konsumenter kan agere på i det øyeblikk den gjenkjenner en hendelse. Dette fører til at tjenestene blir minimalt koblet, kommunikasjonen går én vei og den er ikke avhengig av styrende kommandoer.

Økosystem for nasjonal digital samhandling og tjenesteutvikling, skapes gjennom måten vi samhandler på, på tvers av sektorer, fagområder og bransjer.

For å utvikle sammenhengende tjenester i økosystemet er det helt sentralt at vi har evnen til å ta brukerperspektivet, og at vi etablerer og sikrer samarbeid og styring mellom aktørene – Vi starter sammen, vi former sammen og vi leverer sammen!

Samtidig må vi erkjenne at aktørene som samhandler i økosystemet i stor grad er autonome og at tjenester og data er distribuert. For å levere sammenhengende tjenester til innbyggere og virksomheter på en dynamisk og effektiv måte, må vi etablere evnen til å fange opp når en hendelse inntreffer. Vi må kunne publisere hendelser og gjør det mulig for andre aktører å abonnere på disse hendelsene. Tjenesteeierne må kunne tilgjengeliggjøre beskrivelser av sine tjenester slik at tjenestene kan sammenkobles eller integreres med andre tjenester og danne tjenestekjeder. Sammenkoblingene bør skje på en måte som gir størst mulig fleksibilitet for de involverte aktørene.

### Utfordringsbildet

Hovedutfordringer

1. Sammenhengende tjenester utvikles i (større) siloer, og det er risiko for at disse blir lite fleksible med hensyn til videreutvikling og nye kontinuerlige behov.
2. Manglende kunnskap og kompetanse på hva, hvorfor og hvordan «hendelser» må håndteres fra konsept til løsning, og hvilken effekt det vil ha på fremtidig tjenesteutvikling
3. Det finnes ingen dominerende tilnærming til utveksling av hendelser, meldingsformat eller meldingskommunikasjon på tvers av hendelsesdrevet integrasjonsteknologi. Å forstå hvordan aktørene skal utveksle hendelser er nøkkelen til å vurdere fordelene vi kan oppnå.

### Sammenhengende tjenester utvikles i større siloer

Sammenhengende tjenester utvikles i større siloer der et begrenset antall aktører samarbeider om å utvikle en sammenhengende tjeneste. Sammenhengende tjenester blir i stor grad orkestrert. Dette fører til redusert mulighet for gjenbruk, og endringer i den sammenhengende tjenesten krever mye koordinering fra de involverte aktørene.

Eksempler på sammenhengende tjenester som orkestreres (se [Eksempler på behov og scenarier](https://www.digdir.no/digital-samhandling/eksempler-pa-behov-og-scenarier/4694)):

- Byggesøknad
- Oppgjør etter dødsfall
- eBevis

#### Orkestrering av tjenester

Orkestrering av tjenester

Som figuren over illustrerer er det en sentral prosess (dirigent/koordinator) som styrer interaksjonene med tjenestene som inngår i tjenestekjeden. Den sentrale prosessen bestemmer spillereglene for deltakelse i kjeden og den definerer kjeden fra begynnelse til slutt. Dette kalles orkestrering.

Det er sterk avhengighet mellom tjenestene. Integrasjonene mellom tjenestene gir lite fleksibilitet, skalerer dårlig og det er krevende å få til samhandlingsevne mellom mange tjenester.

En endring i en tjeneste i kjeden vil ofte føre til behov for endringer i de andre tjenestene.

### Manglende kunnskap og kompetanse

Det er manglende kunnskap om hva en hendelse er. Mange blander sammen aktiviteter, kommandoer og hendelser. I tillegg blir livssituasjoner blir noe misvisende kalt livshendelser. En hendelse er en følge av en planlagt eller uplanlagt aktivitet. Aktiviteten kan utføres av en sluttbruker, en saksbehandler eller i en automatisert prosess. Kompetanse om hvordan vi kan utnytte hendelser i teknologien er mangelvare, og i et teknisk perspektiv vil en hendelse føre til behov for tjenester som bruker data, oppretter eller endrer data – slik oppstår en ny hendelse. En hendelse er noe som har skjedd for eksempel

- Barnet er blitt syk
- Vedtak om opphold fattet
- Nabovarsel er sendt
- Enkeltmannsforetak er registrert i foretaksregisteret

En kommando er styrende og formidler noe som skal skje, ved en kommando forventes en respons eller en kvittering tilbake.

- Hendelse
   - En endring i tilstand (noe som har skjedd og beskrives i fortid)
   - Tilbyder har fullt eierskap til hendelsen
   - Det er kun én tilbyder av en hendelse
   - Det er ingen eller mange konsumenter av en hendelse
- Kommando
   - Er en forespørsel som krever en handling og en respons
   - Mottaker tar eierskap til å utføre handlingen som kommandoen krever og gir respons
   - Det er kun én mottaker som kan respondere på en forespørsel
   - Det kan være flere produsenter av forespørsler til samme mottaker

### Ingen dominerende tilnærming

I dag finnes det ingen felles metode eller beste praksis for utveksling av hendelser på tvers av virksomheter og sektorer. Det er fare for at sektorer og virksomheter løser dette på hver sin måte, og at samhandling på tvers ved hjelp av hendelser blir komplekst og i verste fall umulig.

Utveksling av hendelser som samhandlingsform kan bidra til en rekke fordeler for aktørene. Det gir økt fleksibilitet og modularitet i samhandlingen og det vil bidra til svært løse koblinger mellom tjenestene som leveres av de ulike aktørene.

### Hvorfor er det smart å være hendelsesdrevet

For å lykkes med sammenhengende tjenester må tjenestene kunne utvikles mer dynamisk og uavhengig av hverandre og baseres på løse koblinger og koreografi.

#### Koreografi av tjenester

Koreografi av tjenester

Ved koreografi er det ingen sentral eller helhetlig prosess som styrer interaksjonene med tjenestene som inngår i tjenestekjeden. Hver tjeneste i kjeden trigges av et resultat, eller en hendelse fra en eller flere andre tjenester. Dermed har den enkelte tjeneste kontroll på sin egen integrasjon med de andre tjenestene. Dette er illustrert i figuren over.

Ved koreografi baseres arkitekturen på løse koblinger som gir økt fleksibilitet. Tjenester som inngår i kjeden, kan enklere byttes ut, og de kan inngå eller gjenbrukes i flere ulike tjenestekjeder. De enkelte tjenestene trenger ikke å vite om hverandre. Ved koreografi reduseres kompleksitet og sårbarhet.

En beste praksis for «Arkitektur for hendelser i felles økosystem» vil bidra til at virksomhetene kan utveksle og agere på hendelser på tvers. For offentlig sektor er dette en relativt ny måte å samhandle på, på tvers av virksomheter og sektorer. Ved å basere arkitekturen på hendelser vil tjenester kunne tilbys selvstendig eller i en tjenestekjede og nye behov vil kunne støttes i tilnærmet sanntid og uten endringer i tilstøtende tjenester. Tjenester og informasjon vil kunne tilpasses til brukerens behov smidig og kontinuerlig, og det vil være mulig å agere proaktivt overfor bruker.

#### Orkestrering og koreografi av sammenhengende tjenester

Orkestrering og koreografi av sammenhengende tjenester

For sammenhengende tjenester som skal følge en fastlagt prosess der det er viktig å ha kontroll på alle involverte aktører og deres bidrag inn i den sammenhengende tjenesten, vil orkestrering være det beste alternativet. Det vil allikevel være viktig å ikke orkestrere mer enn det som er absolutt nødvendig. Vurder derfor om en kombinasjon av orkestrering og koreografi kan være den beste tilnærmingen for å levere den sammenhengende tjenesten.

### Hypoteser

Arkitektur for hendelser vil bidra til en mer effektiv og enklere utvikling og forvaltning av tjenester og vil kunne gi store kostnadsbesparelser. Det vil være mindre punkt-til-punkt integrasjon, svært løse koplinger og færre avhengigheter mellom tjenestene som tilbys. Dette vil kunne bidra til bedre ytelse i tjenesteleveransene og være et viktig bidrag for økt dataminimering. Det vil være behov for økt kompetanse om hendelsesdrevet arkitektur og etter hvert som modenheten øker vil det være et økende behov å kunne håndtere hendelser i felles økosystem.

Ved hjelp av en hendelsesdrevet arkitektur vil innovasjonskraften øke, både i offentlig-, kommunal- og privat sektor. I dag baseres store deler av samhandlingen på tvers av aktører, på kommandoer og API-oppslag. Tilbyder og konsument må kjenne til hverandre og hvilke behov den andre part har. Ved å basere samhandlingen på hendelser trenger ikke tilbyder å kjenne til konsumentene, hverken hvem de er, hvor mange de er eller hvilke behov de har. Konsumentene kan abonnere på hendelser som er interessant for dem og benytte disse til å skape nye og innovative tjenester. Det ligger et enormt potensial i dette. For eksempel kan et adressebytte være interessant for svært mange ulike aktører, både statlige, kommunale og private tjenester. En kommune kan abonnere på «nye innbyggere» og tilby informasjon og tjenester som er aktuelle for de nye innbyggerne.

### Behov

Vi lever i en tid der store teknologigiganter og servicenæringen tilbyr proaktive og brukertilpassede digitale tjenester. Innbyggere og virksomheter forventer tilsvarende fra det offentlige.

Innbyggerne forventer at hendelser og endringer i livet proaktivt skal påvirker hvilke tjenester som tilbys, og at tjenestene er persontilpassede og relevante. Innbyggerne vil ha sammenhengende tjenester, de ønsker å slippe å forholde seg til mange forskjellige aktører og nettsteder. Informasjon må tilbys helhetlig og enhetlig ut ifra en gitt kontekst.

Virksomheter ønsker å tilby tjenester og informasjon i alle de sammenhenger som er relevante for en bruker. Dette skal kunne skje uten endring av de løsningene eller tjenestene brukeren er i, også når disse tjenestene er utviklet av andre aktører. Dette innebærer at relevante tjenester eller informasjon, utviklet av andre, kan tilbys som en del av egne tjenester. Virksomheter har behov for å finne og få oversikt over tjenester som tilbys av andre aktører, og de må kunne få oversikt over hvilke tjenesteresultat eller hendelser som kan trigge egne tjenester.

Det er et behov for en beste praksis for utveksling av hendelser på tvers av løsninger og sektorer, og der er behov for løsning(er) for å håndtere og utveksle hendelser, både i sektorene selv og som en fellesløsning.

Behovene for å utveksle hendelser er i hovedsak knyttet til to generelle scenario:

1. Tjenestekjeder - hendelser som oppstår etter at en tjeneste er utført, der en eller flere andre tjenester kan/skal bruke resultatet fra denne.
2. Tilgang til hendelsesdata fra datakilder, der det ikke nødvendigvis er en veldig klar tjenestekjede (for eksempel fra registre eller datakilder som tilbyr sammenstilt informasjon)

I tillegg kommer hendelser basert på telemetri og monitorering, og såkalte «komplekse hendelser». Dette vil vi ta inn i videreutviklingen av en «beste praksis»:

- Hendelser basert på telemetri og monitorering knyttes ofte til «IoT – Internet of things»
- «Komplekse hendelser»: hendelser basert på analyse og monitorering av data og/eller flere enkelthendelser

#### Behov for å koble sammen tjenester i sanntid?

For å kunne realisere dynamiske tjenestekjeder som utveksler informasjon mellom distribuerte løsninger på tvers av virksomheter uten komplekse og tette integrasjoner, må tjenestene kunne kobles sammen i tilnærmet sanntid. Et tjenesteresultat eller en hendelse må dermed «pushes» fra en tilbyder-tjeneste til en konsument-tjeneste i det øyeblikket endringen/hendelsen har skjedd.

Eksempler på behov for hendelser i sanntid (scenario 1):

- Advokatregisteret
   - **Endring/hendelse**: «Advokat mistet bevilgning»
   - **Behov**: Konsumenter må agere raskt! Varsel/Melding om hendelsen må sendes ut i det endringen oppstår. Det er behov for en «Push» av hendelsen til konsument.
- E-bevis
   - **Endring/hendelse**: Leverandør må samtykke til oppdragsgiver om innsyn i egne skatteopplysninger
   - **Behov**: For raskere behandling er det behov for at oppdragsgiver får tilgang til skatteopplysninger umiddelbart. Det er behov for en «Push» av hendelsen til konsument.

I noen tilfeller er det mer hensiktsmessig at konsumenten selv kan velge når den ønsker å lese hendelsen og behovet for å få tilgang til en hendelse i sanntid er ikke til stede.

Eksempler på behov for hendelser, men ikke i sanntid (scenario 2):

- Folkeregisteret
   - **Endring/hendelse**: Tilbyder «legger» alle hendelser i en hendelsesliste det er en «Push» til hendelseslisten. Folkeregisteret tilgjengeliggjør hendelseslisten for konsument og hendelsene i listen har en avtalt levetid.
   - **Behov**: Konsumentene ønsker selv å styrere sekvens på lesing og hvor mange hendelser konsumenten skal lese. Samme hendelser kan leses av flere systemer hos konsumentene og man kan lese hendelser så mange ganger man ønsker. Konsumentene må selv holde orden på en intern feed-peker som viser hvor langt man har lest i hendelseslisten. Det er behov for at konsument kan gjøre en «Pull» av hendelsene i hendelseslisten for å oppdatere sin tjeneste.

#### Behov for tilgangsstyring ved deling av hendelser

På samme måte som ved deling av data vil tilgang til å abonnere på gitte typer hendelser, kreve god tilgangsstyring. Aktører som kun deler data kun med de som har hjemmel til å behandle dataene, vil på samme måte også kreve at det er avtaler som ligger til grunn for a abonnere på en hendelsestype. Det er i disse tilfellene behov for at tilbyder og konsument kjenner til hverandre og inngår nødvendige avtaler. En mekanisme for hendelseshåndtering må støtte tilgangsstyring, og fellesløsningene for tillitstjenester vil spille en viktig rolle i dette.

### Knytning til de overordnede arkitekturprinsippene

De overordnede nasjonale arkitekturprinsippene ligger også til grunn for en beste praksis for «Arkitektur for hendelser i felles økosystem»:

**Ta utgangspunkt i brukernes behov (Prinsipp 1)**  
*For hendelsesdrevet arkitektur ivaretas dette gjennom*:  
Tjenestekjeder kan utvikles organisk, og tilpasse seg brukers behov uten endring av eksisterende tjenester.

*Beskrivelse*:  
Ved å basere tjenestene på hendelser i en aktørs livssyklus vil tjenestekjeden kunne tilpasses individuelt. En hendelse kan føre til behov for en tjeneste, tjenesten bruker og fører til endring i data. Endring i data kan føre til en ny hendelse som igjen fører til behov for en tjeneste. En tjeneste kan bruke resultatet fra en eller flere andre tjenester.

**Lag digitale løsninger som støtter samhandling (Prinsipp 6)**

*For hendelsesdrevet arkitektur ivaretas dette gjennom:*  
Hendelser vil bidra til samhandlingsevne på tvers av virksomheter, sektorer, fagområder og bransjer og støtte distribuerte arkitekturer.

*Beskrivelse*:  
Ved å basere tjenestene i en tjenestekjede på hendelser vil hver enkelt tjenestetilbyder kunne optimalisere sin tjeneste uavhengig av de andre tjenestetilbyderne. Endring i en tjeneste vil ikke påvirke de andre tjenestene i kjeden.

**Standardiserte beskrivelser (Prinsipp 6, anbefaling 6.6)**  
*For hendelsesdrevet arkitektur ivaretas dette gjennom:*  
Hendelser og tjenester skal beskrives på en standardisert maskinlesbar måte.

*Beskrivelse*:  
Ved å beskrive hendelser og tjenester etter gjeldende standarder og tilgjengeliggjøre beskrivelsene i en hendelse- og tjeneste-katalog, vil andre kunne oppdage og gjenbruke tjenester i en tjenestekjede. Tjenester vil kunne tilbys basert på hendelser/resultater fra andre tjenester.

**Del og gjenbruk løsninger (Prinsipp 5)**  
*For hendelsesdrevet arkitektur ivaretas dette gjennom:*  
Tjenester er autonome, de kan tilbys selvstendig eller i en tjenestekjede.

**Minst mulig avhengighet (Prinsipp 5, anbefaling 5.7)**  
*For hendelsesdrevet arkitektur ivaretas dette gjennom:*  
Sikre at det er minst mulig avhengighet mellom tilbyder og konsument, og at tjenestene er løst koblet.

*Beskrivelse*:  
«Konsument» og «Tilbyder» av hendelser trenger ikke vite om hverandre. Utveksling av informasjon skjer uten direkte integrasjon. Mange konsumenter kan få tilgang til hendelser uten at tilbyder er involvert. Konsumenter kan selv kople seg opp ved å abonnere på gitte hendelsestyper (som de har tilgang til).

Arkitektur for hendelser i felles økosystem
