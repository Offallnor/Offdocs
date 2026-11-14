---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/lage-og-velge-relevante-egenskaper"
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

## Lage og velge relevante egenskaper

Av og til er det behov for å justere hvor mye informasjon du har i datasettet, enten fordi viktig informasjon mangler, eller fordi du ikke trenger all informasjonen for å trene KI-løsningen.

Målet er å finne et nivå som gir et godt grunnlag for å trene KI-systemet.

Egenskaper, features, er variabler i datasettet som beskriver det du analyserer, for eksempel temperatur, jordfuktighet eller alder. Det er disse KI-systemet bruker for å lære mønstre.

### Slik velger og lager du egenskaper

Å velge egenskaper betyr å plukke ut det som faktisk er relevant, og kutte det som er overflødig eller gir lite verdi. Dette kalles feature selection på engelsk og kan gjøre modellen både enklere og mer presis.

Nye egenskaper kan lages ved å kombinere eksisterende data. Dette kalles feature creation på engelsk, og kan for eksempel være å beregne gjennomsnittlig jordfuktighet per dag basert på flere målinger.

Metoder du kan bruke

Det finnes metoder, som PCA (Principal Component Analysis), som kan hjelpe med dette. Slike metoder beskrives ofte i sammenheng med maskinlæring. De finner egenskaper som gir mye av den samme informasjonen, såkalte redundante egenskaper, og slår dem sammen slik at datasettet kan forenkles uten å miste viktig informasjon.

### Reduser kompleksitet

Antall egenskaper i et datasett kalles dimensjonalitet. Mange egenskaper kan gjøre modellen mer kompleks uten nødvendigvis å gi bedre resultater. Det kan derfor være nyttig å redusere antallet egenskaper.

### Eksempel

Et smart vanningssystem bruker data som jordfuktighet, temperatur, luftfuktighet og værdata for å avgjøre når planter skal vannes. Dette er eksempler på egenskaper som KI-systemet bruker for å lære mønstre.

Systemet kan lage nye egenskaper ved å kombinere eksisterende data. For eksempel beregne gjennomsnittlig jordfuktighet per dag eller lage en indikator for tørkerisiko basert på temperatur, sol og luftfuktighet. Dette kan gi et bedre grunnlag for beslutninger enn enkeltmålinger.

Systemet kan fjerne unødvendige egenskaper hvis datasettet inneholder både temperatur i celsius og fahrenheit eller flere målinger som sier det samme. Dette gjør modellen enklere og mer effektiv.

Systemet kan redusere kompleksitet, dimensjonalitet. Hvis systemet bruker mange sensorer som måler nesten det samme kan det bli unødvendig komplisert. Da kan man slå sammen informasjonen eller velge ut de mest relevante målingene.

[Neste stegBerike data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/berike-data)
