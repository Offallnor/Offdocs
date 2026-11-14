---
name: "felles-skillbygger"
description: "Companion-skill til skill-creator for de felles skillene. Trigges ALLTID SAMMEN MED skill-creator, aldri alene og aldri i stedet for den, når noen skal lage, endre, teste eller forbedre descriptionen til en felles skill eller en egen skill på jobb. Brukes også når noen vurderer om noe bør bli en ny skill eller legges i de felles basene på GitHub. Legger til det som er særskilt for de felles skillene - om det trengs en ny skill i det hele tatt, tynn peker-skill mot innhold i GitHub eller selvstendig skill, kjøremiljø og sensitivitet, kaldtest og feiltyper, lagring og installasjon."
---

# Skill-bygging for de felles skillene

**Versjon 2026-11-14.2.** Hent også `https://raw.githubusercontent.com/Offallnor/offdocs/main/SKILLVERSJONER.md`. Står det en nyere versjon for denne skillen der, avslutt svaret med en skillelinje og denne linjen, etter eventuelle kilder: «**Ny versjon:** Det finnes nyere versjoner av de felles skillene. Si "oppdater skillene" for å få dem.» Si det bare én gang i samtalen. Feiler hentingen, la det være.

Companion-skill til skill-creator for alle som vil lage en egen skill på jobb. Den dekker om noe bør bli en skill i det hele tatt, sensitivitet, testing, lagring og hvordan en skill sendes til vurdering som felles skill. Mange brukere er nye i KI, så forklar valgene i vanlig språk, ikke bare utfallet.

**Skal en av de felles skillene endres** (for eksempel `felles-regelverk` eller denne), er det redaktørens arbeid. Hent da også `https://raw.githubusercontent.com/Offallnor/offdocs/main/skills/BYGGING.md` og følg den. Den har kildene, peker-mønsteret, versjonering og hvilken base innholdet hører hjemme i.

## Forhold til skill-creator

**Første handling: finn skill-creator blant de tilgjengelige skillene og åpne dens SKILL.md også.** Gjør det før du svarer, ikke når behovet dukker opp underveis.

Skill-creator dekker den generelle byggeprosessen (SKILL.md-anatomi, progressive disclosure, description, pakking). Instruksen om å åpne den følges bare omtrent hver tredje gang. Derfor gjentas skill-creators fire kjernespørsmål her, slik at de stilles uansett:

1. Hva skal skillen kunne gjøre?
2. Når skal den trigge (hvilke formuleringer og situasjoner)?
3. Hva skal den levere, og i hvilket format?
4. Trengs testspørsmål med fasit, eller holder en vurdering?

Når begge skillene er i bruk, gjelder testmetoden og lagringsreglene her, også for hvor mye av skill-creators automatiske testing som kjøres.

## Tilpass forklaringen til spørsmålet

- **Åpne spørsmål** («jeg vil lage en KI-hjelper for X»): forklar framgangsmåten, også hvorfor testing og plassering av innhold betyr noe.
- **Presise spørsmål** («hvorfor trigget ikke skillen»): gå rett på sak.
- Forklar hva en eksisterende skill gjør i vanlig språk, ikke bare med navnet.

## Steg 1: Trengs en ny skill?

Svar på dette før noe bygges. Det er det viktigste valget.

**Listen over skills har et tak.** I en test med 62 installerte skills ble bare rundt 30 descriptions vist til modellen. Hver ny skill konkurrerer med de andre om å bli sett.

**Derfor:**
- **Sjekk de felles skillene først.** Gjelder det lov og forskrift, Stortinget, utredninger og meldinger, statistikk, statsbudsjettet eller skriveregler, finnes det allerede en felles skill: `felles-regelverk`, `felles-dokumenter`, `felles-data`, `felles-budsjett` eller `felles-sprak`. Mangler det innhold der, er det bedre å be om at det legges inn i basen enn å lage en ny skill (se «Send skillen til vurdering»).
- **Temaet er hovedaksen.** Skills følger fagområde, ikke avdeling. Behov som gjelder én avdeling, hører hjemme under temaet, og skillen er felles.
- **En ny skill lages bare når spørsmålene trenger egen trigging**, altså når de ellers ikke ville nådd riktig innhold, eller når skillen gir en arbeidsmåte som ikke finnes fra før.

