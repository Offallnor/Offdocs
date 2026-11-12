# Folketrygdloven: veiviser

Folketrygdloven regulerer medlemskap i folketrygden og ytelsene derfra: dagpenger, sykepenger, pleiepenger, arbeidsavklaringspenger, uføretrygd, foreldrepenger, stønad til enslig mor eller far, ytelser ved dødsfall, alderspensjon, grunnstønad, hjelpestønad og hjelpemidler. Den har også felles regler om saksbehandling, utbetaling og tilbakekreving. Over 50 forskrifter utfyller loven, blant annet dagpengeforskriften, uføretrygdforskriften, forskrift om alderspensjon og den årlige forskriften om grunnbeløp og satser.

Ansvaret for loven er delt mellom flere departementer. Kapittel 5 (stønad ved helsetjenester) hører til Helse- og omsorgsdepartementet, kapittel 14 (foreldrepenger og engangsstønad) til Barne- og familiedepartementet, og kapittel 23 og 24 (finansiering og avgifter) til Finansdepartementet. Resten av loven forvaltes av Arbeids- og inkluderingsdepartementet, blant annet kapittel 15 (stønad til enslig mor eller far). «Forvaltes av» i kildelisten under gjelder hele loven og sier ikke hvem som har ansvaret for det enkelte kapitlet.

Noen forskrifter under loven forvaltes av andre departementer enn loven: A-trygdforskriften (Nærings- og fiskeridepartementet), tre forskrifter om nedsettelse av pensjonsgivende inntekt mv. (Finansdepartementet), forskriften om disponering av kontantytelser under institusjonsopphold (Helse- og omsorgsdepartementet) og forskriften om utvidet stønad til helsetjenester under opphold i utlandet (sammen med Helse- og omsorgsdepartementet). Se kildelisten under.

Merknadene i basen dekker ikke kapittel 5, 14, 23 og 24, men NAVs rundskriv til dem ligger i basen (se under).

## Slik bruker du veiviseren

Finn paragrafen i listen under «Innhold», og åpne filen før du svarer. Merknadene under er hjelp til å unngå vanlige feil. De er ikke en offisiell tolkning.

Merknadsfilene er flyttet fra de gamle ftrl-skillene og er delt etter ytelse. Bruk tabellen nederst til å finne riktig fil.

NAVs rundskriv ligger i `rundskriv/` og dekker nesten hele loven. Rundskriv er forvaltningspraksis, ikke lov. Skill i svaret mellom det som står i loven eller forskriften og det NAV legger til grunn i rundskrivet. Rundskrivene kan være eldre enn lovteksten, så sjekk datoen i rundskrivfilen, og vær forsiktig med satser og beløp. Er en paragraf opphevet eller endret etter rundskrivets dato, gjelder lovteksten. Rundskrivene hentes hver uke fra Nav rettskilder hos Lovdata, så de følger Navs siste versjon. Datoen rundskrivet sist ble endret hos Nav, står i oversikten øverst i hver rundskrivfil. De ligger i to mappestrukturer:

- `rundskriv/rundskriv-<kode>/` for rundskriv til loven, med Navs dokumentnummer i mappenavnet: `rundskriv-r08-00/` for kapittel 8, `rundskriv-r05-07/` for § 5-7, `rundskriv-r10-07b/` for § 10-7 bokstav b. Hver mappe har `oversikt.md`, `innledning.md` og `par-X-Y.md` per paragraf. Kapittel 3 har tilleggsdeler `rundskriv-r03-01` til `r03-04`, og kapittel 5 har ett rundskriv per paragraf. Kapittel 5, 23 og 24 hører til andre departementer (se over), men rundskrivene ligger i basen. Navs kommentarer til forskrifter som ikke er i basen, ligger også her (for eksempel `rundskriv-r11a-00-for/` til tilleggsstønadsforskriften).
- `rundskriv/forskrifter/<forskrift>/` for Navs kommentarer til forskrifter som ligger i basen. Mappenavnet er det samme som forskriftens mappe under `forskrifter/`, og `par-N.md` er nummerert etter forskriften, ikke loven.

Ikke gjett stien. Slå opp paragrafen i `indeks.tsv` på roten, der alle rundskrivfilene står med sti (dokumentet heter «Rundskriv»), eller les `oversikt.md` i mappen. Lange kommentarer til én paragraf er ikke delt videre, så søk i filen.

