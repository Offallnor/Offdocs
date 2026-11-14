---
veileder: "Veileder for digitaliseringsvennlig regelverk"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/datadeling/datamaskiners-muligheter-og-begrensninger-ved-automatisert-rettsanvendelse/2939"
hentet: "2026-11-14"
---

# Datamaskiners muligheter og begrensninger ved automatisert rettsanvendelse

Opprettet: 07. oktober 2021

Sist endret: 16. november 2021

## Hvordan gjøres regelverk til programkode?

Ved automatisering av rettsanvendelse må en med utgangspunkt i juridisk metode tolke regelverket for å finne innholdet i den aktuelle rettsregelen.

Den ferdigtolkede rettsregelen må brytes ned til instruksjoner som kan gjøres til et dataprogram. Denne delen av prosessen vil være lettere ved et automatiseringsvennlig regelverk enn ved et tradisjonelt utformet regelverk.

Når instruksjonene settes sammen, får man en oppskrift for hva datamaskinen skal gjøre. Dette kalles en [algoritme](https://snl.no/algoritme). Normalt gjøres den til et dataprogram ved å skrives som kildekode i et eller flere høynivåprogrammeringsspråk.

For at kildekoden kan "kjøres" som et dataprogram gjøres den automatisk til instruksjoner som datamaskinen forstår ved hjelp av en [kompilator eller tolk](https://snl.no/programmeringsspr%C3%A5k). Denne prosessen er begrenset av at datamaskinen på et grunnleggende nivå opererer med logiske og aritmetiske operasjoner. Dersom det er skrevet elementer i kildekoden som kompilatoren eller tolken ikke aksepterer, kan ikke programmet kjøre.

Forutsatt at alt er gjort korrekt, representerer kildekoden fullt ut det ferdigtolkede regelverket. Resultatet datamaskinen produserer når programmet kjøres kan vi velge å anse som en avgjørelse, eller vi kan benytte resultatet som en del av en avgjørelse.

Denne prosessen kalles ofte for [transformasjon](https://www.digdir.no/datadeling/spesifikke-anbefalinger-lage-automatiseringsvennlig-regelverk/2879#automatiseringsvennlig_regelverk_gjor_det_lettere_aa_automatisere_rettsanvendelsen) av regelverket. Prosessen behøver ikke å gjennomføres ved at alle juridiske spørsmål uttømmende avklares før det gjøres om til instruksjoner i programkoden. Ofte vil dette skje vekselsvis. Når en skal forsøke å bryte regelverket ned i instruksjoner vil en kanskje se hvor det er behov for ytterligere tolkningsspørsmål som rettsanvenderen må ta stilling til med utgangspunkt i juridisk metode.

**Logiske og aritmetiske operasjoner**

Logiske operasjoner jobber med og resulterer i om noe er sant eller usant. Dette er operasjoner som:

- OG - Sant hvis begge er sanne.
- ELLER - Sant hvis en eller begge er sanne.
- IKKE - Det motsatte. Sant når det usant. Usant når det er sant.

Aritmetiske operasjoner er operasjoner som:

- Addisjon
- Subtraksjon
- Multiplikasjon
- Divisjon

Grunnleggende operasjonene settes sammen for mer avanserte operasjoner. Dette kan igjen bygges på lag for lag og gir muligheten for avanserte [dataprogrammer](https://snl.no/dataprogram).

## Finnes det maskinlesbar informasjon?

Instruksjonene i programkoden knytter seg både til hvilken informasjon datamaskinen skal behandle og hvordan denne informasjonen skal behandles. Begge disse er begrenset av at kompilatoren eller tolken bare aksepterer elementer i kildekoden som kan gjøres til logiske eller aritmetiske instruksjoner til datamaskinen.

Informasjonen datamaskinen skal behandle må foreligge i et maskinlesbart format som kan benyttes i de logiske og aritmetiske operasjonene. For at regelverket skal kunne lede til automatisert rettsanvendelse må vilkår eller begrep i regelverk kunne vurderes på bakgrunn av slik maskinlesbar informasjon. Det kan være mye arbeid knyttet til å gjøre informasjon som ikke er maskinlesbar om til informasjon som datamaskinen kan prosessere. Den som utvikler regelverk [bør derfor ha et bevisst forhold til hvilke dataforekomster som forutsettes](https://www.digdir.no/datadeling/spesifikke-anbefalinger-lage-automatiseringsvennlig-regelverk/2879#anbefalinger_for_automatiseringsvennlig_regelverk) når regelverk skal gi grunnlag for automatisert rettsanvendelse.

Forskrift om utdanningsstøtte § 51 har vilkåret "ikke bor sammen med en av eller begge foreldrene".

Dersom dette skal lede til automatisert rettsanvendelse, må dette vilkåret tolkes og det må vurdere hvordan dette kan knyttes opp mot maskinlesbare dataforekomster.

I forskrift om utdanningsstøtte § 51 er dette gjort mer automatiseringsvennlig ved at bestemmelsen viser til § 3 som definerer hva som ligger i "ikke bor sammen med en av eller begge foreldrene". Av § 3 følger det at:

*"En søker regnes som ikke å bo sammen med foreldrene når søkeren oppfyller ett av følgende vilkår:*

*a. Søkeren bor i en selvstendig boenhet som er fysisk atskilt fra huset der foreldrene bor.*

*b. Søkeren bor i en selvstendig og klart atskilt boenhet i samme hus som foreldrene, og søkerens boenhet er registrert med et eget bruksenhetsnummer eller tilsvarende i Folkeregisteret eller i matrikkelen"*

Vilkårene i § 3 knytter seg til informasjon som det er langt lettere å løse på bakgrunn av maskinlesbar informasjon fra registre eller liknende. Instruksjonene i programkoden kan for eksempel sammenlikne informasjonen som knyttet til foreldrenes bosituasjon og søkerens bosituasjon.

## Datamaskiner er forutbestemte

Datamaskinens algoritme er fastsatt før denne utføres av datamaskinen. Dette betyr at dersom datamaskinen «tar en avgjørelse», så ble avgjørelsen i virkeligheten tatt da algoritmen ble skrevet. Ofte er det et omfattende arbeid for å [transformere regelverket til instruksjoner til datamaskinen](https://www.digdir.no/datadeling/spesifikke-anbefalinger-lage-automatiseringsvennlig-regelverk/2879#automatiseringsvennlig_regelverk_gjor_det_lettere_aa_automatisere_rettsanvendelsen). Det kan bety at hele eller deler av avgjørelsen også ble tatt igjennom tolkninger og vurderinger i transformasjonsprosessen.

En datamaskin gjør alltid det samme så lenge informasjonen den jobber med og algoritmen ikke er endret. To helt like saker vil bli behandlet helt likt. Datamaskinen er altså forutsigbar. Det betyr også at hvis du kjenner til informasjonen som behandles samt algoritmen, kan du se hva datamaskinen kommer til å avgjøre.

Hvordan utvikle automatiseringsvennlig regelverk?
