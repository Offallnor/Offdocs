---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/merke-data"
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

## Merke data

Datamerking betyr at du setter etiketter på dataene slik at KI-systemet forstår hva det ser på. For eksempel hvis du trener en modell til å kjenne igjen dyr i bilder, merker du hvert bilde med riktig dyr, som “hund”, “katt” eller “elg”.

Du må merke data når du trenger slike etiketter for å trene KI-systemet og de ikke allerede finnes i datasettet.

### Datamerking er spesielt viktig hvis

- du bruker ustrukturerte data som bilder, tekst og lyd siden disse ikke har en tydelig struktur fra før
- du bruker veiledet læring der modellen lærer fra eksempler med fasit, som i bildeklassifisering

For metoder som ikke-veiledet læring trenger du derimot ikke slike etiketter siden modellen selv finner mønstre og grupper i dataene.

Hvordan påvirker merking KI-systemet?

Det er viktig at du merker dataene på en konsekvent og riktig måte. Ulike tolkninger eller uklare regler kan føre til dårligere resultater fra KI-systemet. Feil eller skjev merking kan også påvirke hvordan KI-systemet tar beslutninger.

Du bør derfor

- ha klare retningslinjer for hvordan data skal merkes
- dokumentere hvordan merkingen er gjort
- kvalitetssikre merkingen med stikkprøver eller ved at flere vurderer samme data

### Merk data automatisk eller manuelt

Automatisk merking betyr at data blir merket maskinelt basert på faste regler eller tidligere lagret informasjon. Det krever tydelig styring, og det er særlig viktig med åpenhet, sporbarhet og menneskelig kontroll.

Ofte er en kombinasjon av menneske og maskin best, for da får du både effektivitet og kontroll.

Tips til hvordan du kan kvalitetssikre automatisk merking:

- Kontroller et utvalg av de merkede dataene manuelt. Hvis det er store forskjeller mellom hvordan mennesker og systemet merker må du justere reglene eller vurdere om metoden fungerer godt nok.
- Følg opp automatisk merking med Modenhetstrappen kan hjelpe dere å forstå hvor dere er i dag kvalitetssikring. Da unngår du feil og at modellen gradvis blir dårligere.

Bruk av KI og automatisering i datastyring kan effektivisere arbeidet, men krever tydelig styring.

### Eksempel

For å trene et KI-system må du ofte merke data med riktig “fasit”. Her er noen vanlige eksempler.

- Bilder: Et bilde merkes med hva det inneholder, f.eks. “hund”, “katt” eller “bil”.
- Tekst (saksbehandling): En henvendelse merkes som “klage”, “søknad” eller “spørsmål”.
- Tekst (følelser): En kommentar merkes som “positiv”, “negativ” eller “nøytral”.
- Dokumenter: Dokumenter merkes som f.eks. “kontrakt”, “rapport” eller “notat”.
- Informasjonsuttrekk fra tekst: Ord eller setninger merkes som “person”, “organisasjon” eller “dato”.
- Transaksjoner: Hendelser merkes som “svindel” eller “ikke svindel”.
- Lyd: Lydopptak merkes med hva som blir sagt (tekst).

[Neste stegAnalysere skjevhet i data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data)
