# Bygging og vedlikehold av de felles skillene

Håndbok for redaktøren av de felles skillene. Skillen `felles-skillbygger` er for alle som vil lage en egen skill, og viser hit når en av de felles skillene skal endres. Hvordan regelverk legges inn og kontrolleres, står i `verktoy/BYGGING.md`.

## Hvor kildene ligger

- De åpne felles skillene ligger i `skills/<navn>/SKILL.md`, med en oversikt i `skills/KATALOG.md`. Hent gjeldende versjon herfra før du endrer, og skriv endringen tilbake hit.
- En ny felles skill legges inn i katalogen med hvem den er for.
- Skills med innhold som ikke skal ligge åpent, lastes ned som fil fra intranettet (i dag bare `felles-intern`). Kildene til dem ligger privat hos redaktøren, og et privat repo kan ikke leses av brukere uten egen GitHub-tilkobling, heller ikke med token (testet 21.10.2026). Legg aldri token i en skill.
- Felles skills heter `felles-…`. Ingenting i de åpne basene skal vise hvilket departement som står bak: ikke i navn, tekst, e-postadresser, commit-meldinger eller PR-tekster. `verktoy/sjekk_tekst.py` kontrollerer dette.

## Hvilken base innholdet hører hjemme i

| Innhold | Base |
|---|---|
| Lov, forskrift, rundskriv, tariffavtale, EU-rettsakter, Stortinget, statsbudsjettet, statistikkatalogen, veiledere, politiske dokumenter, skriveregler | `Offallnor/offdocs` |
| NOU-er, meldinger, proposisjoner, strategier og tildelingsbrev på utdannings-, arbeids- og velferdsområdet | `Offallnor/offdocsfor`, nås via skillen `felles-dokumenter` og via `CLAUDE.md` i offdocs |
| Dokumenter om politiet og forvaltningen rundt politiet | `Offallnor/offdocspol`, med egen skill |
| Forskningssvar, kildekataloger og forskningsløypa | `Offallnor/forskning`, med fulltekst i det private `Offallnor/forskning-tekst` |

Alle basene er åpne. Bare innhold som allerede er offentlig eller kan offentliggjøres, legges der. Kontroller av andres forslag, upubliserte svar og innhold fra interne dokumenter hører ikke hjemme der, selv om de bygger på offentlige fakta.

## Mønster for en peker-skill

`felles-regelverk`, `felles-dokumenter`, `felles-data`, `felles-budsjett` og `felles-sprak` har samme oppbygning. Bruk den:

1. **Description:** bred på tema og hverdagsspråk. Avslutt med «Last den før du svarer, og svar ikke fra hukommelsen.»
2. **Brødtekst:** si at innholdet ikke ligger i skillen, men hentes ved hvert oppslag.
3. **Fremgangsmåte:** hent én inngangsfil med full adresse (`https://raw.githubusercontent.com/Offallnor/offdocs/main/...`), med `curl -sL` i kodeverktøyet eller med hentverktøyet. Følg den.
4. **Hvis hentingen feiler:** ta med avsnittet «Hvis hentingen feiler» fra `skills/felles-regelverk/SKILL.md`, og bytt ut hva som hentes. Det skiller en sperre i innstillingene fra en midlertidig feil, og ved sperre sier Claude hvilket nettsted brukeren må tillate og hvor i innstillingene det gjøres.

Avgrensningen (hva som er dekket og ikke) ligger i inngangsfilen i repoet, ikke i skillen. Da kan den endres uten ny opplasting.

## Kjøremiljøet

- Skriving til GitHub fra claude.ai er sperret (403, testet 20.10.2026), både med token og uten. En skill kan derfor ikke sende noe til et repo fra vanlig chat. Meldinger om feil går på e-post etter oppskriften i `OM-BASENE.md`.
- Skills som henter fra de åpne basene, krever nettverkstilgang til `raw.githubusercontent.com`. Skills med skript krever kodeverktøy.

## Versjon

Hver SKILL.md har linjen «Versjon ÅÅÅÅ-MM-DD» øverst (med .2, .3 osv. ved flere endringer samme dag), og `SKILLVERSJONER.md` har nyeste versjon av hver skill. Sett ny versjon begge steder i samme commit. Glemmer du `SKILLVERSJONER.md`, får ingen beskjed om den nye versjonen. Glemmer du skillen, får brukerne beskjed hver gang. For en skill som lastes ned som fil, settes versjonen i `SKILLVERSJONER.md` først når den nye filen ligger på intranettet.

## Installasjon og oppdatering

- Brukerne installerer og oppdaterer ved å si «oppdater skillene» til `felles-intern`. Den henter kildene herfra og legger skillene fram som kort brukeren lagrer.
- Endringer i innholdet i en base krever ingen ny installasjon. Bare endringer i SKILL.md gjør det.

## Endre en description

Kjør én måling med skill-creators `run_eval.py` (20 spørsmål, omtrent halvparten som skal trigge) når descriptionen til en felles skill er ny eller endret. `run_loop.py` kjøres bare når målingen viser at skillen trigger dårlig. Kaldtest i vanlig chat trengs fortsatt før endringen sendes ut, se `felles-skillbygger`.

## Dokumentasjon

Commit-meldingen er loggen for de felles skillene. Si hva som ble funnet, hva som ble endret og hva det bygger på.
