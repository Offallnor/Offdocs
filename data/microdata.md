# microdata.no

microdata.no er SSBs og Sikts tjeneste for egne analyser av registerdata på personnivå. Brukeren logger inn via sin institusjon og kjører analysen selv. Resultatene er bare aggregerte (tabeller, nøkkeltall, regresjoner og anonymiserte figurer), og enkeltdata kan ikke tas ut. Claude kan ikke logge inn eller kjøre noe i tjenesten, men kan foreslå en analyse og skrive et skriptutkast som brukeren kjører.

## Hva som ligger i basen

En kopi av variabelkatalogen og brukerveiledningen hentes hver mandag med jobben «Hent variabelkatalog og veiledning fra microdata.no» (`verktoy/microdata_hent.py`). Når kopien sist ble hentet og endret, står i `data/microdata/status.tsv`.

| Fil | Innhold |
|---|---|
| `data/microdata/variabler.tsv` | Én rad per variabel: navn, etikett, enhet (person, jobb, kommune …), temporalitet, datatype, måleenhet, første og siste dato med data, emner, antall koder, når variabelen sist ble oppdatert, versjon av databanken og beskrivelsen for siste periode |
| `data/microdata/kodelister/<NAVN>.tsv` | Gjeldende kodeliste (siste periode) for kategoriske variabler |
| `data/microdata/variabler/<NAVN>.json` | Hele variabelbeskrivelsen fra katalogen, med beskrivelse og kodeliste for hver periode. Kodelistene for senere perioder er lagret som endringer (`delta`: `remove`, `insert`, `replace`) fra perioden før |
| `data/microdata/manual/` | Brukerveiledningen som tekst, én fil per side. Start med `kommandoer-og-funksjoner/kommandoer.md` og `kommandoer-og-funksjoner/funksjoner.md` for syntaks, `konfidensialitet.md` for hva resultatene kan vise, og `eksempel/` for ferdige skript |

Datoene i JSON-filene er dager siden 1. januar 1970. I `variabler.tsv` er de gjort om til vanlige datoer.

Brukeren kan ofte lite eller ingenting om koding i microdata.no. Forslaget skal derfor kunne kjøres og forstås uten at brukeren må skrive kode selv.

## Sparring før skriptet

Skriv ikke skriptet før analysen er avklart med brukeren. Kommer forslaget som et kort utkast på slutten av et forskningssvar, start sparringen først når brukeren vil gå videre med det. Still ett spørsmål om gangen, og hopp over det som allerede er klart:

1. Hva skal tallene brukes til, og hvem skal lese dem?
2. Hvem er populasjonen, hva er utfallet, og hvilken periode gjelder det?
3. Hvilke grupper eller tidspunkter skal sammenlignes?

Oppsummer deretter opplegget med vanlige ord og be brukeren bekrefte det. De fleste analysene vil være beskrivende, og da er det nok.

**Når spørsmålet handler om virkninger** («virker tiltaket», «hva skyldes forskjellen»), eller brukeren virker åpen for det, si kort hva en beskrivende sammenligning kan og ikke kan si, og tilby å se på et sterkere opplegg. Registerdataene gjør det ofte mulig med for eksempel:
- kontroll for observerbare kjennetegn (regresjon med bakgrunnsvariabler), med forbehold om det som ikke er observert
- forskjeller-i-forskjeller rundt en regelendring (`data/microdata/manual/brukermanual/avansert-analyse/5.11-diff-in-diff-analyse.md`)
- regresjonsdiskontinuitet ved en alders- eller inntektsgrense i regelverket (`data/microdata/manual/brukermanual/avansert-analyse/5.12-regression-discontinuity-design-rdd.md`)
- paneldata med faste effekter, der de samme personene følges over tid (`data/microdata/manual/brukermanual/avansert-analyse/5.10-paneldata-analyse.md`)
- instrumentvariabler, når det finnes en kilde til variasjon som bare virker gjennom tiltaket (`data/microdata/manual/eksempel/regresjonsanalyser/bruk-av-instrumentvariabel-i-regresjonsanalyse.md`)

For hvert opplegg: si hvilken variasjon det utnytter, hva som må være oppfylt for at estimatet skal kunne tolkes som en virkning, og for hvem estimatet gjelder (for eksempel bare personer rundt aldersgrensen). Press ikke brukeren. Velger brukeren det beskrivende, gå videre med det.

## Slik lager du forslaget og skriptet

