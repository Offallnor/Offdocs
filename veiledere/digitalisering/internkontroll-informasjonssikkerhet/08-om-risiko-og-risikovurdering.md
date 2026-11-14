---
veileder: "Internkontroll i praksis – informasjonssikkerhet (versjon 2.0)"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/informasjonssikkerhet/om-risiko-og-risikovurdering/3048"
hentet: "2026-11-14"
---

# Om risiko og risikovurdering

For å jobbe effektivt med risiko og risikostyring, må man ha en god forståelse av hva det handler om. Her forklares sammenhengene mellom risiko, risikostyring og risikovurderinger.

Opprettet: 22. november 2021

Sist endret: 10. januar 2024

## 1. Hva er risiko?

Risiko er et abstrakt begrep vi benytter for å gjøre vurderinger om fremtiden. Risiko er knyttet til mulige avvik fra våre mål. Det blir også kalt mulige avvik fra ønskede resultater eller ønskede tilstander.

Med det som utgangspunkt beskrives risiko ofte som en kombinasjon av mulige konsekvenser (utfall eller resultat) og tilhørende usikkerhet.

Usikkerhet angis ved hjelp av sannsynligheter. Vi sier derfor ofte at risiko er kombinasjonen av (mulige) konsekvenser og (tilhørende) sannsynligheter, eller bare at risiko er kombinasjonen av konsekvens og sannsynlighet. Ordene i parentes er ofte underforstått og utelatt, slik som i entallsformen i siste del av uttrykket.

Selv om de vanlige definisjonene innebærer at risiko kan være både negativ og positiv, er det i forbindelse med informasjonssikkerhet mest vanlig å kun rette søkelyset på det negative, og på uønskede hendelser. Det har vi også valgt å gjøre i dette veiledningsmateriellet.

Det finnes flere definisjoner og beskrivelser av risiko, men de fleste er bygd rundt den samme kjernen. Digitaliseringsdirektoratet legger til grunn den internasjonale definisjonen i ISO Guide 73:2009, som benyttes i NS-ISO/IEC 27001.

## 2. Hva er risikostyring?

Når man har en risikobasert tilnærming til måloppnåelse, inkludert å sørge for tilstrekkelig informasjonssikkerhet for virksomhetens oppgaver og tjenester, så er risikostyring verktøyet man benytter i arbeidet.

Arbeidet med informasjonssikkerhet handler i hovedsak om «operasjonell risiko» – hva som kan skje i gjennomføring av oppgaver og leveranse av tjenester. Risikostyring og internkontroll er da i praksis det samme.

Risikostyring på operasjonelt nivå i virksomheten er det samme som arbeidet med internkontroll

Direktoratet for forvaltning og økonomistyring

