# Lånekassen – statistikk om studiestøtte

Lånekassen publiserer statistikk på https://lanekassen.no/nb-NO/statistikk-og-analyse/statistikk/. Kontrollert 2026-11-12. Lånekassen har ikke et åpent API for statistikk.

For å lese sidene må `lanekassen.no` være tillatt i brukerens innstillinger i Claude. `www.lanekassen.no` sender videre til `lanekassen.no`, så `*.lanekassen.no` alene er ikke nok.

## Slik bruker du Lånekassen

1. **Tabellene på statistikksidene kan du ikke lese.** De er innebygde Power BI-rapporter som lastes i nettleseren, og de krever at brukeren har godtatt informasjonskapsler. Gi brukeren lenken til riktig side (se under), og si at tallene må leses der. Beskriv ikke tallene eller figurene, og gjengi ikke tall fra hukommelsen.
2. **Nøkkeltallene i årsrapporten «Utdanningsstøtten» kan du lese.** Rapportsiden for hvert år har de viktigste tallene som vanlig tekst, for eksempel antall kunder, utbetalt studiestøtte og studiegjeld. Oppgi rapporten og året som kilde. Rapporten kommer om sommeren, og hver rapport har tall for forrige kalenderår og inneværende studieår.
3. **Hele rapporten er en PDF** som lenkes fra rapportsiden. Den ligger under `lanekassen.no/api/`, som Lånekassen ikke tillater automatisk henting fra (robots.txt). Gi brukeren lenken i stedet for å hente den.
4. **Bevilgninger** til stipend, lån og tap står i budsjettet, kap. 2410, 5310 og 5617 (se budsjettdelen), ikke hos Lånekassen.

## Statistikksidene

Alle sidene ligger under `https://lanekassen.no/nb-NO/statistikk-og-analyse/statistikk/`.

| Side | Innhold |
|---|---|
| `hovedtall/` | Nøkkeltall, antall kunder siste ti år, tildeling av stipend og lån, utviklingen i basislånet |
| `studenter-i-norge/` | Studenter med støtte i Norge, blant annet barnestipend, foreldrestipend, flyktningstipend, tilleggslån, skolepengelån og tilleggsstipend |
| `studenter-i-utlandet/` | Gradsstudenter og utvekslingsstudenter i utlandet etter land, lærested, fylke, kjønn, alder og fag, og skolepengestøtte og rekrutteringsstipend |
| `elever-i-norge/` | Elever med støtte, borteboerstipend (også per fylke), inntektsavhengig stipend og utstyrsstipend |
| `tilbakebetaling/` | Antall tilbakebetalere, gjennomsnittsgjeld etter endt utdanning, betalingsutsettelse, fast og flytende rente |

## Rapporter og analyser

Ligger under `https://lanekassen.no/nb-NO/statistikk-og-analyse/innsikt-og-analyse/`.

| Side | Innhold |
|---|---|
| `utdanningsstotten-ÅR/` | Årsrapporten «Utdanningsstøtten» (finnes for 2023, 2025 og 2026; 2024 heter `utdanningsstotta-2024/`, 2022 `utdanningsstotten-2022---tall-og-fakta/`) |
| `rapport-om-mislighold-av-studielan/` | Mislighold av studielån |
| `studieforlop/`, `inntekt-og-studieprogresjon/`, `studenter-og-arbeid/` | Studieforløp, inntekt og arbeid blant studenter |
| `behovsproving-hvem-overstiger-belopsgrensene/` | Behovsprøving av stipend |
| `rapport-om-bruk-av-studiestotte-blant-studenter-med-innvandrerbakgrunn/` | Studiestøtte blant studenter med innvandrerbakgrunn |
| `analyse-av-flyktningstipend/` | Flyktningstipend |

Listen over analyser endres. Se hele lista på `https://lanekassen.no/nb-NO/statistikk-og-analyse/`.
