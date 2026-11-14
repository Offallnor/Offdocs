---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/kom-i-gang-med-ki/test-ki-systemet"
hentet: "2026-11-14"
---

# 3. Teste og evaluere

1. [Planlegg testen](https://ki.norge.no/veiledning/kom-i-gang-med-ki/planlegg-testen)
2. [Test KI-systemet](https://ki.norge.no/veiledning/kom-i-gang-med-ki/test-ki-systemet)
3. [Analyser resultatene](https://ki.norge.no/veiledning/kom-i-gang-med-ki/analyser-resultatene)

## Test KI-systemet

Det er viktig å skille mellom to typer målinger som ofte forveksles, benchmark og domenespesifikke evalueringer

**Benchmark** handler om å måle ytelsen til modellen. Det er standardiserte tester som leverandøren selv eller tredjeparts forskere kjører på en rekke generelle oppgaver, for eksempel «Løs denne matteoppgaven», «Oversett denne teksten» eller «Finn feilen i denne koden». Benchmarks måler ofte generell intelligens, ikke spesifikk fagkompetanse.

**Domenespesifikke evalueringer** er laget av fagfolk, basert på reelle oppgaver og data fra en virksomhets hverdag. Evalueringer måler ytelse i den konkrete situasjonen modellen skal brukes i. De svarer for eksempel på spørsmålet: «Kan denne modellen håndtere en søknad om barnetrygd korrekt?» Man lager et datasett med inndata, for eksempel 50 søknader, og forventet utdata, korrekte svar på søknadene. Modellen kjører på dette, og resultatet sammenlignes med «fasiten».

### Evalueringer best til å teste reelle oppgaver

En modell som scorer høyt på generelle benchmarks, kan likevel feile når den skal tolke norsk forvaltningslov eller kommunale retningslinjer. Det gjør at benchmarks er bra for en grov sammenligning av modeller, men det er ikke et tilstrekkelig grunnlag for beslutning om hvilken modell deres virksomhet skal bruke..

Evalueringer er et nyttigere verktøy for å vurdere om en modell egner seg for din virksomhet og gode parametere for å velge mellom de ulike modellene som er på markedet. Men det er avgjørende at evalueringssettet har data som er relevante for virksomheten.

### Sjekk ulike testmuligheter

Mange leverandører tilbyr testmiljøer hvor du kan laste opp data og teste uten at data lagres

Du kan også vurdere å samarbeid med andre kommuner eller fylkeskommuner for å teste løsninger sammen.

Ulike forskningsmiljø kan bistå med å sette opp testmiljø, som Simulas Centre for AI Security and Safety. De har utviklet et åpent evalueringsrammverk for KI modeller, Simple Audit, som er tilgjengelig på GitHub.

[Gå til Simulas Centre for AI Security and Safety](https://www.simula.no/research/research-centres/caiss-centre-ai-security-and-safety)

[Se evalueringsrammeverket på GitHub](https://github.com/kelkalot/simpleaudit)

### Eksempel

Du trenger ikke være utvikler eller data scientist for å vurdere om en KI-modell egner seg i din virksomhet. Det handler først og fremst om å forstå hvordan modellen oppfører seg i praksis.

For eksempel kan du kjøre en enkel, strukturert test i egen virksomhet. Start med å samle et sett med konkrete problemstillinger fra din arbeidshverdag. Dette bør være saker eller spørsmål du allerede kjenner svaret på, eller enkelt kan verifisere mot pålitelige kilder, som lovverk eller lignende vedtak. Be deretter modellen besvare alle spørsmålene, og vurder resultatene langs fire sentrale akser:

1. Hvor nøyaktig er modellen? Gå gjennom svarene og registrer hvor mange som er korrekte. Vurder også hva som er tilstrekkelig nivå basert på risikoen i bruken. For juridiske vurderinger kreves svært høy nøyaktighet, mens enklere oppgaver som oppsummeringer kan tåle noe lavere presisjon.

2. Graden av hallusinering. Identifiser hvor mange ganger modellen oppgir informasjon som ikke kan bekreftes, for eksempel oppdiktede paragrafer eller fakta. I saksbehandling i offentlig sektor bør denne andelen være nær null.

3. Konsekvente svar er også viktig. For stor variasjon i svar er utfordrende for rettsikkerheten. Still noen av de samme spørsmålene flere ganger, og vurder om svarene er like.

4. Vurder begrunnelser og graden av etterprøvbarhet. Se på om modellen forklarer hvordan den har kommet frem til svaret, og om den viser til relevante regler eller kilder. Vurder om begrunnelsene gjør det mulig å kontrollere og kvalitetssikre resultatene i etterkant.

5. Dokumenter funnene enkelt, for eksempel ved å angi andel korrekte svar, andel hallusinasjoner, grad av konsistens og kvalitet på begrunnelser. Dette gir et konkret grunnlag for å vurdere om modellen er egnet for deres formål.

[Neste stegAnalyser resultatene](https://ki.norge.no/veiledning/kom-i-gang-med-ki/analyser-resultatene)
