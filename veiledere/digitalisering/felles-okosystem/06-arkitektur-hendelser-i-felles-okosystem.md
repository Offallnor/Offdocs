---
veileder: "Felles økosystem"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/digital-samhandling/arkitektur-hendelser-i-felles-okosystem/4692"
hentet: "2026-11-14"
---

# Arkitektur for hendelser i felles økosystem

Opprettet: 15. juni 2023

Sist endret: 14. oktober 2024

Hendelsesdrevet arkitektur er et designparadigme der en tjeneste kjøres etter å ha mottatt en hendelse. Det gjør det mulig å utveksle informasjon mellom distribuerte løsninger på tvers av organisasjoner i tilnærmet sanntid uten komplekse og tette integrasjoner.

Hendelsesdrevet arkitektur er en kjent arkitekturstil brukt i ulike sammenhenger, og er vanlig i bl.a applikasjoner bygget med lettvekts-mikrotjenester. Denne type arkitektur er velegnet i Felles Økosystem (Økosystem for nasjonal digital samhandling og tjenesteutvikling).

«Arkitektur for hendelser i Felles Økosystem» er et grunnlag for å utveksle og agere på hendelser på tvers av virksomheter, domene og tjenester. Det er ikke en teknisk løsningsarkitektur, men vil peke på konseptet og en beste praksis for utveksling av hendelsesinformasjon slik at sammenhengende tjenester kan realiseres.

For enkelte virksomheter vil hendelsesdrevet løsningsarkitektur kunne være nyttig i eget systemlandskap, men vil måtte tilpasses virksomhetens interne prosesser og arkitektur. Vi ønsker derimot å fokusere på bruk av en slik arkitekturstil i forbindelse med utveksling av hendelser mellom virksomheter, domene og tjenester.

### «Hendelsesdrevet arkitektur» i en verden som består av hendelser

Hendelser er noe vi omgir oss med kontinuerlig. Generelt er hendelser ting som «skjer», en endring i tilstand som har oppstått. Alt som skjer i verden deltar eller bidrar således til hendelser. Mennesker og virksomheter er i sin natur hendelsesdrevet, men dette blir for generelt når vi skal lage digitale løsninger.

Digitale løsninger kan også være hendelsesdrevet, men bruker ikke hendelsesdrevet arkitektur i henhold til dets prinsipper. En digital løsning kan tilby eller lagre et hendelsesobjekt, men blir den tilbudt i det øyeblikk hendelsen oppstod? Er det sterke bindinger mellom tilbyder og konsument?

En viktig forutsetning for å skape en best mulig sømløs digital brukeropplevelse for innbyggerne er å gjøre det enkelt for virksomheter å fange opp hendelser som er av betydning for dem. Da blir de i bedre stand til å tilby sine tjenester til rett tid, og vi kan oppnå effekten av sammenhengende tjenester. Når vi snakker om hendelser som er av betydning for en virksomhet, så mener vi tilstandsendringer som har forretningsmessige- eller økonomiske implikasjoner for den relevante virksomheten. Vi kaller dette for virksomhetshendelser. De kan inntreffe både innad i en virksomhet og på tvers av virksomheter.

Hendelsesorientering handler om å betrakte verdenen som en suksessiv kjede med hendelser fremfor et helhetlig og lukket system. Hendelsesorientert tenkning forutsetter at enhver hendelse har en årsak og endres denne årsaken så vil også hendelsen endres tilsvarende. Hendelsesdrevet arkitektur er en arkitekturstil der komponenter og tjenester i en teknisk løsning er hendelsesdrevet. Tilbyder og konsument av hendelse er minimalt koplet sammen kun via hendelser, og konsument agerer på et hendelsesobjekt.

En innbygger har mange betydningsfulle hendelser i livet sitt. Dette kaller vi livshendelser. En hendelsesorientert forvaltning må kunne automatisk plukke opp innbyggernes livshendelser og agere på disse på en hensiktsmessig måte. De fleste virksomheter er hendelsesorienterte, men det er først når de har etablert mekanismer for når- og hvordan de skal produsere- og konsumere hendelser på en standardisert- og strukturert måte, at de virkelig blir hendelsesdrevne. Det er først da de kan vise til å ha på plass en hendelsesdrevet arkitektur.

