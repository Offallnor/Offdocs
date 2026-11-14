---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/teknisk-dokumentasjon/dokumentasjon-av-datasett"
hentet: "2026-11-14"
---

# Dokumentasjon av datasett for ansvarlig KI

For å sikre tilstrekkelig transparens, sporbarhet og etterprøvbarhet bør du sytematisk dokumentere datasett som brukes til trening, testing eller evaluering av KI-systemer.

En anerkjent metode for å dokumentere datasettdokumentasjon er Datasheets for datasets. Det er systematisk dokumentasjon som tilsvarer tekniske spesifikasjoner for produkter. Metoden gir en strukturert mal for å dokumentere datasettets opprinnelse, sammensetning, innsamling, vedlikehold, anbefalt bruk og begrensninger. Formålet er å gjøre det mulig å vurdere om dataene er egnet for den tiltenkte bruken og å redusere risikoen for feil bruk av data med ukjent eller utilstrekkelig dokumentert bakgrunn.

## Hvorfor er dokumentasjon av datasett viktig?

Forskning viser at manglende dokumentasjon av datasett er en av hovedårsakene til feil og skjevheter i KI-systemer. For å motvirke dette bør du dokumentere datasett systematisk gjennom hele livssyklusen, inkludert hvordan dataene er samlet inn, hvilke forutsetninger som ligger til grunn og hva dataene egner seg til. Dette gjør det mulig å vurdere kvalitet, risiko og egnethet, og er en viktig forutsetning for ansvarlig bruk av KI.

Dette er særlig viktig ved bruk av eksterne eller åpne datasett, hvor opprinnelse og datakvalitet ikke alltid er tilstrekkelig dokumentert.

## Prinsipper for god datasettdokumentasjon

Strukturert dokumentasjon av datasett kan bidra til å operasjonalisere sentrale prinsipper for god datastyring i DAMA DMBok, særlig knyttet til:

- datakvalitet
- metadatahåndtering
- datastyring
- sporbarhet

For alle leverandører av KI-modeller for allmenne formål (KIAF) og KI-systemer med høy risiko er dokumentasjon av datasett en viktig del av arbeidet med å oppfylle kravene til datastyring, datakvalitet og teknisk dokumentasjon i KI-forordningen.

Dette bør du dokumentere

Dokumentasjonen bør

- være oppdatert gjennom hele livssyklusen
- beskrive hvilke datastyringstiltak som er gjennomført
- forklare hvordan tiltakene er implementert i praksis
- tydeliggjøre roller og ansvar
- sikre sporbarhet (data lineage) og etterprøvbarhet

For data og datasett bør du som minimum dokumentere

- hvordan sentrale begreper er definert og brukt i datasettene
- hva slags data som er brukt (beskrivelse av datasettene)
- hvor dataene kommer fra og hvordan de er samlet inn
- hvordan dataene er valgt ut og eventuelt filtrert
- hvordan dataene er merket (hvis relevant)
- hvordan dataene er renset og kvalitetssikret
- om datasettet er basert på reelle observasjoner, syntetiske data eller en kombinasjon
- hva som var det opprinnelige formålet med innsamlingen av dataene
- hvilke forutsetninger og antakelser som ligger til grunn for datasettet
- hvilke kjente svakheter, skjevheter eller usikkerheter som finnes i dataene
- hva datasettet ikke er egnet til å brukes til
- hvordan datasettet er dokumentert (for eksempel et datasheet) og hvor denne dokumentasjonen er tilgjengelig
- hvor representativt datasettet er for den tiltenkte bruken
- hvilken versjon av datasettet som er brukt

For systemets ytelse og begrensninger bør du som minimum dokumentere

- hvor godt systemet fungerer (nøyaktighet, presisjon osv.)
- kjente begrensninger, inkludert for ulike grupper
- mulige feil og risikoer, for eksempel knyttet til skjevhet eller diskriminering

For bruk, overvåking og kontroll bør du som minimum dokumentere

- hvordan systemet skal brukes
- hvilke krav som stilles til input-data
- hvordan mennesker kan overvåke og kontrollere systemet
- hvordan resultatene kan tolkes
