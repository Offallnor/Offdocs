---
name: "felles-analyse"
description: "Fast prosess for en større analyse med oppdragsbeskrivelse, kildegrunnlag fra de felles basene, kildevurdering, beslutningslogg og leveranse med vedlegg. Bruk bare når brukeren ber om en større analyse eller om denne prosessen, for eksempel «kjør en større analyse». Foreslå den gjerne når et spørsmål er stort og sammensatt, men start ikke før brukeren har sagt ja."
---

# Større analyser

**Versjon 2026-11-14.** Hent også `https://raw.githubusercontent.com/Offallnor/offdocs/main/SKILLVERSJONER.md`. Gjør det før noe annet. Står det en nyere versjon for denne skillen der, si det til brukeren i første svar, før oppdragsbeskrivelsen sjekkes: «**Ny versjon:** Det finnes en nyere versjon av analyseskillen. Siden analysen tar tid, anbefaler jeg at du sier "oppdater skillene" og starter analysen i en ny samtale etterpå. Vil du heller fortsette med denne versjonen, si fra.» Vent på svar før analysen starter. Si det bare én gang i samtalen. Står det et driftsvarsel der for et område analysen bygger på, si det i svakhetsvurderingen. Feiler hentingen, la det være.

Mange brukere er nye i KI. Snakk enkelt, og nevn ikke GitHub, repo, filstier eller feilkoder i svaret. Si for eksempel «regelverket», «statistikkatalogen» eller «budsjettdokumentene».

## Når skal denne kjøres?

Bare når brukeren har bedt om det. Prosessen er tung, og den koster tid. Virker et spørsmål stort nok, kan du foreslå den, men brukeren må selv si ja før du går videre. Et vanlig spørsmål om lov, tall eller budsjett besvares av de andre felles skillene, ikke av denne.

## Steg 1: Oppdragsbeskrivelsen

Analysen starter fra en ferdig oppdragsbeskrivelse. Har brukeren ingen, gi malen og tilby å fylle den ut sammen.

```
OPPDRAGSBESKRIVELSE

1. Problemstilling
   Spørsmålet analysen skal svare på, i én eller to setninger.

2. Bakgrunn
   Hvorfor spørsmålet stilles nå, og hva svaret skal brukes til.

3. Avgrensning
   Innenfor: hva som skal være med (ytelser, grupper, periode, land).
   Utenfor: hva som bevisst holdes utenfor.

4. Føringer på metode og kilder
   Kilder som skal eller ikke skal brukes, f.eks. bare forskning
   fra Norden, eller tall fra Nav og SSB. Skriv «ingen» hvis
   det ikke finnes føringer.

5. Målgruppe og presisjonsnivå
   Hvem analysen er til, og hvor grundig og formell den skal være.

6. Omfang og frist
   Ønsket lengde på hoveddokumentet, og når det trengs.
```

Minn brukeren på at r-notater, saksinnhold og personopplysninger ikke skal inn i oppdragsbeskrivelsen eller analysen. Analysen bygger på åpne kilder.

**Mangler punkt 1, 3 eller 5, stopp.** Si hva som mangler, i en form brukeren kan ta med tilbake dit oppdraget ble formulert. Dette er det eneste stedet prosessen stopper. En tung analyse på feil problemstilling er bortkastet.

Når oppdraget er godkjent, si kort hva som leveres (se «Leveranse»), slik at brukeren kan justere før arbeidet starter.

## Steg 2: Kildegrunnlaget fra de felles basene

Hent `https://raw.githubusercontent.com/Offallnor/offdocs/main/CLAUDE.md` med `curl -sL` i kodeverktøyet, eller med hentverktøyet ditt. Den sier hva som finnes og hvordan det hentes. Gå gjennom oppdraget og hent det som gjelder, før du søker andre steder:

| Analysen trenger | Hent |
|---|---|
| Hva lov, forskrift, rundskriv eller rettspraksis sier | Regelverket, via `CLAUDE.md` |
| Tall og statistikk | `data/VEIVISER.md` |
| Bevilgninger, Prop. 1 S, regnskap | `budsjett/VEIVISER.md` |
| NOU-er, meldinger, proposisjoner, strategier, tildelingsbrev | Dokumentbasen som `CLAUDE.md` viser til |
| Hva Stortinget har vedtatt, spurt om eller foreslått | `stortinget/VEIVISER.md` |
| Regjeringens prioriteringer | `politikk/VEIVISER.md` |
| Om forskningsspørsmålet er besvart før | `https://raw.githubusercontent.com/Offallnor/forskning/main/forskning/sporsmal/oversikt.tsv`, og svaret i mappen for spørsmålet |

Følg reglene i filene du henter: oppgi kilde med navn, skill mellom lov, utredning og politikk, og svar ikke fra hukommelsen. Bygger du på et tidligere forskningssvar, oppgi status og dato for søket slik det står i svaret.

Skriv i beslutningsloggen hvilke av basene som ble brukt, og hva de ikke dekket.