Felles prinsipper og forståelse for hendelsesdrevet arkitektur er en forutsetning for å dra nytte av denne arkitekturstilen på tvers av ulike virksomheter.

Hendelser er noe vi omgir oss med kontinuerlig på ulike måter

Begrepene i figuren:

**Hendelsesdrevet arkitektur**er en arkitekturstil *der komponenter og tjenester i en teknisk løsning er hendelsesdrevet.* Tilbyder og konsument av hendelse er minimalt koplet sammen kun via hendelser, og konsument agerer på et hendelsesobjekt.

**Hendelser**  
Endring i en tilstand som kan utløse behov for tjenester. En hendelse er «noe som har skjedd».

**Virksomhetshendelser**  
Hendelser som er meningsfullt i en forretnings- eller domenekontekst.

**Livshendelser**  
Hendelser som er meningsfullt i en innbyggerkontekst.

**Hendelsesobjekt**  
Hendelse som er maskinlesbar og formidler informasjon om hvilken endring som har skjedd.

**Hendelsesdrevet**  
Atferden til en aktør som handler når den gjenkjenner en hendelse, fremfor å respondere på kommandoer

### «Hendelsesdrevet arkitektur – logisk»

Utgangspunktet er når en hendelse oppstår i et system som er interessant for andre. «Tilbyder av hendelse» er løst koplet til «Konsument av hendelse» og de trenger ikke vite om hverandre. Det er høy grad av autonomi mellom aktørene, og konsumenter kan få tilgang til hendelser uten at tilbyder er involvert. Det kan være 1, mange eller svært mange aktører som har interesse for en hendelse.

Hendelsesdrevet arkitektur (logisk skisse)

Merk at dette er et logisk nivå. Løsningsmessig kan utveksling av hendelser gjøres på flere måter, avhengig av behov og mønstre for utveksling av hendelser.

Figuren over viser «Tilbyder av hendelse» som representerer en aktør som ønsker å publisere en hendelse på bakgrunn av endringer i en tilstand, enten dette er resultat av en tjeneste eller andre endringer i en datakilde. «Tilbyder av hendelse» publiserer eller lagrer denne endringen i en logisk arkitekturbyggekloss for «Hendelseshåndtering». En slik hendelse må tilgjengeliggjøres for en eller flere «Konsument av hendelse». «Hendelseshåndtering» innebærer ulike kapabiliteter for tilgangsstyring og tilgangskontroll utifra behov og valgt mønster for utveksling av hendelser. En «Konsument av hendelse» som skal være mest mulig løskoplet fra en «Tilbyder av hendelse» vil for eksempel ha behov for å kunne abonnere på relevante hendelser, mest mulig selvbetjent.

#### Begreper knyttet til hendelsesdrevet arkitektur:

**Hendelse**  
Endring i en tilstand som kan utløse behov for tjenester. En hendelse blir sendt ut i det øyeblikk det skjer en endring i tilstand hos «Tilbyder av hendelse», enten dette er endringer i data som resultat av en tjeneste eller endringer i en sammenstilt datakilde.

**Hendelsesobjekt**  
Hendelse som er maskinlesbar og formidler informasjon om hvilken endring som har skjedd, slik at en «Konsument av hendelse» kan forstå og agere basert på informasjonen.

**Tilbyder av hendelser**  
Når en datakilde endres, og endringen(e) er interessante for andre, kan dette tilbys som en hendelse. Hendelsen må publiseres («Push») eller lagres i «Hendelseshåndtering».

**Konsument av hendelser**  
En tjeneste eller løsning som skal agere basert på en eller flere spesifikke hendelser som oppstår. En eller flere konsumenter handler i det øyeblikk en hendelse blir gjenkjent.

**Hendelseshåndtering**  
Mekanisme som sikrer at hendelser er transportert og behandlet riktig mellom «Tilbyder av hendelse» og «Konsument av hendelse». «Tilbyder av hendelse» publiserer hendelsen til denne («Hendelsesinntak»), mens «Konsument av hendelse» får tilgang («Hendelsesuttak»).

