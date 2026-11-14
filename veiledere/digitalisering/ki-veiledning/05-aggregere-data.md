---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/aggregere-data"
hentet: "2026-11-14"
---

# 3. Forberede data til bruk

1. [Måle og forbedre datakvalitet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/male-og-forbedre-datakvalitet)
2. [Transformere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/transformere-data)
3. [Aggregere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/aggregere-data)
4. [Velge ut data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/velge-ut-data)
5. [Lage og velge relevante egenskaper](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/lage-og-velge-relevante-egenskaper)
6. [Berike data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/berike-data)
7. [Merke data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/merke-data)
8. [Analysere skjevhet i data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data)
9. [Gjøre data tilgjengelig for KI-systemet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/gjore-data-tilgjengelig-for-ki-systemet)

## Aggregere data

For å forstå mønstre i dataene kan det være nødvendig å gruppere dem. Det er det vi kaller å aggregere data. Det gjør det enklere å ta beslutninger samtidig som tilfeldige variasjoner i enkeltmålinger får mindre betydning. Da kan du analysere egenskaper ved grupper i stedet for enkeltobservasjoner.

Du kan for eksempel:

- Aggregere data fra individnivå til grupper. For eksempel fra enkeltpasienter til antall pasienter per diagnose per måned.
- Fra enkeltresultater på prøver til gjennomsnitt per skole eller trinn.
- Fra enkeltreiser til totalt antall reiser per dag eller per rute.

Behold data på et detaljert nivå og lag aggregerte visninger ved behov. Hvilket nivå du bør bruke avhenger av hva KI-systemet skal brukes til. For grovt nivå kan skjule viktige forskjeller, mens for detaljert nivå kan gi for lite datagrunnlag.

Velg derfor et nivå som gir godt grunnlag for analyse og beslutninger.

### Slik aggregerer du data

1. Finn ut hvilket gruppenivå du trenger å analysere data på.
2. Velg hva du vil gruppere data etter, for eksempel per trinn, per skole, per kommune.
3. Bestem hvordan du vil oppsummere dataene, for eksempel gjennomsnitt, sum eller antall.
4. Grupper de originale dataene etter karakteristikkene du har valgt. Beregn måltall, for eksempel gjennomsnitt, sum, antall, for hver gruppe og bruk dette som datasett for KI-systemet.
5. Dokumenter hvordan du har laget aggregeringene slik at det er sporbart og lett å forstå for andre.

### Eksempel

Vanningssystemet mottar målinger av jordfuktighet hvert 10. minutt fra flere sensorer i et område. I stedet for å bruke hver enkelt måling direkte kan dataene aggregeres:

- Per time: beregne gjennomsnittlig jordfuktighet per time.
- Per område (sone): slå sammen data fra flere sensorer til ett gjennomsnitt for hele området.
- Per dag: beregne totalt vanningsbehov basert på gjennomsnitt og værdata.

For eksempel:

- Sensor A: 20 %, 22 %, 21 %
- Sensor B: 18 %, 19 %, 20 %

Gjennomsnitt for området: ca. 20 %

Dette gir et mer stabilt og oversiktlig grunnlag for å avgjøre om området trenger vanning.

[Neste stegVelge ut data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/velge-ut-data)