Du kan lese mer om [sammenhengen mellom internkontroll og risikostyring på DFØs nettsider](https://dfo.no/fagomrader/risikostyring/sammenhengen-mellom-risikostyring-og-internkontroll).

ISOs risikoterminologi beskriver risikostyring som “coordinated activities to direct and control an organization with regard to effect of uncertainty on objectives”. ISO beskriver “management system” som “set of interrelated or interacting elements of an organization to establish policies and objectives and processes to achieve those objectives”. Vi sier derfor gjerne at når det handler om informasjonssikkerhet så er internkontroll, risikostyring og styringssystem i praksis det samme. Og at styringssystemet er ledelsens redskap for å oppnå tilstrekkelig styring og kontroll.

Kjernen i styringssystemet – og «processes to achieve those objectives” – er de styringsaktivitetene som beskrives i dette veiledningsmateriellet.

## 3. Risikoforståelse

### 3.1 Risikomodeller

Vi benytter risikomodeller for å skaffe oss evne til å resonnere om risiko. Man ser ofte på flere elementer for å forstå og vurdere risiko. En risikomodell beskriver disse elementene, og sammenhengene mellom dem. Man trenger dette for å kunne arbeide med, forstå og vurdere risiko. Man kan vurdere de ulike elementene og gjøre en samlet vurdering av risiko.

Risikomodeller kan være enkle eller komplekse. De kan være generelle eller spesielle, og tilpasset ulike bruksområder.

Slike modeller inneholder alltid mer enn konsekvens og tilhørende sannsynlighet. For eksempel beskriver vi ofte risikoer ved å referere til mulige hendelser. Dette gir et helhetsuttrykk for risiko som dekker både det utløsende (mulig hendelse) og selve risikoen (mulig konsekvens og tilhørende sannsynlighet).

Et eksempel på en slik modell er illustrert i figur 3 i kapittel 2 i[NIST 800-30 rev 1 Guide for Conducting Risk Assessments](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final):

Den generiske risikomodellen som NIST beskriver er ganske kompleks. Den bruker for eksempel flere ulike sannsynligheter, for forskjellige ting. Det finnes andre mer komplekse modeller. Avanserte brukere, med komplekse behov, vil kunne finne nytte i den som er i [IRAM2 fra ISF](https://www.securityforum.org/solutions-and-insights/information-risk-assessment-methodology-2-iram2/)**.**

Metoden for vurdering av risiko som er beskrevet i dette veiledningsmateriellet benytter en enklere modell, som vil dekke behovet til de aller fleste.

### 3.2 Konsekvensens sannsynlighet

Dersom man benytter en risikomodell med bare én sannsynlighet, så bør den knyttes til konsekvensen. Man beskriver konsekvens og tilhørende sannsynlighet.

En mulig hendelse kan få mange ulike konsekvenser med ulik sannsynlighet. Når vi skal uttrykke sannsynlighet, så er det ikke nok å estimere sannsynligheten for at den utløsende hendelsen skal inntreffe. Estimatet av sannsynlighet må også dekke at den konsekvensen vi har valgt å se på, faktisk blir utfallet av hendelsen. Det er da hendelse, konsekvens og sannsynlighet kan gi en god beskrivelse av risiko.

Dette har mindre betydning dersom vi alltid konsentrerer oss om den mest trolige eller forventede konsekvensen av en hendelse, og dette er den klart mest sannsynlige konsekvensen. Det har imidlertid større betydning dersom vi ser på den potensielt verste eller beste konsekvensen, som begge kan være sjeldne og lite sannsynlige konsekvenser av en hendelse.

Hvilke typer konsekvenser en ønsker eller er pålagt å beskrive og formidle, kan i en del sammenhenger gjøre det naturlig å synliggjøre flere risikoer ved den samme hendelsen. Dette kan være både den mest trolige eller forventede konsekvensen med tilhørende sannsynlighet og den potensielt verste konsekvensen med tilhørende sannsynlighet. En slik presentasjon gir en spennvidde i beskrivelsen av risiko som enkelte beslutningstakere ønsker å få.

### 3.3 Negative og positive konsekvenser

Det har i risikoarbeid tradisjonelt vært vanlig å bare legge vekt på uønskede hendelser og negative konsekvenser. De fleste veiledninger og verktøy for vurdering av risiko har denne tilnærmingen.

I ISO-standardene og i en del andre sammenhenger blir også mulige positive konsekvenser inkludert i risikobegrepet. Risiko handler da om usikkerhet rundt måloppnåelse generelt. Usikkerheten kan være påvirket av både trusler og muligheter og dermed gi både negative og positive resultater i henhold til målet.

#### Forskjell i ulike fagmiljø

I noen fagmiljø, for eksempel innen samfunnsøkonomi og enkelte prosjektmetoder, legges det kun vekt på negative konsekvenser når de snakker om risiko. Risiko blir da motpol til muligheter, og analysen som omfatter begge kalles ofte usikkerhetsvurdering i stedet for risikovurdering.

Forskjellen handler i realiteten om terminologi og har liten praktisk betydning. En virksomhet som tar for seg både positive og negative konsekvenser, bør imidlertid vurdere å etablere en ensartet terminologi internt.

#### Fokus i dette veiledningsmateriellet

Det finnes per i dag lite av godt utbredte og anerkjente veiledninger og verktøy for å arbeide med «positive risikoer» innen informasjonssikkerhet. Informasjonssikkerhetsbrudd er stort sett alltid en uønsket hendelse som gir negative konsekvenser. Vi har derfor valgt å ikke se på positive risikoer i dette veiledningsmateriellet.

Ved risikoer som er så store at virksomheten kanskje bør vurdere å ikke utføre aktiviteten for å unngå risikoen, må beslutningstaker imidlertid vurdere risikoene ved aktiviteten opp mot nytten av aktiviteten. En slik vurdering vil være en variant av vurdering av muligheter eller positive risikoer.

## 4. Vurdering av risiko

### 4.1 Prosess

Risikovurdering er et begrep i risikostyringen som dekker de tre stegene

- identifisere risiko
- analysere risiko
- evaluere risiko

Det kan også kalles risikoidentifisering, risikoanalyse og risikoevaluering.

Dette er en begrepsbruk som er forankret i den internasjonale standarden NS-ISO 31000 «Risikostyring». NS-ISO/IEC 27001, som dette veiledningsmateriellet baserer seg på, bygger på og refererer til denne overordnede risikostyringsstandarden.

Under følger en generell beskrivelse av hovedinnholdet i de tre stegene i en risikovurdering.

#### Identifisere risiko

Det første steget i risikovurderinger kalles identifisere risiko. Formålet er å lage en omfattende liste over mulige hendelser som kan føre til negative konsekvenser for vår evne til å utføre oppgaver og tjenester, ivareta våre plikter og økonomi.

Som en innledende del av identifiseringen av risiko ser en gjerne også på mulige risikokilder, områder som berøres og lignende. Innenfor informasjonssikkerhet er det vanlig å identifisere og vurdere trusler, farer og sårbarheter som en innledende del. Lignende skjer også på andre fagområder.

#### Analyse av risiko

Det andre steget i risikovurderingen er analyse av risiko. Det handler om å utvikle en forståelse av risikoene. Formålet er å kunne fastslå mulig konsekvens og tilhørende sannsynlighet på hendelser identifisert i forrige steg. Dette gir en god beskrivelse av risiko.

Analysen omfatter en vurdering av både årsakene og kildene til hendelsene, hvilke konsekvenser de kan få, samt sannsynligheten for at disse konsekvensene skal forekomme.

##### Ulike konsekvenser med ulik sannsynlighet

I praksis vil en uønsket hendelse kunne ha mange forløp og kunne få mange ulike konsekvenser med hver sine sannsynligheter. Dette er illustrert ved hjelp av den blå streken i figuren under. Hvor den blå streken faktisk går, er avhengig av hvor stramt eller løst konsekvensene er spesifisert i risikobeskrivelsen. Den blå streken vil dermed ha ulik utforming for ulike risikobeskrivelser. Den vil også ofte ha ulik utforming i ulike konsekvenskategorier for en og samme risikobeskrivelse.

Å velge ett konsekvensnivå i en risikomatrise er derfor en forenkling. Det er også en forenkling å primært velge det mest forventede konsekvensnivået. Tilnærmingen som i dette veiledningsmateriellet er beskrevet i trinnet analysere, er imidlertid akseptabel siden formålet i denne sammenheng er å finne det høyeste risikonivået. Det er det vi trenger for å evaluere risikoer i neste trinn i risikovurderingen.

Det er imidlertid viktig at man er bevisst de egentlige sammenhengene, og at man forenkler. Man bør være tydelig på det i kommunikasjonen med risikoeier, systemeier fellessystem og andre, slik at de også vet det. Det kan ha betydning for deres beslutninger. Det er også viktig å være klar over det når man senere skal håndtere risikoene.

#### Evaluering av risiko

Det tredje steget i risikovurderingen er evaluering av risiko. Formålet er å gi støtte til beslutninger om hvilke risikoer som må håndteres, og hvilken prioritet håndteringen av dem bør gis.

Det går ut på å sammenligne risikonivået som ble avdekket i analysen av risiko i steget foran, med kriterier for å akseptere risiko. Dette er kriterier ledelsen har besluttet og gitt som føringer for arbeidet.

### 4.2 Overgang til håndtering av risiko

Håndtering av risiko omfatter å velge ett eller flere alternativ for å håndtere risikoer som er for høye, og deretter iverksette disse alternativene og tilhørende tiltak.

Håndtering av risiko er et hovedsteg i risikostyringen på linje med vurdering av risiko. I praksis er det imidlertid ikke alltid et like klart skille mellom vurdering og første del av håndteringen, det vil si å lage forslag til alternativ eller tiltak for å håndtere risiko.

I mange praktiske sammenhenger og veiledninger blir denne første delen av håndteringen inkludert i det som kalles risikovurdering. Grunnen er nok at oppdraget med å gjennomføre risikovurderinger ofte også inkluderer et tilleggsoppdrag om å foreslå hvordan risikoer bør håndteres, inkludert relevante risikoreduserende tiltak.

### 4.3 Uttrykke usikkerhet om vurderingene

Risikovurderinger er kunnskapsbaserte og uttrykker våre vurderinger om noe i fremtiden. Når vi vurderer mulige hendelser, mulige konsekvenser og deres sannsynligheter, bygger vurderingene på den kunnskapen vi har fra før, og den vi etablerer underveis i arbeidet. Vurderingene blir selvsagt også preget av mangelen på kunnskap. Hvor god er forståelsen vår av hendelsene som vurderes, og hvor gode grunnlagsdata har vi? Denne delen av usikkerheten kan det være viktig eller nyttig å si noe om når vi presenterer resultatene fra risikovurderingen.

Det er vanlig å gi en tilleggsbeskrivelse av hvor usikre vi er på estimeringen av risikoen, det vil si usikkerheten ved anslagene for konsekvens og tilhørende sannsynlighet.

#### Hvordan uttrykke usikkerhet

Ofte benyttes enkle graderinger som stor, middels eller lav usikkerhet. Disse kan kobles direkte til hver enkelt risiko. Alternativt kan usikkerhetsnivåene omtales samlet og mer generelt for flere risikoer i et risikovurderingsnotat eller en rapport.

Innsats for å uttrykke usikkerhet ved hver enkelt risiko må ses i et kost/nytte-perspektiv. På kritiske områder kan det være viktig, mens det på andre områder kan bli for detaljert. Å gi en kort oppsummering av usikkerheten ved vurderingene samlet vil alltid være et positivt bidrag i all kommunikasjon om risiko.

#### Kunnskapsstyrke

Man kan også se på det som at *kunnskapsstyrke* er et uttrykk for hvor god bakgrunnskunnskap man har når man vurderer en risiko og estimerer mulig konsekvens og tilhørende sannsynlighet. Det kan være hensiktsmessig å gradere kunnskapsstyrken i kategoriene svak, medium og sterk. Nivået man setter på kunnskapsstyrken bør samsvare med den usikkerhet man har rundt estimatene i vurderingene.

Risikovurderinger er beslutningsgrunnlag. Informasjon om kunnskapsstyrke kan da være viktig for å ta gode beslutninger.

### 4.4 Alternativ begrepsbruk

I noen fagmiljø og sammenhenger brukes begrepet «risikoanalyse» på hele risikovurderingsprosessen og ikke bare på det midterste av de tre stegene i risikovurderingen, slik ISO-standardene og vi bruker begrepet.

En slik alternativ eller utvidet bruk av begrepet «risikoanalyse» er spesielt vanlig når noen snakker om enkeltstående risikovurderinger som ikke inngår i en helhetlig risikostyringsprosess, slik vårt veiledningsmateriell her gjør innen informasjonssikkerhet.

Innholdsmessig er det ingen vesentlig forskjell i arbeidet som skal gjøres om en kaller hele prosessen risikovurdering eller risikoanalyse. I begge tilfeller velges og brukes ulike metoder avhengig av problemstillingen som skal vurderes og analyseres. Og i begge tilfeller blir risikoer identifisert, analysert og evaluert.

Noen fagmiljø bruker begrepet «risiko- og sårbarhetsanalyse (ROS)» på hele risikovurderingsprosessen, gjerne inkludert første del av risikohåndteringen. «Sårbarhet» er ofte et element i en risikomodell, sammen med mange andre, og er ikke sidestilt med «risiko», men inkludert i «risiko». Vi benytter derfor ikke «ROS»-begrepet i dette veiledningsmateriellet. Sårbarhet er en faktor som påvirker all risiko, og som derfor alltid, i større eller mindre grad, bør være en del av analysen i en risikovurdering.