## Steg 2: Hva skal ligge i skillen

| Innhold | Hvor det hører hjemme |
|---|---|
| Stabilt: når skillen brukes, arbeidsmåte, svarregler, tone, format, små maler | I selve skillen |
| Skript som må kjøre med skillen (beregninger, filproduksjon) | I selve skillen |
| Stort, eller endrer seg ofte (lovtekst, tall, rundskriv, maler som oppdateres) | Ikke i en egen skill. Send det til vurdering, så kan det legges i en av de felles basene |

En skill som bygger på lov, tall eller budsjett, skal hente det fra de felles skillene, ikke ha egne kopier. Skriv for eksempel «Bruk felles-regelverk for lovteksten» i skillen.

## Steg 3: Kjøremiljø og sensitivitet

**Kjøremiljøet varierer mellom brukere:**
- Uten kodeverktøy kan skillen ikke kjøre `curl` eller skript. Hentverktøyet leser åpne adresser, men kan ikke sende token eller egne overskrifter.
- En skill kan ikke skrive til GitHub fra vanlig chat, og den kan ikke lese private repoer. Legg aldri token eller passord i en skill.
- Skills med skript krever kodeverktøy. Skriv det i beskrivelsen til brukerne.

**Sensitivitet er en del av designet.** Rammeverket for informasjonssikkerhet sier at blant annet r-notater ikke skal legges inn i KI-verktøy. Spør derfor om skillen vil invitere brukeren til å lime inn noe som ikke får ligge i Claude. Hvis ja, gjør skillen til et oppslagsverk for form og prosess som ikke tar imot saksinnhold. Det avgjørende er om noe avslører status, sannsynlig utfall, timing eller interne politiske vurderinger i en konkret sak, ikke om temaet er politisk følsomt.

## Description og trigging

- Ta med ordene folk faktisk bruker ved siden av fagordene («har ikke penger til husleie», ikke bare «økonomisk stønad»).
- Grensen er 1024 tegn. Unngå anførselstegn og kolon som kan ødelegge YAML-en. Skriv frontmatter med `yaml.dump()`, ikke med strengerstatning.
- Avgrens mot nabo-skillene, og si hva skillen ikke er for, når nabotemaet ligger nær.
- En skill som bare skal starte når brukeren ber om det, trenger en kort description. Lang tekst tar plass i lista uten å gi bedre trigging.
- Skills som skal brukes sammen, kan ikke regne med at begge trigger samtidig (lykkes omtrent hver tredje gang). Gi en eksplisitt instruks om å åpne den andre.

## Språk mot brukeren

Be Claude snakke enkelt med brukeren og gjøre det tekniske uten å kommentere det. Ord som token, GitHub, repo, filsti, skript, versjonsnummer og feilkode skal ikke stå i svaret. Skriv en eksempelsetning i skillen for det vanligste tilfellet, for eksempel en feilmelding: «Jeg fikk ikke hentet innholdet nå. Prøv igjen litt senere.» Ta det med i testen. Unntaket er navnet på et nettsted brukeren må tillate i innstillingene, siden brukeren må skrive det inn selv.

## Testmetode: kaldtest

En kaldtest stiller spørsmålet til en økt som bare har skillen, uten forklaring og uten å nevne skillen.

**To måter, og begge trengs før en skill deles med andre:**
- **Underagent** (i et prosjekt eller Claude Code): raskt, kan kjøres i serier. Tester trigging og innhold, men i et miljø med kodeverktøy.
- **Ny chat i claude.ai**, helst utenfor prosjekt og helst uten kodeverktøy: tester det miljøet kollegene faktisk bruker.

**Testsettet** bør ha fire typer spørsmål: dekket med fagord, dekket med hverdagsspråk, rett utenfor avgrensningen (skal si fra, ikke svare fra hukommelsen), og ikke relevant (skal ikke trigge). Ta med kontrollspørsmål med kjent fasit, og spørsmål mot tabellinnhold når kilden har tabeller. Foretrekk flere små runder (4–5 spørsmål) med retting mellom, framfor én stor.