| Tema | Les |
|---|---|
| Medlemskap, trygdetid, pensjonsgivende inntekt, omsorgspoeng, grunnbeløp (kap. 1–3) | Rundskriv `rundskriv/rundskriv-r01-00/`, `r02-00/`, `r03-00/` (og `r03-01` til `r03-04`), Navs kommentarer til omsorgspoengforskriftene i `rundskriv/forskrifter/omsorgspoeng/` og `rundskriv/forskrifter/omsorgspoeng-omsorgsarbeid/` |
| Stønad ved helsetjenester (kap. 5) | `rundskriv/rundskriv-r05-00/` (§ 5-1) og ett rundskriv per paragraf, for eksempel `rundskriv/rundskriv-r05-07/` (psykolog) og `rundskriv/rundskriv-r05-14-02/` (legemidler) |
| Dagpenger, permittering, minsteinntekt (kap. 4) | `merknader/dagpenger.md`, rundskriv `rundskriv/rundskriv-r04-00/` |
| Dagpenger og arbeid eller bosted i et annet EØS-land | `regelverk/eu/forordning-883-2004/merknader/dagpenger.md` fra roten (forordningsteksten er på engelsk), og R45 kapittel 4 |
| Alle ytelser ved bosted, arbeid eller trygdetid i et annet EØS-land, medlemskap og lovvalg i EØS | Navs EØS-rundskriv R45-00: `regelverk/eu/forordning-883-2004/rundskriv/r45-00/oversikt.md` fra roten (kapittel 2 for medlemskap og lovvalg, ellers samme kapittelnummer som i loven) |
| Dagpenger ved konkurs, lønnsgaranti | `regelverk/lonnsgarantiloven/VEIVISER.md` |
| Grunnstønad og hjelpestønad (kap. 6) | Rundskriv `rundskriv/rundskriv-r06-00/` |
| Hjelpestønad ved en bestemt diagnose | `rundskriv/rundskriv-r06-04-for/oversikt.md` (R06-04-FOR, ti diagnoser, gjelder § 6-4 og § 6-5 og supplerer kommentarene i R06-00) |
| Gravferdsstønad, båretransport, omstillingsstønad, barnepensjon (kap. 7, 16, 17, 17 A, 18) | `merknader/etterlatte-gravferd.md`, rundskriv `rundskriv/rundskriv-r07-00/` (gravferd, satsen kan være gammel), `r16-00/`, `r17-00/`, `r18-00/` |
| Sykepenger, omsorgspenger, pleiepenger, opplæringspenger (kap. 8 og 9) | `merknader/sykepenger.md`, forskriftene om sykepengeforsikring (`forskrifter/forsikring-arbeidsgiverperioden/`, `forskrifter/forsikring-sykepenger-selvstendige/`, `forskrifter/forsikring-sykepenger-frilansere/`), legeerklæring fra kiropraktor og manuellterapeut, opplæring i sykmeldingsarbeid og gradering av pleiepenger, rundskriv `rundskriv/rundskriv-r08-00/` og `rundskriv/rundskriv-r09-00/` |
| Tilskudd til ekspertbistand ved langvarig eller hyppig sykefravær (§ 8-7 a) | Forskrift om tilskudd til ekspertbistand i `forskrifter/ekspertbistand/`, rundskrivet til § 8-7 a i `rundskriv/rundskriv-r08-00/`, og NAVs rundskriv til forskriften (R08-07A-FOR, én fil per forskriftsparagraf), start med `rundskriv/forskrifter/ekspertbistand/oversikt.md`. Rundskrivet kommenterer ikke § 9a om forsøk med anskaffelse |
| Hjelpemidler, tolk, bil, høreapparat, briller til barn (kap. 10) | Forskriftene i `forskrifter/hjelpemidler/`, `lese-sekretarhjelp/`, `tolkehjelp-horselshemmede/`, `tolke-ledsagerhjelp-dovblinde/`, `ortopediske-hjelpemidler/`, `horeapparat/`, `motorkjoretoy/` og `briller-barn/`. Rundskriv `rundskriv/rundskriv-r10-00/` (ingen kommentar til § 10-4 eller § 10-7) |
| Stønadsformene i § 10-7 | Ett rundskriv per stønadsform under `rundskriv/`: `rundskriv-r10-07a/` (bokstav a, aktivitetshjelpemidler over 26 år), `rundskriv-r10-07acd/` (bokstav a, c og d og annet og tredje ledd; les begge ved spørsmål om bokstav a, og bare denne for c og d), `rundskriv-r10-07b/` (høreapparat), `rundskriv-r10-07e/` (lese- og sekretærhjelp), `rundskriv-r10-07f/` (tolkehjelp for hørselshemmede), `rundskriv-r10-07g/` (tolke- og ledsagerhjelp for døvblinde), `rundskriv-r10-07h/` (motorkjøretøy), `rundskriv-r10-07i/` (ortopediske hjelpemidler), `rundskriv-r10-07-for/` (servicehund), `rundskriv-r10-07/` (reiseutgifter) og `rundskriv-r10-07-4-5-ledd/` (fjerde og femte ledd) |
| Arbeidsavklaringspenger og tilleggsstønader (kap. 11 og 11 A) | Forskrift om arbeidsavklaringspenger i `forskrifter/arbeidsavklaringspenger/`, `merknader/aap.md`, rundskriv `rundskriv/rundskriv-r11-00/` og `rundskriv/rundskriv-r11a-00/`, Navs kommentarer til tilleggsstønadsforskriften i `rundskriv/rundskriv-r11a-00-for/` |
| Uføretrygd (kap. 12) | `merknader/uforetrygd.md` (forskriftene og kommentarene til dem), institusjonsforskriftene i `forskrifter/uredusert-ytelse-institusjon/`, `forskrifter/uforetrygd-institusjon/` og `forskrifter/overgangsregler-institusjon/`, rundskriv `rundskriv/rundskriv-r12-00/` og forskriftskommentarer (se merknaden) |
| Yrkesskade og yrkessykdom (kap. 13) | Rundskriv `rundskriv/rundskriv-r13-00/`, Navs kommentarer til yrkessykdomsforskriften i `rundskriv/forskrifter/yrkessykdommer/` |
| Svangerskapspenger, foreldrepenger, engangsstønad (kap. 14) | Rundskriv `rundskriv/rundskriv-r14-00/` |
| Stønad til enslig mor eller far (kap. 15) | Rundskriv `rundskriv/rundskriv-r15-00/` (aktivitetskravet i § 15-6 er opphevet fra 1. juli 2026) |
| Alderspensjon (kap. 19 og 20) | Rundskriv `rundskriv/rundskriv-r19-00/` og `r20-00/`. Pensjon fra staten og samordning med folketrygden: `regelverk/spk-loven/VEIVISER.md`, `regelverk/samordningsloven/VEIVISER.md`, `regelverk/afp-loven/VEIVISER.md` |
| Saksbehandling, klage og anke (kap. 21) | Rundskriv `rundskriv/rundskriv-r21-00/` |
| Utbetaling, tilbakekreving, foreldelse, Aa-registeret (kap. 22, 25, 26) | Rundskriv `rundskriv/rundskriv-r22-00/`, `r25-00/` og `r26-00/`, Navs kommentarer til forskriftene om Aa-registeret og arbeidsgivers opplysningsplikt i `rundskriv/forskrifter/aa-registeret/` og `rundskriv/forskrifter/opplysningsplikt-arbeidsgiver/` |
| Permisjon ved fødsel og sykdom i familien | `regelverk/arbeidsmiljoloven/VEIVISER.md` |
| NAV-kontoret og etatens organisering | `regelverk/nav-loven/VEIVISER.md` |
| Økonomisk sosialhjelp (subsidiær til folketrygdytelser) | `regelverk/sosialtjenesteloven/VEIVISER.md` |

<!-- AUTO-START: genereres av verktoy/bygg.py, ikke rediger for hånd -->
## Kilder

- **Lov:** Lov om folketrygd (folketrygdloven) – LOV-1997-02-28-19. Sist endret i kraft: 2026-10-01. Forvaltes av: Arbeids- og inkluderingsdepartementet.
- **Forskrifter:** 77 forskrifter. Lovdata-ID, sist endret i kraft og hvem som forvalter dem, står i `innhold/kilder.md`.

## Tolkningskilder i basen

Dette er ikke lov- eller forskriftstekst. Oppgi kilden med navn i svaret. Listen lages fra mappene ved hvert bygg. Andre tolkningskilder til regelverket er ikke i basen. Hovedtariffavtalen og EU-rettsaktene har egne veivisere.