Ulike behov og ulike mønstre for utveksling av hendelser krever ulike kapabiliteter i denne. Se mer om dette i kapittel om «Kap. 2.3: Hendelsesmønstre i «Arkitektur for hendelser i Felles Økosystem»

**Hendelsesvarsel**  
En melding til en «Konsument av hendelse» at en spesifikk hendelse har oppstått, og inneholder et hendelsesobjekt konsumenten kan agere på.

**Abonnement**  
De type hendelser en «Konsument» ønsker å få tilgang til. Konsumenter kan selv kople seg opp ved å abonnere på gitte hendelsestyper (som de har tilgang til).

### Hendelsesmønstre

Det vil ikke være én måte og utveksle hendelser på i et felles økosystem. Ulike mønstre for utveksling av hendelser vil dekke ulike behov og scenario. Det vil selvsagt også være særskilte behov som ikke nødvendigvis passer inn i et hovedmønster, som den enkelte virksomhet selv må ta stilling til. Det er allikevel tre hovedmønster som er aktuelle å vurdere innenfor hendelsesdrevet arkitektur. Disse tre er Event notification, Event-carried state transfer og Event sourcing. Vi har valgt å beholde de engelske navnene på hovedmønstrene i mangel av gode norske begreper. I tillegg vil hvert hovedmønster kunne realiseres med to ulike delmønstre for tilgang til hendelsene.

Felles for alle mønstrene er at Tilbyder av hendelse er løst koplet til selve hendelseshåndteringen, og ikke trenger å kjenne til hvilke konsumenter som får tilgang til en hendelse via denne.

#### Hovedmønstre for utveksling av hendelser på tvers av sektorer og tjenester

##### Event Notification

En hendelse representerer en endring som er skjedd i data, og hendelsen publiseres som et hendelsesobjekt fra «Tilbyder av hendelse». Hendelsesobjektet inneholder kun informasjon om «hva som skjedd», ikke innholdet til den enkelte endring. Hendelsesobjektet kan f.eks. være «Adresse endret», som da vil være en hendelsestype en eller flere «Konsument av hendelse» ønsker tilgang til.

Event notification er et hovedmønster som kun gir informasjon at en type endring er skjedd.

*Eksempel på hendelsestype “Adresse endret” fra Folkeregister:*

Eksempel på hendelsesmønsteret "Event Notification"

Dette er et konsistent mønster som deler minimalt med data, og som kan kombineres med oppslag i datakilde i bakkant hvis behov for mer data og ytterligere kontroll på konsumentenes tilganger.

##### Event-Carried State Transfer

En hendelse representerer en endring som er skjedd i data, og hendelsen publiseres som et hendelsesobjekt fra «Tilbyder av hendelse». Hendelsesobjektet inneholder informasjon om «hva som skjedd», i tillegg til innholdet til den enkelte endring. Hendelsesobjektet kan f.eks. være «Adresse endret», som da vil være en hendelsestype en eller flere «Konsument av hendelse» ønsker tilgang til.

Dette mønsteret vil i mindre grad enn «Event Notification» føre til behov for oppslag i bakkant siden dataene om endringen er inkludert i hendelsesobjektet.

Hovedmønster "Event-Carried Transfer" er et mønster der det i tillegg til informasjon om hvilken hendelse som er oppstått også sendes med de data som er endret

Eksempel på hendelsestype “Adresse endret” fra Folkeregister:

Hendelsestype "Adresse endret" fra Folkeregister inneholder også selve adresseendringen

##### Event Sourcing

Det kan diskuteres om dette er et hovedmønster eller ikke, siden «Event sourcing» først og fremst dreier seg om at alle endringer i et system blir lagret i en egen hendelseslogg («Event store»), altså en måte å lagre data på. Det er da mulig å gjenskape et system til et bestemt tidspunkt eller tilstand basert på endringene. En tradisjonell database lagrer data i en bestemt tilstand, mens hendelsesloggen tar vare på endringene. En hendelseslogg vil være persistent til enhver tid og inneholde fakta som er såkalt «immutable», altså fakta som representer sannhet og ikke skal kunne endres i ettertid.