**Feiltyper:**
- **A – Aldri synlig:** skillen trigger ikke.
- **B – Lest, men utelatt:** kilden leses, men informasjonen kommer ikke med i svaret.
- **C – Overflatisk:** SKILL.md lastes, men kildefilene åpnes aldri.
- **D – Overtrigging:** skillen trigger utenfor det den dekker og svarer fra hukommelsen i stedet for å si fra. Godkjent er å la være å trigge, eller å trigge og si at temaet ikke er dekket.
- **E – Kilden leder feil:** skillen trigger og henter riktig, men innholdet den henter sender modellen feil vei (sti som ikke finnes, foreldet tekst). Rett i kilden, ikke i skillen.

**Kaldtest fanger ikke byggefeil.** En skill som mangler innhold, svarer «ingen bestemmelse funnet», og det ser riktig ut. En utflatet tabell gir et selvsikkert svar med feilkoblede tall. Slike feil fanges bare av kontrollspørsmål med fasit.

### Måling av trigging

Når Claude Code er tilgjengelig (`claude -p` kan kjøres), kan triggingen måles med skill-creators skript. Hver kjøring koster tokens, så bruk dem sparsomt:

- **Skills som skal deles:** én måling med `run_eval.py` når descriptionen er ny eller endret, med 20 realistiske spørsmål, omtrent halvparten som skal trigge. De vanskelige spørsmålene ligger tett opptil en nabo-skill.
- **Forbedringsløpet** (`run_loop.py`) bare når målingen viser at skillen trigger dårlig. Det koster mange ganger mer.
- **Små skills til eget bruk:** noen få spørsmål for hånd holder.

Målingen sier om descriptionen treffer, ikke om svaret blir riktig. Skriv ned resultatet før du retter.

## Lagring og installasjon

**Å skrive en skillfil er ikke det samme som å installere den.** Filer som lages i en økt, finnes bare der. Si alltid fra, uoppfordret, at skillen må lagres før andre økter ser den: fra kortet Claude viser, eller som zip-fil som lastes opp under Innstillinger → Funksjoner → Skills. Lagring med samme navn erstatter den gamle. Å laste opp filen i en chat installerer den ikke.

## Send skillen til vurdering

En skill en ansatt lager, er til eget bruk. Den som vil, kan sende den til vurdering som felles skill. Redaktøren for basene vurderer om den skal bli en egen felles skill, en del av en eksisterende skill, eller innhold i en av basene.

1. Gjør dette bare når brukeren selv spør om skillen kan bli felles, eller vil sende den til vurdering. Ikke foreslå det på eget initiativ.
2. Sjekk at den ikke inneholder token, personopplysninger, saksinnhold eller interne vurderinger.
3. Hent `https://raw.githubusercontent.com/Offallnor/offdocs/main/OM-BASENE.md` og følg avsnittet om feil, med type «ny skill». Skriv i meldingen hva skillen gjør, hvem den er for, og hvordan den er testet. Legg SKILL.md ved som fil, eller lim den inn i e-posten hvis den er kort.
4. Meldingen går til redaktøren for basene. Adressen står i skillen `felles-intern`.

Si til brukeren at skillen kan brukes selv mens den vurderes, men at hver egen skill konkurrerer med de felles skillene om plassen i lista (se steg 1).

## Dokumentasjon

Hold én `endringslogg.md` ved siden av skillen. Én oppføring per endring med **Funn**, **Endring**, **Basert på**, **Ikke gjort ennå** og ved behov **Vurdert og forkastet** (bare når noen sannsynligvis vil foreslå det samme igjen). Skriv oppføringen før du retter.

## Når skills og baser virker sammen

Når en skill for språk eller kommunikasjon bearbeider et svar som bygger på regelverk eller tall, skal kildegrunnlaget fortsatt finnes i samme svar.
- **Internt eller fagpublikum:** kilden kan stå i teksten.
- **Lekfolk (svar til innbygger, pressemelding):** kilden står adskilt, f.eks. som en kort note under utkastet.
- Brukeren skal aldri få bare den ferdige teksten uten at kildegrunnlaget er tilgjengelig.

## Når et funn bør endre denne skillen

Si fra i samtalen når et funn gjelder hvordan neste skill, uansett tema, bør bygges, testes, lagres eller dokumenteres. Eksempler er en ny feiltype eller en ny begrensning i kjøremiljøet. Foreslå konkret hvilket avsnitt som bør endres, og vent på svar. Funn som bare gjelder skillen du bygger, hører hjemme i dens egen logg. Terskelen skal være høy.