- Navs rundskriv (R01-00, R02-00, R03-00, R03-01, R03-02, R03-03, R03-04, R04-00, R05-00, R05-01a, R05-02, R05-03 og 61 til) og Navs kommentarer til forskrifter – se «Rundskriv» under «Andre kilder» nederst
- Høyesteretts avgjørelser fra november 2021 (rettspraksis) (18 filer) – start med `rettspraksis/hoyesterett/oversikt.md`
- Sivilombudets uttalelser (74 filer) – start med `rundskriv/sivilombudet/oversikt.md`

## Vedtatte endringer som ikke er i kraft

Fra Norsk Lovtidend. Teksten i paragraffilene er gjeldende tekst; ny ordlyd står i filene under.

- **Endringslov til trygderettsloven mv.** (LOV-2025-06-20-38). Ikrafttredelse: Kongen bestemmer. Satt i kraft ved FOR-2025-06-20-1113 (Delt ikraftsetting av lov 20. juni 2025 nr. 38 om endringer i trygderettsloven mv. (ankeerklæring til Trygderetten, avgjørelse innen seks måneder mv.)): 2026-01-01, 2027-01-01. Bare deler av endringene er satt i kraft. Sjekk vedtaket for hvilke deler som gjelder. Endrer: § 21-12. Ny tekst: `vedtatte-endringer/lov-2025-06-20-38.md`
- **Barnelova** (LOV-2025-06-20-40). Ikrafttredelse: Kongen bestemmer, og tidspunktet er ikke fastsatt i Lovtidend ennå. Endrer: § 14-5, § 14-17, § 15-4, § 23-1, § 23-10. Ny tekst: `vedtatte-endringer/lov-2025-06-20-40.md`
- **Forskrift om endring i forskrift om stønad til høreapparat og tinnitusmaskerer** (FOR-2026-09-21-2199). Trer i kraft 2027-01-01. Endrer: Forskrift om stønad til høreapparat og tinnitusmaskerer. Ny tekst: `vedtatte-endringer/for-2026-09-21-2199.md`

## Innhold

Innholdslisten er delt fordi regelverket er stort. Finn kapitlet eller forskriften under, åpne innholdsfilen, og åpne deretter paragraffilen. Stiene i innholdsfilene er relative til `regelverk/folketrygdloven/`.

### Folketrygdloven

- Kapittel 1. Formål og definisjoner m.m. (§§ 1-1 til 1-10, 12 paragrafer) – `innhold/lov-kapittel-1.md`
- Kapittel 2. Medlemskap (§§ 2-1 til 2-17, 19 paragrafer) – `innhold/lov-kapittel-2.md`
- Kapittel 3. Visse beregningsregler, trygdetid, pensjonspoeng og pensjonsgivende inntekt (§§ 3-1 til 3-30, 30 paragrafer) – `innhold/lov-kapittel-3.md`
- Kapittel 4. Dagpenger under arbeidsløshet (§§ 4-1 til 4-28, 29 paragrafer) – `innhold/lov-kapittel-4.md`
- Kapittel 5. Stønad ved helsetjenester (§§ 5-1 til 5-26, 30 paragrafer) – `innhold/lov-kapittel-5.md`
- Kapittel 6. Grunnstønad og hjelpestønad (§§ 6-1 til 6-9, 10 paragrafer) – `innhold/lov-kapittel-6.md`
- Kapittel 7. Stønad ved gravferd (§§ 7-1 til 7-5, 6 paragrafer) – `innhold/lov-kapittel-7.md`
- Kapittel 8. Sykepenger (§§ 8-1 til 8-55, 57 paragrafer) – `innhold/lov-kapittel-8.md`
- Kapittel 9. Stønad ved barns og andre nærståendes sykdom (§§ 9-1 til 9-17, 19 paragrafer) – `innhold/lov-kapittel-9.md`
- Kapittel 10. Stønad for å kompensere for utgifter til bedring av arbeidsevnen og funksjonsevnen i dagliglivet (§§ 10-1 til 10-18, 20 paragrafer) – `innhold/lov-kapittel-10.md`
- Kapittel 11. Arbeidsavklaringspenger (§§ 11-1 til 11-31, 33 paragrafer) – `innhold/lov-kapittel-11.md`
- Kapittel 11 A. Tilleggsstønader til arbeidsrettede tiltak (§§ 11 A-1 til 11 A-5, 6 paragrafer) – `innhold/lov-kapittel-11a.md`
- Kapittel 12. Uføretrygd (§§ 12-1 til 12-21, 22 paragrafer) – `innhold/lov-kapittel-12.md`
- Kapittel 13. Yrkesskadedekning (§§ 13-1 til 13-17, 18 paragrafer) – `innhold/lov-kapittel-13.md`
- Kapittel 14. Ytelser ved svangerskap, fødsel og adopsjon (§§ 14-1 til 14-18, 20 paragrafer) – `innhold/lov-kapittel-14.md`
- Kapittel 15. Stønad til enslig mor eller far (§§ 15-1 til 15-13, 14 paragrafer) – `innhold/lov-kapittel-15.md`
- Kapittel 16. (Opphevet) (§§ 16-1 til 16-12, 13 paragrafer) – `innhold/lov-kapittel-16.md`
- Kapittel 17. Ytelser til gjenlevende ektefelle og tidligere familiepleier (§§ 17-1 til 17-15, 17 paragrafer) – `innhold/lov-kapittel-17.md`
- Kapittel 17 A. Overgangsregler for gjenlevende ektefelle og tidligere familiepleier som har rett til ytelse med virkning før 1. januar 2024 (§§ 17 A-1 til 17 A-8, 9 paragrafer) – `innhold/lov-kapittel-17a.md`
- Kapittel 18. Barnepensjon (§§ 18-1 til 18-10, 11 paragrafer) – `innhold/lov-kapittel-18.md`
- Kapittel 19. Alderspensjon (§§ 19-1 til 19-22, 26 paragrafer) – `innhold/lov-kapittel-19.md`
- Kapittel 20. Ny alderspensjon (§§ 20-1 til 20-23, 26 paragrafer) – `innhold/lov-kapittel-20.md`
- Kapittel 21. Saksbehandling i trygdesaker. Anke- og klagebehandling m.m. (§§ 21-1 til 21-17, 25 paragrafer) – `innhold/lov-kapittel-21.md`
- Kapittel 22. Utbetaling (§§ 22-1 til 22-19, 26 paragrafer) – `innhold/lov-kapittel-22.md`
- Kapittel 23. Finansiering (§§ 23-1 til 23-11, 13 paragrafer) – `innhold/lov-kapittel-23.md`
- Kapittel 24. Saksbehandling i avgiftssaker m.m. (§§ 24-1 til 24-5, 6 paragrafer) – `innhold/lov-kapittel-24.md`
- Kapittel 25. Forskjellige bestemmelser (§§ 25-1 til 25-19, 24 paragrafer) – `innhold/lov-kapittel-25.md`
- Kapittel 26. Ikrafttredelse og overgangsbestemmelser. Endringer i andre lover (§§ 26-1 til 26-3, 3 paragrafer) – `innhold/lov-kapittel-26.md`
- Innhold utenfor paragrafene: Vedlegg, tabeller o.l. – `lov/utenfor-paragrafene.md`