Hendelseslogg er søkbar og kan inneholde øyeblikksbilder av forutbestemte tilstander. Et enkelt eksempel som belyser dette er en bankkonto, med kontotransaksjoner over tid, inkludert øyeblikksbilder pr mnd eller år.

«Event sourcing» er altså ikke direkte knyttet til «Arkitektur for hendelser i Felles økosystem» for utveksling av hendelser mellom eksterne aktører, men mer hvordan en slik hendelseslogg kan benyttes innenfor egen virksomhet.

Det er allikevel viktig å ha med denne som et hovedmønster siden virksomheter som benytter «Event store» kan tilgjengeliggjøre innhold fra denne som en «Hendelsesstrøm» for eksterne konsumenter.

Hendelsesmønster: Event Sourcing

##### Delmønstre for tilgang til hendelsene

###### Delmønster: Meldingsorientert

En hendelse blir sendt som en melding til «Konsument av hendelse», som abonnerer på aktuelle hendelsestyper. Hendelsen blir sendt som en «push» til det endepunktet en konsument har angitt. Mekanismen for hendelseshåndtering må ha kapabiliteter for å sende hendelser til abonnerende konsumenter (publish-subscribe).

- Hendelse sendes til konsument i det den blir publisert av tilbyder
- Konsument av hendelse må kunne motta hendelsen i et egnet endepunkt, f.eks. som en «Webhook URL». Dette innebærer at Konsument av hendelse må implementere et endepunkt en hendelse kan sendes til.
- Hendelseshåndtering må ha kapabiliteter for å sikker og garantert leveranse til riktig konsument.
   - Begrenset levetid til en hendelse siden denne i utgangspunktet fjernes når den er konsumert.
   - Må kunne håndtere situasjoner der konsument ikke er tilgjenglig, eller at feilsituasjoner oppstår
   - Abonnement på hendelser er enten selvbetjent eller kontrollert via tilgangsstyring

Mønsteret vil som nevnt innebære at hendelser blir fjernet etter en viss levetid, og nye abonnementer vil da ikke kunne få tilgang til tidligere hendelser.

###### Delmønster: Hendelsesstrøm

