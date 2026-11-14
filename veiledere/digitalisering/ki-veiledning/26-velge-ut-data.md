---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/velge-ut-data"
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

## Velge ut data

Noen ganger trenger du bare en del av datasettet. Det kan for eksempel være når du vil teste KI-systemet raskt eller når du skal dele data i treningssett, valideringssett og testsett.

Et mindre datasett kan også være nyttig for å teste hypoteser uten å bruke unødvendig kapasitet.

Når du velger ut data er det viktig å gjøre det på en måte som gir et representativt utvalg.

### Velg metode for å velge ut data

Det finnes ulike metoder:

- **Tilfeldig utvalg:** Bruk når du vil ha et representativt utvalg av hele datasettet uten å vektlegge bestemte grupper.
- **Stratifisert utvalg:** Bruk når du vi ha et balansert utvalg som gjenspeiler viktige forskjeller i dataene.

Hva er forskjellen på tilfeldig og stratifisert utvalg?

Forskjellen er at ved tilfeldig utvalg har alle datapunkter like stor sjanse for å bli valgt, mens ved stratifisert utvalg deler du først dataene i undergrupper og velger deretter fra hver gruppe for å sikre at alle grupper er representert.

### Eksempel

Et vanningssystem samler inn store mengder data fra sensorer som måler jordfuktighet, temperatur og værforhold.

Hvis du skal teste en ny KI-modell kan du velge ut et mindre datasett i stedet for å bruke alle dataene.

- Tilfeldig utvalg: Du velger tilfeldig målinger fra hele datasettet. Dette kan fungere hvis forholdene er ganske like i hele området.
- Stratifisert utvalg: Du deler først dataene inn i grupper, for eksempel etter område (solrikt vs. skyggefullt), plantetype eller jordtype. Deretter velger du data fra hver gruppe.

Hvis du bare velger data tilfeldig kan du risikere å få mest data fra områder med høy fuktighet. Ved stratifisert utvalg sikrer du at både tørre og fuktige områder er representert. Et godt utvalg av data gjør at KI-systemet lærer et mer riktig bilde av virkeligheten.

[Neste stegLage og velge relevante egenskaper](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/lage-og-velge-relevante-egenskaper)