### Forskrifter

- Forskrift om beregning av arbeidsavklaringspenger etter EØS-avtalen (§§ 1 til 6, 6 paragrafer) – `innhold/eos-beregning-arbeidsavklaringspenger.md`
- Forskrift om alderspensjon i folketrygden (§§ 1-1 til 12-1, 82 paragrafer) – `innhold/alderspensjon-i-folketrygden.md`
- Forskrift om dagpenger under arbeidsløshet (§§ 1-1 til 13-4, 59 paragrafer) – `innhold/dagpengeforskriften.md`
- Forskrift om dagpenger for fiskere og fangstfolk under arbeidsløshet (A-trygdforskriften) (§§ 1 til 15, 15 paragrafer) – `innhold/dagpenger-fiskere.md`
- Kunngjøring av virkningstidspunktet for regulering av kravet til minsteinntekt i dagpengeordningen (1 fil) – `innhold/minsteinntekt-virkningstidspunkt.md`
- Forskrift om overgangsregler i forbindelse med ikrafttredelse av endring av folketrygdloven § 4-9 fra 1. januar 2024 (§§ 1 til 2, 2 paragrafer) – `innhold/overgangsregler-2023.md`
- Forskrift om tilskudd til ekspertbistand (§§ 1 til 10, 11 paragrafer) – `innhold/ekspertbistand.md`
- Forskrift om stønad til enslig mor eller far etter folketrygdloven kapittel 15 (§§ 1 til 10, 10 paragrafer) – `innhold/stonad-enslig-mor-far.md`
- Forskrift om overgangsregler i forbindelse med endringer i folketrygdloven § 15-6 og § 15-8 fra 1. februar 2024 (§§ 1 til 3, 3 paragrafer) – `innhold/overgangsregler-par15.md`
- Forskrift om ytelser til gjenlevende ektefelle og tidligere familiepleier etter folketrygdloven kapittel 17 (§§ 1 til 13, 13 paragrafer) – `innhold/ytelser-gjenlevende.md`
- Forskrift om behovsprøvet gravferdsstønad (§§ 1 til 8, 8 paragrafer) – `innhold/behovsprovd-gravferdsstonad.md`
- Forskrift om gravferdsstønad og stønad til båretransport for person som er pliktig medlem etter § 2-5 i lov om folketrygd og som dør utenfor Norge og om stønad til båretransport når et medlem dør i et av de nordiske land (§§ 1 til 4, 4 paragrafer) – `innhold/gravferdsstonad-baretransport.md`
- Forskrift om dekning av utgifter til båretransport i Norge (§§ 1 til 4, 4 paragrafer) – `innhold/baretransport.md`
- Forskrift om grunnbeløp, reguleringsfaktorer, satser for minste pensjonsnivå og satser for garantipensjon i folketrygden fra 1. mai 2026 og virknings-tidspunkt for regulering av kravet til minsteinntekt for rett til ytelser etter folketrygdloven kapitlene 4, 8, 9 og 14 (§§ 1 til 7, 7 paragrafer) – `innhold/grunnbelop-og-satser.md`
- Forskrift om beregning av lønnsveksten som skal benyttes ved regulering av grunnbeløpet og alderspensjon i folketrygden (§§ 1 til 6, 8 paragrafer) – `innhold/regulering-lonnsvekst.md`
- Forskrift om gjennomføring av bilaterale trygdeavtaler (§§ 1 til 2, 2 paragrafer) – `innhold/bilaterale-trygdeavtaler.md`
- Forskrift om unntak fra medlemskap i folketrygden for person som er omfattet av eller mottar ytelser etter utenlandsk trygdelovgivning mv og vedkommendes familiemedlemmer (§§ 1 til 5, 5 paragrafer) – `innhold/unntak-medlemskap.md`
- Forskrift om trygdedekning for asylsøkere og deres familiemedlemmer (§§ 1 til 4, 4 paragrafer) – `innhold/trygdedekning-asylsokere.md`
- Forskrift om medlemskap i trygden under fengselsopphold mv (§§ 1 til 10, 10 paragrafer) – `innhold/medlemskap-fengsel.md`
- Forskrift om fastsetting av pensjonsgivende inntekt for året før det året da et medlem får rett til en trygdeytelse (§§ 1 til 3, 3 paragrafer) – `innhold/pensjonsgivende-inntekt-uforetidspunkt.md`
- Forskrift om godskriving av pensjonspoeng (omsorgspoeng) for personer som har omsorg for små barn (§§ 1 til 4, 4 paragrafer) – `innhold/omsorgspoeng.md`
- Forskrift om godskriving av pensjonspoeng (omsorgspoeng) for omsorgsarbeid for en syk, en funksjonshemmet eller en eldre person (§§ 1 til 9, 9 paragrafer) – `innhold/omsorgspoeng-omsorgsarbeid.md`
- Forskrift om godskriving av pensjonspoeng for mottakere av avtalefestet pensjon som omfattes av AFP-tilskottsloven § 12 eller avtalefestet pensjon fra offentlig pensjonsordning før fylte 65 år (§§ 1 til 3, 3 paragrafer) – `innhold/omsorgspoeng-afp.md`
- Forskrift om nedsettelse av pensjonsgivende inntekt, pensjonsopptjening og avgift når fastsatt skatt og avgift helt eller delvis ikke er betalt (§§ 1 til 8, 8 paragrafer) – `innhold/nedsettelse-pensjonsgivende-inntekt.md`
- Forskrift om gjennomføring av nedsettelse av pensjonsgivende inntekt, pensjonsopptjening og avgift når fastsatt skatt og avgift helt eller delvis ikke er betalt (§§ 1 til 5, 5 paragrafer) – `innhold/gjennomforing-nedsettelse.md`
- Forskrift om endring i forskrift om nedsettelse av pensjonsgivende inntekt, pensjonsopptjening og avgift når fastsatt skatt og avgift helt eller delvis ikke er betalt (1 fil) – `innhold/endring-nedsettelse.md`
- Forskrift om fastsettelse av pensjonsgivende inntekt mv. for medlemmer med inntekt som ikke blir skattlagt av norske myndigheter (§§ 1 til 6, 6 paragrafer) – `innhold/pensjonsgivende-inntekt-utland.md`
- Forskrift om pensjonsberegning, om tilståelse og beregning av barnetillegg og barnepensjon og om gjennomføringa av folketrygdlovens bestemmelser om inntektsprøving i tilfelle som omfattes av EØS-avtalen (§§ 1 til 17, 17 paragrafer) – `innhold/pensjonsberegning-barnetillegg.md`
- Forskrift om behandling av tvister i arbeidsgiverperioden (§§ 1 til 19, 19 paragrafer) – `innhold/tvister-arbeidsgiverperioden.md`
- Forskrift om unntak fra anke til Trygderetten (§§ 1 til 2, 2 paragrafer) – `innhold/unntak-anke-trygderetten.md`
- Forskrift om at visse vedtak kan ankes direkte inn for Trygderetten (§§ 1 til 3, 3 paragrafer) – `innhold/anke-direkte-trygderetten.md`
- Forskrift om utveksling av opplysninger mellom Arbeids- og velferdsetaten og pensjonsinnretninger, forsikringsselskaper og andre finansinstitusjoner (§§ 1 til 8, 8 paragrafer) – `innhold/utveksling-opplysninger.md`
- Forskrift om elektronisk kommunikasjon med Arbeids- og velferdsetaten (§§ 1 til 7, 7 paragrafer) – `innhold/elektronisk-kommunikasjon.md`
- Forskrift om unntak fra pålegg om elektronisk kommunikasjon ved innsending av erklæringer og uttalelser til Arbeids- og velferdsetaten (NAV) (§§ 1 til 5, 5 paragrafer) – `innhold/unntak-elektronisk-innsending.md`
- Forskrift om at saksopplysninger til Arbeids- og velferdsetaten skal gis elektronisk (§§ 1 til 2, 2 paragrafer) – `innhold/saksopplysninger-elektronisk.md`
- Forskrift om økt beregningsgrunnlag for gifte og samboende uføretrygdede som mottar en uføretrygd omregnet fra uførepensjon (§§ 1 til 4, 4 paragrafer) – `innhold/okt-beregningsgrunnlag-gift-samboende.md`
- Forskrift om omregning av uførepensjon til uføretrygd (§§ 1 til 10, 10 paragrafer) – `innhold/omregning-uforepensjon-til-uforetrygd.md`
- Forskrift om uføretrygd fra folketrygden (§§ 1-1 til 9-1, 27 paragrafer) – `innhold/uforetrygdforskriften.md`
- Forskrift om gjennomføringen av folketrygdloven § 22-18 og bidragsinnkrevingsloven § 34 om utbetalingsmåten for ytelser mv (§§ 1 til 6, 6 paragrafer) – `innhold/gjennomforing-par22-18.md`
- Forskrift om rentesats etter folketrygdloven § 22-17 første ledd (§§ 1 til 2, 2 paragrafer) – `innhold/rentesats-par22-17.md`
- Forskrift om disponering av kontantytelser fra folketrygden under opphold i kommunal helse- og omsorgsinstitusjon og i helseinstitusjon i spesialisthelsetjenesten (§§ 1 til 11, 11 paragrafer) – `innhold/disponering-institusjon.md`
- Forskrift om overtredelsesgebyr og tvangsmulkt etter folketrygdloven § 25-3 ved brudd på opplysningsplikten til Arbeidsgiver- og arbeidstakerregisteret mv (§§ 1 til 7, 7 paragrafer) – `innhold/overtredelsesgebyr-tvangsmulkt.md`
- Forskrift til folketrygdloven § 25-10 om arbeidsgivers og oppdragsgivers opplysningsplikt om arbeidsforhold og inntekt (§§ 1 til 4, 4 paragrafer) – `innhold/opplysningsplikt-arbeidsgiver.md`
- Forskrift om føring av statistikk over sykefravær og fravær ved barns sykdom (§§ 1 til 8, 8 paragrafer) – `innhold/statistikk-sykefravaer.md`
- Forskrift om beregning av kapitalverdier av trygdeytelser (§§ 1 til 5, 5 paragrafer) – `innhold/kapitalverdier.md`
- Forskrift om videreføring av to forskrifter gitt med hjemmel i lov om folketrygd (1 fil) – `innhold/viderefoering-forskrifter.md`
- Forskrift om Arbeidsgiver- og arbeidstakerregisteret (§§ 1 til 21, 21 paragrafer) – `innhold/aa-registeret.md`
- Forskrift om menerstatning ved yrkesskade (§§ 1 til 5, 5 paragrafer) – `innhold/menerstatning.md`
- Forskrift om yrkessykdommer, klimasykdommer og epidemiske sykdommer som skal likestilles med yrkesskade (§§ 1 til 3, 3 paragrafer) – `innhold/yrkessykdommer.md`
- Forskrift om sykdommer og forgiftninger m.v. som skal likestilles med yrkesskade (§§ 1 til 3, 3 paragrafer) – `innhold/sykdommer-likestilt-yrkesskade.md`
- Forskrift om et rådgivende yrkessykdomsutvalg for regelmessig revisjon av forskrift over sykdommer som skal likestilles med yrkesskade (§§ 1 til 10, 10 paragrafer) – `innhold/radgivende-yrkessykdomsutvalg.md`
- Forskrift om beregning av uførepensjon og godskriving av pensjonspoeng ved yrkesskade (§§ 1 til 5, 5 paragrafer) – `innhold/beregning-uforepensjon-yrkesskade.md`
- Forskrift om beregning av tilleggspensjon ved yrkesskade (§§ 1 til 5, 5 paragrafer) – `innhold/tilleggspensjon-yrkesskade.md`
- Forskrift om frivillig yrkesskadetrygd for selvstendig næringsdrivende og frilansere (§§ 1 til 6, 6 paragrafer) – `innhold/frivillig-yrkesskadetrygd-selvstendig.md`
- Forskrift om frivillig yrkesskadetrygd for elever som ikke er obligatorisk yrkesskadedekket (§§ 1 til 7, 7 paragrafer) – `innhold/frivillig-yrkesskadetrygd-elever.md`
- Forskrift om arbeidsavklaringspenger (§§ 1 til 16, 16 paragrafer) – `innhold/arbeidsavklaringspenger.md`
- Forskrift om stønad til hjelpemidler mv til bedring av funksjonsevnen i arbeidslivet og i dagliglivet og til ombygging av maskiner på arbeidsplassen (§§ 1 til 10, 10 paragrafer) – `innhold/hjelpemidler.md`
- Forskrift om stønad til lese- og sekretærhjelp for blinde og svaksynte (§§ 1 til 6, 6 paragrafer) – `innhold/lese-sekretarhjelp.md`
- Forskrift om stønad til tolkehjelp for hørselshemmede (§§ 1 til 6, 6 paragrafer) – `innhold/tolkehjelp-horselshemmede.md`
- Forskrift om stønad til tolke- og ledsagerhjelp for døvblinde (§§ 1 til 7, 6 paragrafer) – `innhold/tolke-ledsagerhjelp-dovblinde.md`
- Forskrift om stønad til dekning av utgifter til ortopediske hjelpemidler, brystprotese, ansiktsdefektprotese, øyeprotese og parykk (§§ 1 til 14, 15 paragrafer) – `innhold/ortopediske-hjelpemidler.md`
- Forskrift om stønad til høreapparat og tinnitusmaskerer (§§ 1 til 13, 13 paragrafer) – `innhold/horeapparat.md`
- Forskrift om stønad til motorkjøretøy eller annet transportmiddel (§§ 1 til 20, 20 paragrafer) – `innhold/motorkjoretoy.md`
- Forskrift om stønad til briller til barn (§§ 1 til 11, 11 paragrafer) – `innhold/briller-barn.md`
- Forskrift om adgang til å utbetale uredusert ytelse for visse persongrupper i institusjon (§§ 1 til 4, 4 paragrafer) – `innhold/uredusert-ytelse-institusjon.md`
- Forskrift om beregning av uføretrygd og pensjon mv. under opphold i institusjon (§§ 1 til 4, 4 paragrafer) – `innhold/uforetrygd-institusjon.md`
- Forskrift om overgangsregler for beregning av redusert ytelse under opphold i institusjon og under straffegjennomføring (§§ 1 til 5, 5 paragrafer) – `innhold/overgangsregler-institusjon.md`
- Forskrift om gradering av pleiepenger (§§ 1 til 6, 6 paragrafer) – `innhold/gradering-pleiepenger.md`
- Forskrift om beregning av uføretrygd etter EØS-avtalen (§§ 1 til 6, 6 paragrafer) – `innhold/eos-beregning-uforetrygd.md`
- Forskrift om unntak fra vilkåret om legeerklæring når kiropraktorer og manuellterapeuter dokumenterer arbeidsuførheten med erklæring (§§ 1 til 4, 4 paragrafer) – `innhold/legeerklaering-kiropraktor-manuellterapeut.md`
- Forskrift om obligatorisk opplæring i sykmeldingsarbeid for leger (§§ 1 til 5, 5 paragrafer) – `innhold/opplaering-sykmeldingsarbeid.md`
- Forskrift om forsikring mot ansvar for sykepenger i arbeidsgiverperioden for små bedrifter (§§ 1 til 4, 4 paragrafer) – `innhold/forsikring-arbeidsgiverperioden.md`
- Forskrift om forsikring for tillegg til sykepenger for selvstendig næringsdrivende (§§ 1 til 5, 5 paragrafer) – `innhold/forsikring-sykepenger-selvstendige.md`
- Forskrift om forsikring for tillegg til sykepenger for frilansere (§§ 1 til 5, 5 paragrafer) – `innhold/forsikring-sykepenger-frilansere.md`
- Forskrift om stønad til dekning av utgifter til helsetjenester i utlandet (§§ 1 til 5, 5 paragrafer) – `innhold/helsetjenester-utlandet.md`
- Forskrift om utvidet stønad til helsetjenester under opphold i utlandet (§§ 1 til 7, 7 paragrafer) – `innhold/utvidet-helsetjenester-utlandet.md`
- Forskrift om overgangsregler i forbindelse med endringer i folketrygdloven kapittel 15, 16 og 17 fra 1. januar 2016 (§§ 1 til 10, 10 paragrafer) – `innhold/overgangsregler-kap15-17-2016.md`