Vil inneholde hendelsene i en logg og støtte persistens av hendelsene som oppstår over tid. Hendelseshåndtering-mekanisme trenger ikke holde på eller midlertidig lagre hendelsene siden disse vil være tilgjengelig som historikk over lengre tid. En Hendelsesstrøm har mye til felles med «Event Sourcing» men med intensjon å utveksle hendelser til eksterne aktører. En Hendelsesstrøm kan realiseres med tanke på utveksling av spesifikke hendelser som er interessante for konsumenter, og kan realiseres med enklere løsninger. F.eks. finnes det eksempler der ATOM feed er brukt til dette. (Folkeregisteret: [https://skatteetaten.github.io/folkeregisteret-api-dokumentasjon/hendelsesliste/](https://skatteetaten.github.io/folkeregisteret-api-dokumentasjon/hendelsesliste/))

- Konsument må selv styre når en hendelse skal leses inn («pull»-modell), og implementere egen løsning for tilgang til hendelsene.
- Hendelseshåndtering må ha kapabiliteter for sikker og garantert leveranse til riktig konsument.
   - Tilgang på hendelser er enten selvbetjent eller kontrollert via tilgangsstyring
- Levetiden til hendelser er lang, siden disse i utgangspunktet ikke fjernes når de er konsumert. Nye konsumenter vil kunne få tilgang til tidligere hendelser.

##### «Push»- eller «Pull»-modell mellom Hendelseshåndtering og konsument av hendelse

I Hendelsesdrevet arkitektur er det et drivende prinsipp at man ønsker minst mulig binding mellom tilbyder og konsument av hendelser. Tilbyder av hendelse vil da publisere en hendelse («push») til en Hendelseshåndterings-mekanisme med intensjon at aktuelle konsumenter vil få tilgang, uten at tilbyder må vite hvem som er konsument(er), eller hvordan og når en konsument agerer.

Dermot vil det fra konsument av hendelse sin side være ulike modeller for tilgang til hendelsen. Hvilken modell man går inn for vil bl.a. være styrt av de behov som er knyttet til tjenesten hendelsen representer, og hvilket delmønster som benyttes.

I en «Pull»-modell må «Konsument av hendelse» selv avgjøre når en hendelse skal leses inn fra Hendelseshåndtering-mekanismen. Dette kan være fra flere ganger i sekundet til f.eks. en gang pr døgn/uke osv. En slik modell vil f.eks. være egnet hvis det ikke er tidskritisk for når en hendelse blir agert på av «Konsument for hendelse». Modellen er også mest egnet i delmønster der man benytter «Hendelsesstrømmer» fremfor «Meldingsorientert».

Utveksling av hendelser fra en tilbyder kan gjøres som en "PULL"

I en «Push»-modell vil «Konsument for hendelse» få en melding om hendelsen direkte i det øyeblikk en hendelse blir publisert til «Hendelseshåndtering». Modellen er f.eks. egnet til de tilfeller det er tidskritisk at en «Konsument for hendelse» får beskjed så snart som mulig at en hendelse har inntruffet.

Utveksling av hendelser fra en tilbyder kan gjøres som en "PUSH".

I tillegg må man vurdere om det er behov for kvittering fra Konsument, altså hvilke avhengigheter man må innføre med hensyn til behov for kontroll på verdikjeden.

##### Virksomhetens behov vil kreve ulike realisering innenfor mønstrene

De ulike mønstrene må ses i sammenheng med varierende behov, som vil påvirke realisering i den enkelte virksomhet. «Arkitektur for hendelser i Felles Økosystem» skal først og fremst bidra til at tjenester kan utvikles, forvaltes og være sammenhengende på tvers av ulike domener, sektorer og virksomheter. Hendelsesdrevet arkitektur bidrar til løse koplinger og autonome tjenester som er en premiss for dette.

Dette er ikke en uttømmende liste, men eksempler på vurderinger som uansett må gjøres ifb. realisering av en løsningsarkitektur, men en realisering innenfor den enkelte virksomhet må ta hensyn til bl.a.:

- Sanntidsbehov og konsistens
   - Hvor tidskritisk er det at Konsument får tilgang til en hendelse i det den oppstår?
   - Det vil alltid være en viss forsinkelse fra en hendelse blir publisert til den blir lest av en eller flere Konsumenter.
- Kontroll på verdikjeden hendelsene er en del av
   - Hvilke avhengigheter er det behov for mellom aktører i verdikjeden eller tjenestekjeden?
   - Kompleksitet: Sporbarhet i verdikjeden kan bli vanskeligere i en hendelsesdrevet arkitektur, som av natur er distribuert og svært løst koplet. En aktør i en større verdikjede av autonome tjenester må vurdere behovet for evt kontroll og oversikt.
   - Evt behov for kvitteringer og statusinformasjon fra Konsument sett fra Tilbyder eller Hendelseshåndtering sin side?
- Persistens av hendelser
   - Skal Hendelser kunne benyttes senere, at den ikke forsvinner i det øyeblikk den mottas av Konsument? Konsument kan ha behov for tilgang til hendelsen i en gitt tidsperiode, f.eks. i en feilhåndteringssituasjon eller i mer forretningsmessige behov.
- Er det få, noen, mange eller svært mange aktuelle Konsumenter av en hendelse?
- Tilgangsstyring
   - Skal hendelsene kun være tilgjengelig for spesifikke Konsumenter eller ikke?
- Behov for å kombinere Hendelsedrevet arkitektur med andre arkitekturstiler?
   - For at en Konsument skal kunne agere etter en intensjon av en hendelse kan det være behov for e-Oppslag i bakkant, spesielt hvis man bruker hovedmønster «Event notification» og det er behov for mer konsistente data.
- Kompensering
   - Er det behov for å endre på historikk eller feil i en transaksjon i en verdikjede? Vil være mer aktuell i en intern løsningsarkitektur (basert på microservices), innenfor en sektor, domene eller virksomhet, med interne bindinger. Men verdt å nevne hvis dette allikevel er aktuelt i en evt. tjenestekjede. Se: [https://microservices.io/patterns/data/saga.html](https://microservices.io/patterns/data/saga.html)

Samspill i felles økosystem