1. **Spørsmålet først.** Skriv populasjon, utfall, sammenligning og periode før du velger variabler. Beskriv med vanlige ord hvilke sammenhenger analysen ser på, og hvilken variasjon den eventuelt utnytter (for eksempel forskjeller mellom grupper, en regelendring på en bestemt dato eller en aldersgrense), og hva som må være oppfylt for at det skal gi et riktig bilde. Si om analysen kan beskrive (nivå, utvikling, fordeling) eller bare antyde sammenhenger. En enkel sammenligning viser ikke effekt.
2. **Variabler bare fra katalogen.** Hvert variabelnavn i forslaget skal stå i `data/microdata/variabler.tsv`. Sjekk at perioden spørsmålet gjelder, ligger mellom `fra` og `til`, og at enheten passer (en variabel med enhet «Jobb» må aggregeres før den kobles til personer). Står variabelen ikke i katalogen, si det. Ikke gjett navn. Beløpsgrenser i G (for eksempel inntekt over 2 G) regnes om med G fra `data/grunnbelop.tsv`, ikke fra hukommelsen: gjennomsnittlig G for inntekt over et helt år, og G på datoen for regler som gjelder fra en dato.
3. **Temporalitet styrer importen.** `STATUS` (tverrsnitt) importeres på en dato, `ACCUMULATED` gjelder et tidsrom (for eksempel inntekt for et år), `EVENT` er forløp med start og slutt, og `FIXED` endrer seg ikke (for eksempel fødselsår). For `STATUS`-variabler står datoene det finnes tall for, i `temporalStatusDates` i JSON-filen (dager siden 1970-01-01). Bruk en av dem, ikke en antatt dato. Se veiledningen om tverrsnitts- og hendelsesdatasett før du skriver `import`.
4. **Kodelister.** Bruk koder fra `data/microdata/kodelister/` og sjekk i JSON-filen om kodelista har endret seg i perioden. Brudd i kodelista kan gi brudd i serien.
5. **Kommandoer bare fra veiledningen.** Skriptspråket ligner Stata, men er ikke det samme. Bruk bare kommandoer, opsjoner og funksjoner som står i `kommandoer-og-funksjoner/`. Følg eksemplene i `eksempel/` når de passer.
6. **Konfidensialitet.** Les `konfidensialitet.md` før du planlegger tabeller og grupper. Blant tiltakene: populasjonen må ha minst 1 000 personer, numeriske variabler winsoriseres (1 prosent i hver ende), alle opptellinger får tilfeldig støy (verdiene 1–4 vises aldri), en tabell stoppes når mer enn halvparten av cellene har under 5, og spredningsplott vises bare som hexbin. Velg grupperinger som gir mange personer per celle, og si at tallene kan avvike litt fra offisiell statistikk.
7. **Velg modeller som er lette å tolke.** For utfall som er ja/nei (i jobb eller ikke), bruk som hovedregel en lineær sannsynlighetsmodell (`regress` med `robust`). Varierer tiltaket eller instrumentet mellom grupper, for eksempel kommuner eller år, bruk `cluster()` med gruppen i stedet, og si med én setning hvorfor: personer i samme gruppe har felles variasjon, og `robust` gir da for små standardfeil. Koeffisientene leses da direkte som forskjeller i prosentpoeng. Den fungerer godt i hoveddelen av dataene, men ikke for å predikere langt ute i halene. Bruk ikke-lineære modeller (`logit`, `probit`) bare når det er en grunn til det, og vis da marginaleffekter eller predikerte sannsynligheter, ikke koeffisienter eller oddsforhold.
8. **Pedagogisk visning i selve kjøringen.** Skriptet skal vise hovedresultatene slik at de kan leses uten statistikkunnskap. Bruk `textblock` foran hvert steg til å forklare med vanlige ord hva steget gjør og hvordan resultatet skal leses. Vis hovedtallene som andeler i prosent eller prosentpoeng (gang 0/1-variabler med 100 før du viser gjennomsnittet) i enkle tabeller (`tabulate` med prosent) og figurer (`barchart`) før eventuelle regresjoner, og forklar regresjonsresultatene med en setning per hovedkoeffisient. Kommenter hver kommando kort.
9. **Merk utkastet.** Skriv at skriptet ikke er kjørt, hvilken versjon av katalogen det bygger på (dato fra `status.tsv`), lenk til sidene i brukerveiledningen du har bygget på (`kilde:` øverst i filen), og at brukeren bør kjøre små tellinger først for å sjekke populasjonen. Feilmeldinger fra microdata.no kan limes inn, så retter du skriptet.

## Sjekkliste før du viser skriptet

Gå gjennom lista når skriptet er skrevet, og rett det som mangler før brukeren ser det. Testene har vist at steg i oppskriften lett blir hoppet over.

- [ ] Opplegget er oppsummert med vanlige ord, og brukeren har bekreftet det etter siste endring.
- [ ] `data/VEIVISER.md` og `SKILLVERSJONER.md` er lest, også når du kom hit fra et forskningssvar.
- [ ] `konfidensialitet.md` er lest i sin helhet, og veiledningen om tverrsnitts- og hendelsesdatasett er lest før `import`.
- [ ] Hver variabel står i `variabler.tsv`, og perioden ligger mellom `fra` og `til`.
- [ ] Hver `STATUS`-import bruker en dato fra `temporalStatusDates` i JSON-filen.
- [ ] Hver kode i `if`, `keep` og `recode` er slått opp i kodelista, ikke tatt fra hukommelsen.
- [ ] Hver kommando, opsjon og funksjon står i `kommandoer-og-funksjoner/` eller i et eksempel. Det som ikke gjør det, er merket i svaret.
- [ ] Beløp i G er regnet med `data/grunnbelop.tsv`.
- [ ] Ja/nei-utfall bruker `regress` med `robust`, eller `cluster()` med begrunnelse.
- [ ] Andeler vises i prosent, og hver hovedkoeffisient er forklart med én setning i prosentpoeng.
- [ ] Svaret sier at skriptet ikke er kjørt, hvilken katalogversjon det bygger på, og lenker til brukerveiledningen.

## Forbehold

- Katalogen hentes fra nettsiden microdata.no/discovery, som ikke har et dokumentert grensesnitt. Endres siden, stopper hentingen med et driftsvarsel. Kopien i basen er da den siste som ble hentet.
- Noe av veiledningen er skjermbilder (for eksempel feilmeldinger og figurer). De står som `[bilde](lenke)` i tekstfilene, og innholdet i dem er ikke med.
- Veiledningen er SSBs og Sikts tekst. Vis til den med navn («brukerveiledningen for microdata.no») og lenke til siden (`kilde:` øverst i hver fil).
- Tilgang krever avtale mellom institusjonen og microdata.no. Se microdata.no/bli-bruker.