## Steg 3: Forskning og andre kilder

**Tidligere forskningssvar går foran eget søk.** De er laget etter en fast løype med kontrollerte tall. Finnes det et svar på spørsmålet (se steg 2), bygg på det, og søk bare etter det svaret ikke dekker.

**Er analysen avhengig av et forskningsspørsmål som ikke er besvart** (for eksempel «virker tiltaket»), si det til brukeren før du går videre. Har brukeren skillen `felles-forskning`, foreslå å kjøre spørsmålet der først. Ellers går analysen videre med det enklere søket under, og svakhetsvurderingen sier at spørsmålet ikke er gjennomgått like grundig som et fullt forskningssvar.

**Det enklere søket** under er ikke kvalitetssikret som løypa. Skriv det i svakhetsvurderingen, og merk i litteraturoversikten hvilke kilder som kommer fra eget søk.

Søk bredt for det basene ikke dekker. Rapporter og evalueringer bestilt av staten finnes ofte i Kudos (kudos.dfo.no) og i Navs bibliotek (bibliotek.nav.no). Systematiske oversikter og institusjonelle kilder (NOU, OECD, IZA og tilsvarende) teller som fullverdige kilder.

**Vurder studier om effekter etter design:**

1. oversikter, rangert etter studiene de bygger på
2. randomiserte forsøk
3. reformer og naturlige eksperimenter
4. registerstudier med håndtering av seleksjon
5. andre registerstudier

Design og troverdighet avgjør sammen. Metodenavnet er et utgangspunkt: en studie med et svakt argument for hvorfor sammenligningen er gyldig, rangeres lavere. For beskrivende spørsmål (utvikling, nivå, sammenligning mellom land) rangeres kildene etter datadekning: hele befolkningen først, deretter harmoniserte data på tvers av land, lange tidsserier, mindre utvalg og enkeltstudier.

For kilder som bærer resultatet: les metodedelen, ikke bare sammendraget. Oppgi hvilke kvalitetssignaler som er sjekket (fagfellevurdert, utvalgsstørrelse, replikert) og hvilke som ikke er det. Er grunnlaget tynt eller sprikende, si det. Flagg de metodiske premissene brukeren bør kontrollere selv.

## Steg 4: Metode og faktasjekk

- Vurder alternative tilnærminger før én velges. Der valget påvirker resultatet, skriv hvorfor.
- Tall, sitater og påstander skal kunne spores til kilde. Vis mellomregninger. Regn med kode når du har kodeverktøy, ikke i hodet.
- Logg alle valg, alternativer og konsekvenser fortløpende. Loggen stopper ikke arbeidet, den gås gjennom etter levering. Kilder som ble vurdert og forkastet, står i loggen, ikke i litteraturoversikten.

## Steg 5: Avsluttende kildesjekk

Kontroller hver kilde i litteraturoversikten før levering: at den finnes, at lenken virker, og at den handler om det den er brukt til. Dette fanger feilsiterte og forvekslede kilder. Det er ikke en kontroll av hver enkelt påstand.

## Leveranse

- **Hoveddokument:** problemstilling, kort om metode, resultat, konklusjon og svakhetsvurdering. Kort nok til å leses uten vedleggene.
- **Vedlegg A – Beslutningslogg:** valg, alternativer og konsekvens, og hvilke baser som ble brukt.
- **Vedlegg B – Litteraturoversikt:** kildene med lenke, type kilde og hvilke kvalitetssignaler som er sjekket.
- **Vedlegg C – Mellomregninger og metodedetaljer.**

Lever som egne filer, i formatet brukeren ber om (dokument, Word eller markdown). Et regneark tilbys ved levering når beregningene har flere trinn eller usikre forutsetninger, men lages ikke uoppfordret.

Avslutt i chatten med hovedresultatet, de to eller tre viktigste usikkerhetene og hvor videre arbeid gir mest. List opp filene som er levert.

Etter levering: avklar med brukeren om rettinger skal gjøres punktvis eller ved en ny kjøring.

## Hvis hentingen feiler

Fortsett ikke med analysen fra hukommelsen. Ser feilen ut som en sperre (for eksempel 403, «not allowed», «blocked» eller nektet tilkobling), si dette, med nettstedet fra adressen som feilet:

«Jeg fikk ikke hentet kildegrunnlaget, fordi Claude ikke har lov til å hente fra nettstedet [nettsted]. Du kan åpne for det selv: Gå til Innstillinger → Funksjoner. Under «Kodekjøring og filoppretting i skyen» skroller du ned til «Tillatelsesliste for domener» og legger til [nettsted]. Spør meg igjen etterpå, gjerne i en ny samtale. Har du Claude på engelsk, si fra, så får du navnene på engelsk.»

Ved andre feil: «Jeg fikk ikke hentet kildegrunnlaget nå. Prøv igjen litt senere.» Vil brukeren likevel gå videre, skriv i svakhetsvurderingen hvilke kilder som manglet.
