---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare"
hentet: "2026-11-14"
---

# Gjør dataene KI-klare

KI-klare data er data som er tilrettelagt for maskinell bruk og gjenbruk. For å lykkes med å utvikle og bruke KI må virksomheter ha kontroll både på dataene de bruker og på resultatene de skaper med dem. Det går en kjede fra gode data inn til gode resultater ut.

Denne veiledningen beskriver en praktisk prosess for hvordan du kan jobbe systematisk med å styre, forvalte og dele data for å bli KI-klar. Det finnes flere måter å løse disse oppgavene på. Hva som er riktig tilnærming vil avhenge av kontekst, behov og rammebetingelser.

### Hvorfor er dette viktig?

Mangelfulle eller dårlig dokumenterte data kan gi svakere analyser, feil beslutningsgrunnlag eller uønskede skjevheter i KI-systemer. Det er viktigere å etablere et godt datagrunnlag med kvalitetssikrede og pålitelige data, enn å justere eller ta i bruk nye modeller.

1. ### Før du samler inn data
  1. [Finn ut hvilke data du trenger](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/finn-ut-hvilke-data-du-trenger)
  2. [Forstå behandling av sensitive personopplysninger](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/forsta-behandling-av-sensitive-personopplysninger)
  3. [Teknisk dokumentasjon](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/teknisk-dokumentasjon)
  4. [Personvern og sikkerhet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/personvern-og-sikkerhet)
2. ### Samle inn data
  1. [Kartlegg datakilder](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/kartlegg-datakilder)
  2. [Samle inn data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/samle-inn-data)
3. ### Forberede data til bruk
  1. [Måle og forbedre datakvalitet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/male-og-forbedre-datakvalitet)
  2. [Transformere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/transformere-data)
  3. [Aggregere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/aggregere-data)
  4. [Velge ut data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/velge-ut-data)
  5. [Lage og velge relevante egenskaper](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/lage-og-velge-relevante-egenskaper)
  6. [Berike data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/berike-data)
  7. [Merke data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/merke-data)
  8. [Analysere skjevhet i data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data)
  9. [Gjøre data tilgjengelig for KI-systemet](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/gjore-data-tilgjengelig-for-ki-systemet)
4. ### Slette data
  1. [Slette og arkivere data](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/slette-og-arkivere-data)

Hva kjennetegner KI-klare data?

KI-klare data kjennetegnes blant annet ved at de

- har god og dokumentert datakvalitet
- er strukturert og standardisert
- har tilstrekkelige metadata og beskrivelser
- har tydelig informasjon om opprinnelse, oppdatering og bruksvilkår
- kan deles og brukes på tvers av systemer og virksomheter
- er forvaltet på en måte som ivaretar personvern, sikkerhet og ansvarlighet

Arbeid med metadata, standardisering, datakvalitet og interoperabilitet bidrar ikke bare til bedre datadeling, men også til at data kan brukes tryggere og mer effektivt i KI-anvendelser. God informasjonsforvaltning er derfor også et viktig grunnlag for framtidig bruk av kunstig intelligens.

Vi finner retning i strategier, krav i reguleringer, stadig flere rammeverk og fagmiljøer som peker på hva som er viktig for å lykkes med KI-klare data. [Open Data Institute (ODI) peker i rapporten A Framework for AI-ready Data](https://theodi.cdn.ngo/media/documents/A_framework_for_AI-ready_data.pdf) (2025) på at KI-klare data krever både tekniske, organisatoriske og styringsmessige tiltak, inkludert dokumentasjon, metadata, kvalitet og tydelig governance.

Hva er KI-styring og hvem jobber med det?

God styring av KI handler om kvaliteten på resultatene fra KI-systemet.

Målet er å sikre at KI-løsninger er rettferdige og uten skjevheter, forklarbare og forståelige, robuste og trygge i bruk og ansvarlige i tråd med regelverk. Dette gir tillit til hvordan KI brukes og hvilke beslutninger som tas.

Hvem jobber med KI-styring?

- Juridiske og personvernmiljøer
- Risikostyring og compliance
- Produkt- og fagansvarlige
- Data scientists og KI-utviklere

Typiske utfordringer:

- Skjevheter i modeller
- Redusert ytelse over tid
- Manglende transparens
- Omdømmerisiko

Hva er datastyring og hvem jobber med det?

God datastyring handler om kvaliteten på dataene som brukes i systemet. Målet er å sikre at dataene er riktig og komplett, oppdatert og tilgjengelig, samt håndtert på en sikker måte i tråd med personvern og informasjonssikkerhet.

Dette gir et pålitelig grunnlag for analyse og KI.

Hvem jobber med datastyring?

- Dataforvaltere og datastewards
- Informasjons- og dataarkitekter
- Sikkerhets- og personvernmiljøer
- IT- og dataplattformteam

Typiske utfordringer:

- Dårlig datakvalitet
- Manglende kontroll på data
- Risiko for feil beslutninger

FAIR-prinsippene og kunstig intelligens

FAIR-prinsippene gir en felles ramme for god dataforvaltning, spesielt når data kommer fra ulike kilder og skal brukes på tvers av systemer og virksomheter. Prinsippene er et viktig grunnlag for å gjøre data klare for deling, gjenbruk og bruk i kunstig intelligens. FAIR alene er imidlertid ikke nok for å lykkes med kunstig intelligens. Data må også være pålitelige. Pålitelige data har god kvalitet, er dokumentert, oppdaterte og håndtert på en måte som skaper tillit.

[Les mer om FAIR-prinsippene](https://ki.norge.no/veiledning/gjor-dataene-ki-klare/finn-ut-hvilke-data-du-trenger/gjor-data-ki-klare-med-fair-prinsippene)

EU og Norge stiller krav

Både EU og Norge stiller økende krav til hvordan data forvaltes, deles og brukes. Regelverkene peker i samme retning. For å lykkes med datadeling og bruk av KI må virksomheter ha god kontroll på egne data og begreper.

Kravene gjelder ikke bare offentlig sektor, men mange av dem retter seg spesielt mot offentlig forvaltning eller får størst betydning der.

[Interoperable Europe Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R0903&qid=1781007879572)stiller krav til at data deles på en standardisert måte. Dette forutsetter at virksomheter bruker felles begreper og har et tydelig begrepsapparat som gjør data forståelig på tvers av systemer og organisasjoner.

[Data governance Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R0868&qid=1781007768629) legger til rette for økt deling og gjenbruk av data. Det stilles blant annet krav til publisering av metadata i nasjonale datakataloger slik at data blir enklere å finne og bruke.

[AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689&qid=1781010991372) krav til kvaliteten på data som brukes i KI-systemer, spesielt for systemer med høy risiko. Dette inkluderer krav til datakvalitet, dokumentasjon og håndtering av skjevheter i data.

[Lov om datadeling og dataforvaltning](https://www.regjeringen.no/no/dokumenter/prop.-54-ls-20252026/id3154578/?) samler og videreutvikler krav til deling og viderebruk av offentlige data i Norge. Loven innebærer blant annet at virksomheter skal gjøre data tilgjengelig der det er mulig og sørge for at datasett er tilstrekkelig dokumentert gjennom metadata. Dette bidrar til at data blir lettere å finne, forstå og bruke - også som grunnlag for utvikling og bruk av KI.