## EU-rettsakter som teksten viser til

Funnet automatisk ved søk etter rettsaktnummer. Stier til `regelverk/eu/` er fra roten av basen.

- **Forordning nr. 883/2004** (Trygdeforordningen) – i basen: `regelverk/eu/forordning-883-2004/VEIVISER.md`. Nevnt i `forskrifter/dagpengeforskriften/par-1-7.md`, `forskrifter/dagpengeforskriften/par-1-8.md`, `forskrifter/dagpengeforskriften/par-1-9.md`, `forskrifter/dagpengeforskriften/utenfor-paragrafene.md`, `forskrifter/eos-beregning-arbeidsavklaringspenger/par-1.md`, `forskrifter/eos-beregning-uforetrygd/par-1.md`, `forskrifter/omregning-uforepensjon-til-uforetrygd/par-4.md`, `lov/par-1-3a.md`
- **Forordning nr. 987/2009** (Gjennomføringsforordningen til trygdeforordningen) – i basen: `regelverk/eu/forordning-987-2009/VEIVISER.md`. Nevnt i `forskrifter/eos-beregning-arbeidsavklaringspenger/par-1.md`, `forskrifter/eos-beregning-uforetrygd/par-1.md`, `lov/par-1-3a.md`
- Forordning nr. 1408/71 – ikke i basen. Nevnt i `forskrifter/bilaterale-trygdeavtaler/par-1.md`, `forskrifter/omregning-uforepensjon-til-uforetrygd/par-4.md`
- Forordning nr. 988/2009 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 1244/2010 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 1224/2012 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 465/2012 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 1372/2013 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 517/2013 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning nr. 1368/2014 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning 2017/492 – ikke i basen. Nevnt i `lov/par-1-3a.md`
- Forordning 2019/1149 – ikke i basen. Nevnt i `lov/par-1-3a.md`

