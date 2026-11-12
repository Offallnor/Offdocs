# Udir – statistikk om barnehage, grunnskole og videregående

Utdanningsdirektoratet (Udir) publiserer statistikk på https://www.udir.no/tall-og-forskning/statistikk/. Tallene vises i en innebygd statistikkportal og i Udirs analysebrett, som henter dataene med JavaScript i nettleseren. Analysebrettet krever innlogging for noen data. Claude kan derfor ikke lese tallene rett fra sidene. Kontrollert 2026-11-11.

## Slik bruker du Udir

1. **Finnes tallet hos SSB, bruk SSB** (se `data/ssb.md`). Det gjelder blant annet elevtall, lærlinger, gjennomføring i videregående, lærerkompetanse og nøkkeltall for barnehage og skole.
2. **Er det Udirs egen statistikk** (karakterer, nasjonale prøver, fravær, søkere og førsteinntak), vis brukeren til riktig side under og si at tallene må leses der. Gjengi ikke tall fra hukommelsen. Beskriv ikke hva som står på siden, eller hvilke valg brukeren må gjøre der, når du ikke har lest siden.
3. **Elevundersøkelsen** kan hentes fra Udirs åpne API, se under.

## Elevundersøkelsen fra API-et

Udirs åpne API har åtte eksporttabeller, alle fra Elevundersøkelsen. Udir skriver i dokumentasjonen at API-et «ikke er ment for ekstern bruk i dag, og vil endres uten varsel». Si det i svaret, og vis til Udirs side for offentlige resultater ved tvil.

| EksportID | Innhold |
|---|---|
| 148 | Grunnskole: indikatorer (mestring, trivsel, støtte fra lærer m.m.) |
| 149 | Grunnskole: tema |
| 150 | Grunnskole: mobbing |
| 151 | Grunnskole: deltakelse |
| 152 | Videregående: indikatorer |
| 154 | Videregående: tema |
| 153 | Videregående: mobbing |
| 243 | Videregående: deltakelse |

Krever kodeverktøyet og at `api.statistikkbanken.udir.no` er tillatt i brukerens innstillinger.

```
# Lista over eksporter
curl -s https://api.statistikkbanken.udir.no/api/rest/v2/Eksport
# Gyldige verdier for skoleår (TidID) og enhet (EnhetID)
curl -s https://api.statistikkbanken.udir.no/api/rest/v2/Eksport/148/filterVerdier
# Data for hele landet, skoleåret 2025-26
curl -s "https://api.statistikkbanken.udir.no/api/rest/v2/Eksport/148/data?filter=TidID(202512)_EnhetID(-12)"
```

- Filter må oppgis. `TidID` er skoleåret (`202512` = 2025-26), `EnhetID(-12)` er hele landet. Andre enheter (fylke, kommune, skole) står i `filterVerdier`.
- Svaret for hele landet er stort (2,5 MB for eksport 148). Les det inn i kodeverktøyet og filtrer på `Indikator`, `TrinnKode` og `KjoennKode` før du viser noe.
- Tallene kommer som tekst med norsk desimalkomma og mellomrom som tusenskille (`"3,6"`, `"52 526"`).
- `Score` er snittet på en skala fra 1 til 5. `AndelSvaralternativ1–5` er prosent som har svart hvert alternativ.
- API-dokumentasjonen: https://statistikkportalen.udir.no/api/rapportering/openapi
- Bare eksport 148 er prøvd med data. De andre er ikke kontrollert.
- **Mobbing.** Si hvilken definisjon tallet bygger på, slik den står i svaret fra API-et (indikator og svaralternativ). Udir regner som regel som mobbet den som svarer at det skjer 2–3 ganger i måneden eller oftere. Kontroller det i svaret før du skriver det.

## Udirs statistikksider

Sidene under ligger under https://www.udir.no/tall-og-forskning/statistikk/. Analysebrettet: https://analysebrettet.udir.no/. Statistikknotater: https://sokeresultat.udir.no/forskning-og-rapporter.html?rapportinnholdstype=Statistikk

| Tema | Side |
|---|---|
| Barnehage | `statistikk-barnehage/` |
| Grunnskole (oversikt med karakterer, nasjonale prøver, elevtall og fravær) | `statistikk-grunnskole/` |
| Fag- og yrkesopplæring | `statistikk-fag-og-yrkesopplaring/` |
| Videregående: søkere | `statistikk-videregaende-skole/sokere-vgs/sokere-utdanningsprogram/` |
| Videregående: elevtall | `statistikk-videregaende-skole/elevtall-i-videregaende-skole/elevtall-vgo-utdanningsprogram/` |
| Videregående: førsteinntak | `statistikk-videregaende-skole/forsteinntak/sortert-etter-utdanningsprogram/` |
| Videregående: karakterer | `statistikk-videregaende-skole/karakterer-vgs/` |
| Videregående: fravær | `statistikk-videregaende-skole/fravar-vgs/` |
| Videregående: fagvalg | `statistikk-videregaende-skole/fagvalg-i-videregaende-skole/fagvalg-vgs/` |
| Videregående: gjennomføring | `statistikk-videregaende-skole/tall-for-gjennomforing-av-videregaende-opplaring/gjennomforing-av-videregaende-opplaring--sortert-etter-fylke/` |
| Videregående: overganger | `statistikk-videregaende-skole/overganger-i-videregaende-opplaring/overganger/` |
| Videregående: elever som har sluttet | `statistikk-videregaende-skole/sluttet/` |
| Ungdom uten og utenfor videregående | `statistikk-videregaende-skole/ungdom-uten-og-utenfor-vgo/` |
| Oppfølgingstjenesten | `statistikk-videregaende-skole/ungdom-utenfor-opplaring-og-arbeid/` |
| Voksne i videregående | `statistikk-videregaende-skole/voksne/voksne-i-vgo-utdprg/` |
| Privatisteksamener | `statistikk-videregaende-skole/avlagte-privatisteksamener/` |
| Elevundersøkelsen, offentlige resultater for grunnskolen | Gå fra https://www.udir.no/tall-og-forskning/brukerundersokelser/elevundersokelsen/ (egen side for grunnskolen er ikke kontrollert) |
| Elevundersøkelsen, offentlige resultater (vgs) | https://www.udir.no/tall-og-forskning/brukerundersokelser/elevundersokelsen/resultater/offentlige-resultater-vgs/ |

Udir publiserer også analyser med tall under `statistikk-videregaende-skole/analyser/ÅR/`. Veiledning i bruk av tallene: https://www.udir.no/kvalitet-og-kompetanse/bruk-av-tall-og-data/
