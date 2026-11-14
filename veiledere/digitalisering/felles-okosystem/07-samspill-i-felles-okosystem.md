---
veileder: "Felles økosystem"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/digital-samhandling/samspill-i-felles-okosystem/4693"
hentet: "2026-11-14"
---

# Samspill i felles økosystem

Opprettet: 15. juni 2023

Sist endret: 01. november 2024

Økosystem for nasjonal digital samhandling og tjenesteutvikling er en måte å samhandle på, og en samling verktøy og løsninger som flere kan bruke for å utvikle digitale tjenester. Dette skal bidra til at offentlige tjenester oppleves som sammenhengende for brukerne, uansett hvilken offentlig virksomhet som tilbyr dem. Hvor godt de ulike delene av økosystemet samhandler, har stor betydning for hvor gode og trygge digitale løsninger som skapes og tilbys oss som innbyggere.

Hendelser er data som må kunne utveksles mellom aktørene i Felles Økosystem, slik at vi oppnår bedre samhandling. Løse koplinger gir færre bindinger mellom aktørene, men heller ikke Hendelsesdrevet arkitektur er skånet for bindinger man må vurdere.

### Semantisk Interoperabilitet

Semantisk interoperabilitet er «evnen til å virke sammen, utveksle informasjon og til å bruke informasjonen som er utvekslet», og er viktig for deling av data, herunder hendelsesdata.

For å beskrive tjenester og hendelser, samt kunne utveksle beskrivelsene på tvers av landegrenser har EU utarbeidet CPSV-AP. Basert på denne har vi i Norge etablert applikasjonsprofilen [CPSV-AP-NO](https://data.norge.no/specification/cpsv-ap-no). Beskrivelser av hendelser og tjenester som virksomhetene publiserer finnes på [data.norge.no](https://data.norge.no/nb/catalogs/public-services-and-events)

Viser hvordan cpsv-ap-no støtter tjenestekjeder

For å beskrive tjeneste er det en rekke obligatoriske felt, blant annet beskrivelse, navn, identifikator, kontaktpunkt og tjenesteresultat (som kan inngå i et datasett). Som figuren over viser er tjenesteresultat, eller endringen i data, det som utløser en hendelse.

For å beskrive hendelse må navn og identifikator dokumenteres. I tillegg anbefaler vi sterkt å dokumentere type hendelse. Les mer i selve spesifikasjonen om alle obligatoriske, anbefalte og valgfrie opplysninger: [CPSV-AP-NO](https://data.norge.no/specification/cpsv-ap-no)

CPSV-AP-NO dekker metadata og ikke data, og kan benyttes for å designe tjenestekjeder. Selve hendelsesobjektene inngår som en del av teknisk interoperabilitet og beskriver hver enkelt hendelse som kan inngå i en operative kjede. I tillegg trengs det mekanismer og tekniske løsninger for å utføre selve utvekslingen av hendelsesobjektene.

### Teknisk Interoperabilitet

«Den tekniske evnen to eller flere løsninger eller applikasjoner har til å utveksle og bruke informasjon, evnen til å tilby og konsumere tjenester fra andre systemer, og å bruke tjenestene som utveksles slik at systemene arbeider effektivt sammen» (https://data.nav.no/begrep/BEGREP-540)

Informasjon om oppståtte hendelser må kunne utveksles mellom aktørene i Felles Økosystem. Det vil være behov for mekanismer for å publisere og gi tilgang til hendelser, for både «store og små». Løsninger på tvers av virksomheter og domene må fungere sammen. I Norge har vi fellesløsninger, både nasjonale og sektorielle som kan eller skal kunne gjenbrukes.

Ulike alternative tilnærming:

1. Sentralisert arkitektur
2. Desentralisert arkitektur
3. Gjenbruk og desentralisert

Gjenbruk og desentralisert er den tilnærmingen som vil bidra til at flest mulig aktører kan bidra til at hendelser kan utveksles på tvers uavhengig av modenhet hos de ulike aktører. Her vil aktører kunne fungere i et samspill der man er enig om en felles beste-praksis. Virksomheter kan implementere egne løsninger for Hendelseshåndtering som fungerer i felles økosystem eller gjenbruke en felles løsning. Illustrasjonen under viser dette samspillet.

Gjenbruk og desentralisert tilnærming

Et eksempel på en gjenbrukbar løsning vil være «Altinn Events». En gjenbrukbar løsning som Altinn Events er en fellesløsning som kan benyttes direkte i Altinn plattformen, eller at man gjenbruker koden og kjører den på egen plattform.

#### Utveksling av hendelser i distribuerte system

For å øke teknisk interoperabilitet for utveksling av hendelser er det behov for å se på mulige felles spesifikasjoner. Et eksempel på dette er Cloud Events-spesifikasjonen (https://cloudevents.io/)

Målet med CloudEvents-spesifikasjonen er å definere interoperabilitet av hendelsessystemer som lar tjenester tilby eller konsumere hendelser uavhengig av hverandre. CloudEvents-spesifikasjonen er fokusert på interoperabilitet av hendelsesformatet og hvordan det formateres, men at det kan sendes på ulike protokoller, for eksempel HTTP.

Det finnes ulike løsninger for publisering av hendelser fra ulike leverandører, og enhver virksomhet vil gjøre ulike valg for egen løsningsarkitektur utifra ulike behov, drivere og rammebetingelser. Større systemleverandører som for eksempel AWS, Microsoft, Google har løsninger som publiserer hendelser i ulike formater. Dette øker behovet for en felles og normaliserende spesifikasjon ved utveksling av hendelser, slik som for eksempel CloudEvents-spesifikasjonen. Vi vil da unngå at konsumenter av hendelser må implementere særskilt logikk mot den enkelte tilbyder av hendelser.

Eksempel på hendelsesobjekt i CloudEvents-spesifikasjonen.

Eksempler på behov og scenarier
