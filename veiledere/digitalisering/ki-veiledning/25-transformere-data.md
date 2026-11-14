---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/transformere-data"
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

## Transformere data

For å kunne sammenstille data fra ulike kilder og bruke dem likt må de være like i struktur og format.

Det betyr at du må tilpasse dataene slik at de kan sammenlignes og brukes på samme måte der det er forskjeller i for eksempel måleenheter, ulike kategoriseringer eller datoformater.

Deretter må du gjøre dataene like.

### Slik gir du dataene likt format

Du kan gi dataene likt format ved å

- normalisere verdier til en felles skala
- skalere dem til samme størrelsesorden
- konvertere dem til samme format eller enhet

### Eksempel

For å bruke data fra ulike kilder inn i det smarte vanningssystemet må dataene gjøres sammenlignbare.

Gjør om til samme skala: Jordfuktighet kan måles på ulike måter. For eksempel 0–1023 eller 0–1. Dette må gjøres om til én skala, for eksempel prosent: 0–100 %.

Gjør verdiene sammenlignbare: Én sensor måler jordfuktighet hvert minutt, mens en annen måler én gang i timen. For å kunne bruke dataene sammen må de tilpasses til samme tidsintervall, for eksempel ved å beregne gjennomsnitt per time.

Bruk samme enhet og format: Temperatur kan være i fahrenheit eller celsius, og datoer kan skrives på ulike måter. Dette må gjøres likt før dataene brukes.

[Neste stegAggregere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/aggregere-data)
