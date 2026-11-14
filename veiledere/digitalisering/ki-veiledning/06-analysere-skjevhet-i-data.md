---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data"
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

## Analysere skjevhet i data

Skjevhet, eller bias, er en systematisk feil som kan oppstå når dataene ikke er balanserte. Det skjer når enkelte grupper eller typer informasjon er overrepresentert, mens andre er underrepresentert.

Dette kan føre til at KI-systemet gir skjeve eller urettferdige resultater.

Å analysere skjevhet i data handler om å sikre at de er pålitelige, representative og egnet til formålet.

Det er viktig å være klar over at skjevhet ikke alltid er feil som må fjernes. Ofte gjenspeiler dataene virkelige forhold. Det viktigste er at du forstår skjevheten og hvilken betydning den har for bruken av KI-systemet. Selv om dataene kan være “korrekte” kan de inneholde skjevheter fordi de gjenspeiler historiske eller samfunnsmessige forhold. Derfor er det avgjørende å forstå konteksten dataene er hentet fra.

### Slik kan du analysere skjevhet

Målet er å sikre at dataene gir et mest mulig balansert og riktig grunnlag slik at KI-systemet ikke gir skjeve eller urettferdige resultater.

1. Identifiser kilder til skjevhet
2. Vurder skjevhet i dataene
3. Vurder behov for tiltak
4. Følg opp over tid

[Mer om hvordan du kan analysere skjevhet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data/skjevhet-i-data)

### Jobb kontinuerlig med skjevhet i data

Du må alltid vurdere og følge opp skjevhet i dataene dine, fra innsamling og behandling til utvikling og bruk av KI-systemet.

Du bør

- ha tydelige roller og ansvar for å følge opp datakvalitet og skjevhet
- dokumentere vurderinger og tiltak
- overvåke dataene over tid, siden skjevhet kan endre seg

### Eksempel

Et smart vanningssystem er trent på data fra et område der det er mest sol og lite skygge. Systemet lærer derfor at jorden ofte tørker raskt og at det er behov for hyppig vanning.

Når systemet tas i bruk begynner det å vanne oftere i disse områdene. Samtidig samler det inn nye data, men disse dataene er påvirket av at systemet allerede vanner mye.

Resultatet blir at

- systemet fortsetter å se mye tørre forhold, fordi det hovedsakelig overvåker solrike områder
- det får lite data fra skyggefulle områder der behovet er annerledes
- det lærer at høy vannmengde er “riktig” i stadig flere situasjoner

Over tid forsterkes dette mønsteret. Systemet blir dårligere til å håndtere variasjoner i forhold og kan for eksempel vanne for mye i områder som egentlig ikke trenger det.

[Neste stegGjøre data tilgjengelig for KI-systemet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/gjore-data-tilgjengelig-for-ki-systemet)
