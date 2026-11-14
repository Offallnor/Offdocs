---
name: "felles-dokumenter"
description: "Offentlige dokumenter om utdanning, arbeid og velferd: NOU-er, stortingsmeldinger, lovproposisjoner, strategier, handlingsplaner og tildelingsbrev til etatene (Nav, IMDi, Arbeidstilsynet, Lånekassen, HK-dir, universiteter og høyskoler). Bruk ved spørsmål om hva et dokument sier, foreslår eller pålegger, også når det omtales med kortnavn (integreringsmeldingen, arbeidsmarkedsmeldingen, perspektivmeldingen, pensjonsmeldingen) eller etter utvalget (hva foreslo Lavlønnsutvalget), f.eks. «hovedbudskapet i …-meldingen», «hva står i tildelingsbrevet til Nav», «forarbeidene til lovendringen». Ikke for gjeldende lovtekst (felles-regelverk) eller bevilgninger i Prop. 1 S (felles-budsjett). Last den før nettsøk, og svar ikke fra hukommelsen."
---

# Dokumenter om utdanning, arbeid og velferd

**Versjon 2026-11-14.** Hent også `https://raw.githubusercontent.com/Offallnor/offdocs/main/SKILLVERSJONER.md`. Står det en nyere versjon for denne skillen der, avslutt svaret med en skillelinje og denne linjen, etter eventuelle kilder: «**Ny versjon:** Det finnes nyere versjoner av de felles skillene. Si "oppdater skillene" for å få dem.» Si det bare én gang i samtalen. Står det et driftsvarsel der for et område svaret bygger på, si kort aller først i svaret, før selve svaret, at det nyeste fra kilden kan mangle. Feiler hentingen, la det være.

Dokumentene ligger ikke i denne skillen. De ligger i en felles base på GitHub og hentes ved hvert oppslag. Hva basen dekker, står i basen.

## Fremgangsmåte

1. **Sjekk basen før nettsøk.** Søk ikke på nettet før du har sett etter dokumentet i basen, heller ikke når du kjenner dokumentet fra før.
2. Hent `https://raw.githubusercontent.com/Offallnor/offdocsfor/main/CLAUDE.md` med `curl -sL` i kodeverktøyet, eller med hentverktøyet ditt. Følg den. Hent deretter `VEIVISER.md` fra samme sted.
3. Finn dokumentet. Brukerne omtaler ofte dokumenter med kortnavn («integreringsmeldingen», «arbeidsmarkedsmeldingen») eller etter utvalget («Lavlønnsutvalget»), mens lista har nummeret («Meld. St. 17 (2023–2024)»). Søk derfor også på emneord i sammendraget og i `dokumenter.tsv`. Tildelingsbrev finnes på mottaker og år.
4. Åpne hovedfila og bare delen eller delene du trenger. Svar med kildehenvisning etter reglene i CLAUDE.md, og si hvilken type dokument det er.
5. **Nettsøk etterpå, bare for det som er nyere.** Har det skjedd noe etter dokumentet (for eksempel en ny strategi eller en senere avtale), kan du søke på nettet for å supplere. Si da tydelig hva som kommer fra dokumentet, og hva som kommer fra nettsøket.
6. **Finnes ikke dokumentet i basen,** følg regel 5 i CLAUDE.md.
7. **Gjelder spørsmålet hva loven sier nå,** bruk skillen `felles-regelverk`. Gjelder det bevilgninger i Prop. 1 S, bruk `felles-budsjett`. Har brukeren ikke disse skillene, hent `https://raw.githubusercontent.com/Offallnor/offdocs/main/CLAUDE.md` og følg den.
8. **Spør brukeren hva basen inneholder, eller har brukeren funnet en feil eller noe som mangler,** hent `https://raw.githubusercontent.com/Offallnor/offdocs/main/OM-BASENE.md` og følg den. Meldinger om feil, mangler og ønsker går på e-post til redaktøren for basene. Adressen står i skillen `felles-intern`.
9. Hvis hentingen feiler: se «Hvis hentingen feiler» under.

## Hvis hentingen feiler

Svar ikke fra hukommelsen. Ser feilen ut som en sperre (for eksempel 403, «not allowed», «blocked» eller nektet tilkobling), si dette, med nettstedet fra adressen som feilet:

«Jeg fikk ikke hentet dokumentet, fordi Claude ikke har lov til å hente fra nettstedet [nettsted]. Du kan åpne for det selv: Gå til Innstillinger → Funksjoner. Under «Kodekjøring og filoppretting i skyen» skroller du ned til «Tillatelsesliste for domener» og legger til [nettsted]. Spør meg igjen etterpå, gjerne i en ny samtale. Har du Claude på engelsk, si fra, så får du navnene på engelsk.»

Ber brukeren om engelske navn, eller skriver brukeren på engelsk, bruk Settings → Capabilities, «Code execution and file creation» og listen over tillatte domener lenger ned på siden. Nettstedsnavnet er det eneste tekniske ordet som skal stå i svaret.

Ved andre feil: «Jeg fikk ikke hentet dokumentet nå. Prøv igjen litt senere.»