## Andre kilder

Dette er ikke lov- eller forskriftstekst.

### Merknader

- Arbeidsavklaringspenger og tilleggsstønader (kap. 11 og 11 A) – `merknader/aap.md`
- Dagpenger (kap. 4) – `merknader/dagpenger.md`
- Etterlatte og gravferd (kap. 7, 16, 17, 17 A og 18) – `merknader/etterlatte-gravferd.md`
- Folketrygdloven – sykepenger og pleiepenger (kap. 8 og 9) – `merknader/sykepenger.md`
- Folketrygdloven – uføretrygd (kap. 12) – `merknader/uforetrygd.md`

### Rundskriv

- `rundskriv/forskrifter/aa-registeret/` – 23 filer, start med `rundskriv/forskrifter/aa-registeret/oversikt.md`
- `rundskriv/forskrifter/ekspertbistand/` – 12 filer, start med `rundskriv/forskrifter/ekspertbistand/oversikt.md`
- `rundskriv/forskrifter/okt-beregningsgrunnlag-gift-samboende/` – 6 filer, start med `rundskriv/forskrifter/okt-beregningsgrunnlag-gift-samboende/oversikt.md`
- `rundskriv/forskrifter/omregning-uforepensjon-til-uforetrygd/` – 9 filer, start med `rundskriv/forskrifter/omregning-uforepensjon-til-uforetrygd/oversikt.md`
- `rundskriv/forskrifter/omsorgspoeng/` – 5 filer, start med `rundskriv/forskrifter/omsorgspoeng/oversikt.md`
- `rundskriv/forskrifter/omsorgspoeng-omsorgsarbeid/` – 10 filer, start med `rundskriv/forskrifter/omsorgspoeng-omsorgsarbeid/oversikt.md`
- `rundskriv/forskrifter/opplysningsplikt-arbeidsgiver/` – 6 filer, start med `rundskriv/forskrifter/opplysningsplikt-arbeidsgiver/oversikt.md`
- `rundskriv/forskrifter/overgangsregler-institusjon/` – 7 filer, start med `rundskriv/forskrifter/overgangsregler-institusjon/oversikt.md`
- `rundskriv/forskrifter/overgangsregler-kap15-17-2016/` – 12 filer, start med `rundskriv/forskrifter/overgangsregler-kap15-17-2016/oversikt.md`
- `rundskriv/forskrifter/uforetrygdforskriften/` – 6 filer, start med `rundskriv/forskrifter/uforetrygdforskriften/oversikt.md`
- `rundskriv/forskrifter/uredusert-ytelse-institusjon/` – 6 filer, start med `rundskriv/forskrifter/uredusert-ytelse-institusjon/oversikt.md`
- `rundskriv/forskrifter/yrkessykdommer/` – 2 filer, start med `rundskriv/forskrifter/yrkessykdommer/oversikt.md`
- `rundskriv/rundskriv-r01-00/` – 14 filer, start med `rundskriv/rundskriv-r01-00/oversikt.md`
- `rundskriv/rundskriv-r02-00/` – 20 filer, start med `rundskriv/rundskriv-r02-00/oversikt.md`
- `rundskriv/rundskriv-r03-00/` – 2 filer, start med `rundskriv/rundskriv-r03-00/oversikt.md`
- `rundskriv/rundskriv-r03-01/` – 9 filer, start med `rundskriv/rundskriv-r03-01/oversikt.md`
- `rundskriv/rundskriv-r03-02/` – 11 filer, start med `rundskriv/rundskriv-r03-02/oversikt.md`
- `rundskriv/rundskriv-r03-03/` – 8 filer, start med `rundskriv/rundskriv-r03-03/oversikt.md`
- `rundskriv/rundskriv-r03-04/` – 3 filer, start med `rundskriv/rundskriv-r03-04/oversikt.md`
- `rundskriv/rundskriv-r04-00/` – 29 filer, start med `rundskriv/rundskriv-r04-00/oversikt.md`
- `rundskriv/rundskriv-r05-00/` – 3 filer, start med `rundskriv/rundskriv-r05-00/oversikt.md`
- `rundskriv/rundskriv-r05-01a/` – 2 filer, start med `rundskriv/rundskriv-r05-01a/oversikt.md`
- `rundskriv/rundskriv-r05-02/` – 2 filer, start med `rundskriv/rundskriv-r05-02/oversikt.md`
- `rundskriv/rundskriv-r05-03/` – 8 filer, start med `rundskriv/rundskriv-r05-03/oversikt.md`
- `rundskriv/rundskriv-r05-03d1/` – 9 filer, start med `rundskriv/rundskriv-r05-03d1/oversikt.md`
- `rundskriv/rundskriv-r05-03d2/` – 8 filer, start med `rundskriv/rundskriv-r05-03d2/oversikt.md`
- `rundskriv/rundskriv-r05-05-for-1702/` – 2 filer, start med `rundskriv/rundskriv-r05-05-for-1702/oversikt.md`
- `rundskriv/rundskriv-r05-07/` – 5 filer, start med `rundskriv/rundskriv-r05-07/oversikt.md`
- `rundskriv/rundskriv-r05-08/` – 6 filer, start med `rundskriv/rundskriv-r05-08/oversikt.md`
- `rundskriv/rundskriv-r05-09/` – 8 filer, start med `rundskriv/rundskriv-r05-09/oversikt.md`
- `rundskriv/rundskriv-r05-10/` – 6 filer, start med `rundskriv/rundskriv-r05-10/oversikt.md`
- `rundskriv/rundskriv-r05-10a/` – 7 filer, start med `rundskriv/rundskriv-r05-10a/oversikt.md`
- `rundskriv/rundskriv-r05-12/` – 7 filer, start med `rundskriv/rundskriv-r05-12/oversikt.md`
- `rundskriv/rundskriv-r05-13/` – 3 filer, start med `rundskriv/rundskriv-r05-13/oversikt.md`
- `rundskriv/rundskriv-r05-14-01/` – 12 filer, start med `rundskriv/rundskriv-r05-14-01/oversikt.md`
- `rundskriv/rundskriv-r05-14-02/` – 12 filer, start med `rundskriv/rundskriv-r05-14-02/oversikt.md`
- `rundskriv/rundskriv-r05-14-03/` – 11 filer, start med `rundskriv/rundskriv-r05-14-03/oversikt.md`
- `rundskriv/rundskriv-r05-21/` – 5 filer, start med `rundskriv/rundskriv-r05-21/oversikt.md`
- `rundskriv/rundskriv-r05-22/` – 2 filer, start med `rundskriv/rundskriv-r05-22/oversikt.md`
- `rundskriv/rundskriv-r05-24/` – 2 filer, start med `rundskriv/rundskriv-r05-24/oversikt.md`
- `rundskriv/rundskriv-r05-24a-for/` – 15 filer, start med `rundskriv/rundskriv-r05-24a-for/oversikt.md`
- `rundskriv/rundskriv-r05-25/` – 12 filer, start med `rundskriv/rundskriv-r05-25/oversikt.md`
- `rundskriv/rundskriv-r05-26/` – 2 filer, start med `rundskriv/rundskriv-r05-26/oversikt.md`
- `rundskriv/rundskriv-r06-00/` – 14 filer, start med `rundskriv/rundskriv-r06-00/oversikt.md`
- `rundskriv/rundskriv-r06-04-for/` – 2 filer, start med `rundskriv/rundskriv-r06-04-for/oversikt.md`
- `rundskriv/rundskriv-r07-00/` – 8 filer, start med `rundskriv/rundskriv-r07-00/oversikt.md`
- `rundskriv/rundskriv-r08-00/` – 93 filer, start med `rundskriv/rundskriv-r08-00/oversikt.md`
- `rundskriv/rundskriv-r09-00/` – 25 filer, start med `rundskriv/rundskriv-r09-00/oversikt.md`
- `rundskriv/rundskriv-r10-00/` – 8 filer, start med `rundskriv/rundskriv-r10-00/oversikt.md`
- `rundskriv/rundskriv-r10-07/` – 2 filer, start med `rundskriv/rundskriv-r10-07/oversikt.md`
- `rundskriv/rundskriv-r10-07-4-5-ledd/` – 3 filer, start med `rundskriv/rundskriv-r10-07-4-5-ledd/oversikt.md`
- `rundskriv/rundskriv-r10-07-for/` – 12 filer, start med `rundskriv/rundskriv-r10-07-for/oversikt.md`
- `rundskriv/rundskriv-r10-07a/` – 9 filer, start med `rundskriv/rundskriv-r10-07a/oversikt.md`
- `rundskriv/rundskriv-r10-07acd/` – 4 filer, start med `rundskriv/rundskriv-r10-07acd/oversikt.md`
- `rundskriv/rundskriv-r10-07b/` – 12 filer, start med `rundskriv/rundskriv-r10-07b/oversikt.md`
- `rundskriv/rundskriv-r10-07e/` – 6 filer, start med `rundskriv/rundskriv-r10-07e/oversikt.md`
- `rundskriv/rundskriv-r10-07f/` – 7 filer, start med `rundskriv/rundskriv-r10-07f/oversikt.md`
- `rundskriv/rundskriv-r10-07g/` – 7 filer, start med `rundskriv/rundskriv-r10-07g/oversikt.md`
- `rundskriv/rundskriv-r10-07h/` – 18 filer, start med `rundskriv/rundskriv-r10-07h/oversikt.md`
- `rundskriv/rundskriv-r10-07i/` – 2 filer, start med `rundskriv/rundskriv-r10-07i/oversikt.md`
- `rundskriv/rundskriv-r11-00/` – 36 filer, start med `rundskriv/rundskriv-r11-00/oversikt.md`
- `rundskriv/rundskriv-r11a-00/` – 7 filer, start med `rundskriv/rundskriv-r11a-00/oversikt.md`
- `rundskriv/rundskriv-r11a-00-for/` – 18 filer, start med `rundskriv/rundskriv-r11a-00-for/oversikt.md`
- `rundskriv/rundskriv-r12-00/` – 45 filer, start med `rundskriv/rundskriv-r12-00/oversikt.md`
- `rundskriv/rundskriv-r12-15-for/` – 5 filer, start med `rundskriv/rundskriv-r12-15-for/oversikt.md`
- `rundskriv/rundskriv-r12-19-for-1376/` – 6 filer, start med `rundskriv/rundskriv-r12-19-for-1376/oversikt.md`
- `rundskriv/rundskriv-r13-00/` – 24 filer, start med `rundskriv/rundskriv-r13-00/oversikt.md`
- `rundskriv/rundskriv-r14-00/` – 41 filer, start med `rundskriv/rundskriv-r14-00/oversikt.md`
- `rundskriv/rundskriv-r15-00/` – 15 filer, start med `rundskriv/rundskriv-r15-00/oversikt.md`
- `rundskriv/rundskriv-r15-00-for-1361/` – 16 filer, start med `rundskriv/rundskriv-r15-00-for-1361/oversikt.md`
- `rundskriv/rundskriv-r15-08/` – 2 filer, start med `rundskriv/rundskriv-r15-08/oversikt.md`
- `rundskriv/rundskriv-r16-00/` – 15 filer, start med `rundskriv/rundskriv-r16-00/oversikt.md`
- `rundskriv/rundskriv-r17-00/` – 19 filer, start med `rundskriv/rundskriv-r17-00/oversikt.md`
- `rundskriv/rundskriv-r18-00/` – 13 filer, start med `rundskriv/rundskriv-r18-00/oversikt.md`
- `rundskriv/rundskriv-r19-00/` – 77 filer, start med `rundskriv/rundskriv-r19-00/oversikt.md`
- `rundskriv/rundskriv-r20-00/` – 81 filer, start med `rundskriv/rundskriv-r20-00/oversikt.md`
- `rundskriv/rundskriv-r21-00/` – 33 filer, start med `rundskriv/rundskriv-r21-00/oversikt.md`
- `rundskriv/rundskriv-r21-00b/` – 13 filer, start med `rundskriv/rundskriv-r21-00b/oversikt.md`
- `rundskriv/rundskriv-r22-00/` – 25 filer, start med `rundskriv/rundskriv-r22-00/oversikt.md`
- `rundskriv/rundskriv-r23-00/` – 18 filer, start med `rundskriv/rundskriv-r23-00/oversikt.md`
- `rundskriv/rundskriv-r24-00/` – 4 filer, start med `rundskriv/rundskriv-r24-00/oversikt.md`
- `rundskriv/rundskriv-r25-00/` – 19 filer, start med `rundskriv/rundskriv-r25-00/oversikt.md`
- `rundskriv/rundskriv-r25-03-for/` – 8 filer, start med `rundskriv/rundskriv-r25-03-for/oversikt.md`
- `rundskriv/rundskriv-r25-16-for-368/` – 39 filer, start med `rundskriv/rundskriv-r25-16-for-368/oversikt.md`
- `rundskriv/rundskriv-r26-00/` – 117 filer, start med `rundskriv/rundskriv-r26-00/oversikt.md`
- `rundskriv/sivilombudet/` – 74 filer, start med `rundskriv/sivilombudet/oversikt.md`

### Rettspraksis

- `rettspraksis/hoyesterett/` – 18 filer, start med `rettspraksis/hoyesterett/oversikt.md`
<!-- AUTO-SLUTT -->
