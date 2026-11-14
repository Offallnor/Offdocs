---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/kartlegg-datakilder"
hentet: "2026-11-14"
---

# 2. Samle inn data

1. [Kartlegg datakilder](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/kartlegg-datakilder)
2. [Samle inn data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/samle-inn-data)

## Kartlegg datakilder

Finn ut hvilke kilder du kan hente data fra. Du kan bruke data du samler inn selv, for eksempel brukerdata og kundedata, eller hente data fra andre hvis det er nødvendig for formålet.

Hvis du henter data fra kun én kilde risikerer du at systemet lærer mønstre som er spesifikke for den kilden, ikke for virkeligheten systemet skal brukes i. For å redusere denne risikoen bør du

- ha oversikt over hvor dataene kommer fra og bruk data fra flere ulike kilder
- vurdere om kildene representerer den populasjonen systemet faktisk skal brukes på
- undersøke om noen grupper er over- eller underrepresentert
- avklare hvem som eier og forvalter dataene
- vurdere kvalitet og frekvens for oppdatering

### Bruk autoritative kilder når du kan

Det finnes to hovedtyper data:

- Autoritative kilder er den opprinnelige og mest pålitelige kilden til dataene.
- Kopierte eller flyttede data er hentet fra annen kilde og lagret på nytt.

Når data vi kopierer eller flytter data øker risikoen for feil, at datene ikke blir oppdaterte eller at vi mister informasjon. Hvis dataene kopieres til andre systemer må du fortsatt sikre at de er oppdaterte og korrekte.

### Obs! KI trenger godt strukturerte data

For å gjøre KI-systemer mer presise og pålitelige må dataene settes inn i en tydelig struktur som gir felles begreper og sammenhenger.

​[Begrepsmodeller er et verktøy for å gi data struktur](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/kartlegg-datakilder/begrepsmodeller)

Strukturerte og ustrukturerte data

Noen data er allerede samlet inn og bearbeidet for eksempel i registre som helseregistre, offentlige databaser og åpne datakilder. Slike kilder er ofte strukturerte, det vil si organisert i faste formater (modeller) og godt dokumentert.

Andre data kan være mer ustrukturerte, for eksempel data fra logger eller fritekst. Slike data kan mangle en fast struktur og krever gjerne mer bearbeiding før de kan brukes i et KI-system.

Det kan være nødvendig å organisere ustrukturerte data ved å merke innhold. Det gjør det enklere å finne riktige data.

### Eksempel

Et smart vanningssystem vil kombinere flere typer data fra ulike kilder:

- Egne sensorer måler jordfuktighet, temperatur og luftfuktighet, ofte rådata som må bearbeides.
- Eksterne kilder som værdata fra værtjenester, ofte strukturerte og klare til bruk.
- Fagdata som informasjon om plantetyper og vanningsbehov, kan være strukturert eller tekstbasert.

Sensorer og værtjenester kan være eksempel på autoritative kilder.

[Neste stegSamle inn data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/samle-inn-data)
