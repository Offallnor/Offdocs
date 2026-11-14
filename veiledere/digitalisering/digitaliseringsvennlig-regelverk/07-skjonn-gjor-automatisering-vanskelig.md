---
veileder: "Veileder for digitaliseringsvennlig regelverk"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/datadeling/skjonn-gjor-automatisering-vanskelig/2902"
hentet: "2026-11-14"
---

# Skjønn gjør automatisering vanskelig

Datamaskinen er avhengig av instruksjoner av logisk eller aritmetisk karakter. Alle relevante tolkningsspørsmål må være tatt stilling til før regelverket gjøres til programkode. Dette er særlig krevende ved skjønnsmessig regelverk og er i noen tilfeller ikke mulig.

Opprettet: 17. september 2021

Sist endret: 29. oktober 2021

## Hva mener vi med skjønn?

Å utøve skjønn handler om å gjøre en konkret vurdering som ikke er bestemt på forhånd.

Det skilles ofte mellom to typer skjønn. Sentralt for dette skillet er hvordan og i hvilken grad domstolene prøver forvaltningens rettsanvendelse.

## Rettsanvendelsesskjønn

Den første typen er det «skjønnet» som ligger i at deler av språket vårt ikke entydig gir uttrykk for fenomener i verden. Det vil alltid være et behov for å tolke ord, uttrykk, setninger, avsnitt og tekster for å forstå hva som er den underliggende meningen. Noen ord og uttrykk er det særlig nødvendig å tolke. Ord som «rimelig», «hensiktsmessig» eller «forsvarlig» er det vanskelig å forstå uten en nærmere vurdering. Når det er brukt slike uttrykk i regelverket ser vi ofte på det som skjønnsmessige ord og uttrykk.

Denne formen for «skjønn» kalles ofte for «rettsanvendelsesskjønn» eller «rettslige standarder». Den som skal tolke ord og uttrykk i regelverket må gjøre dette i tråd med den juridiske metoden.

Slike skjønnsmessige uttrykk gjør det mulig for den som tolker uttrykket å ta mange forhold med i betraktningen. Den som har laget regelverket har ofte ønsket nettopp dette. For lovgiver kan det være vanskelig å vurdere alle detaljene som har betydning på et konkret rettsområde. Da kan det være bedre å overlate dette ansvaret til den som skal tolke regelverket fordi denne personen kanskje har bedre kunnskap om de konkrete forholdene. Dette gjelder særlig på områder som krever spisset kompetanse.

Det kan også være en fordel med slike skjønnsmessige uttrykk dersom det er et område hvor ting endrer seg. Det som var «rimelig» i 1995 er ikke nødvendigvis det samme som det som er rimelig i 2021.

## Kan-skjønn

Den andre typen «skjønn» er det som ofte omtales som forvaltningens frie skjønn og «kan-skjønnet». Denne typen skjønn skyldes ikke at språket vårt må tolkes, men at lovgiver aktivt har bestemt at forvaltningen skal ha muligenheten til å velge.

Lovgiver har altså gitt fra seg litt av sin myndighet, for lovgiver kunne jo detaljbestemt hvordan dette valget skulle foretas. Når lovgiver likevel ikke har gjort det skyldes det ofte gode grunner. Forvaltningen har kanskje bedre grunnlag for å vurdere i hvilke situasjoner et vedtak bør treffes, eller det kan foreligge særskilte forhold som det bør tas hensyn til ved behandlingen av en sak.

På samme måte som for rettsanvendelsesskjønn kan det også være detaljkunnskaper på dette område som lovgiver ikke har, eller det kan være et område hvor det skjer raske endringer. Det er svært viktig å huske på at forvaltningen ikke kan velge fritt. Rettskildene setter rammene for hvor fritt valget egentlig er. Kan-skjønnet gjør det likevel mulig for forvaltningen å vurdere «kan» på bakgrunn av egendefinerte kriterier, så lenge disse er innenfor rammene av de øvrige rettskildene.

## Eksempel på utfordringene ved automatisering av skjønn

Hvorfor det er vanskelig å automatisere skjønn kan illustreres med straffegjennomføringslovens § 32 første ledd om permisjon. Dette er en bestemmelse med mye skjønn som tydelig viser hvorfor dette er utfordrende å gjøre til programkode.

**Straffegjennomføringslovens § 32 første ledd**

«Dersom **sikkerhetmessige grunner** ikke taler mot det, **kan** kriminalomsorgen gi innsatte permisjon av kortere tids varighet dersom **særlige og vektige grunner** taler for det, eller når permisjon anses **formålstjenlig** **for den videre gjennomføring av straffen**» [våre uthevinger].

### Fra en saksbehandlers perspektiv

Den som skal anvende regelverket, rettsanvenderen, vil måtte tolke alle vilkårene for å se hvordan bestemmelsen gjelder i den konkrete saken. Denne prosessen må gjøres med utgangspunkt i juridisk metode, hvor også andre rettskilder kan være relevante for fastsettelsen av rettsregelen. Normalt vil de fleste ordene og uttrykkene være lette å tolke. For en rettsanvender i kriminalomsorgen vil det normalt være uproblematisk å vurdere om en person er «innsatt». Derimot vil vilkårene «sikkerhetsmessige grunner», «særlig og vektige grunner» og «formålstjenlig for den videre gjennomføring av straffen» måtte tolkes grundigere for at det skal være mulig for kriminalomsorgen å vurdere om en innsatt oppfyller disse vilkårene.

Etter at rettsanvenderen har tolket og klarlagt innholdet i de ulike vilkårene, gjenstår «kan-skjønnet» i bestemmelsen. Kriminalomsorgen kan velge dette. Rettsanvenderen må se på rettskildematerialet for å se hvilke føringer som ligger på kriminalomsorgens valg. Det kan for eksempel foreligge noen menneskerettslige forpliktelser og føringer på når kriminalomsorgen skal gi permisjon. Hvis ikke det finnes noen føringer, blir det opp til kriminalomsorgen selv å vurdere om permisjon skal gis. Dette må naturligvis baseres på forsvarlige kriterier, og ofte vil disse være fastsatt i instrukser og rundskriv.

### Fra en datamaskins perspektiv

For at en datamaskin skal kunne gjennomføre rettsanvendelsen, må regelverket ha blitt transformert til et datamaskinprogram. Med i utgangspunkt i juridisk metode finner man innholdet i rettsregelen. Deretter brytes rettsregelen ned i logiske eller aritmetiske operasjoner som bearbeider informasjon som er tilgjengelig for en datamaskin. Som et eksempel kan vilkåret «ikke sikkerhetsmessige grunner som taler mot» blitt transformert til:

*Den innsatte skal ha færre en 3 anmerkinger i fengselet, og i tillegg ingen anmerkninger som har høy alvorlighetsgrad.*

Datamaskiners muligheter og begrensninger ved automatisert rettsanvendelse

Forutsatt at denne typen informasjon eksisterer i et maskinlesbart format kan datamaskinen hente opplysningene, behandle dem og avgjøre om vilkåret er oppfylt.

Utfordringen er imidlertid at datamaskinprogrammet er bestemt på forhånd. Dersom det kommer en sak hvor det åpenbart ikke er «sikkerhetsmessige grunner som taler mot», men dette ikke er implementert i datamaskinprogrammet i transformasjonen, vil ikke datamaskinen kunne avgjøre dette.

## En situasjon datamaskinen ikke ville tatt høyde for

En innsatt soner en dom på 20 år og det bare er en uke igjen til prøveløslatelsen. Den innsatte skal på visning i leiligheten han skal flytte inn i og trenger permisjon til dette. Den innsatte er gammel, dårlig til beins og avhengig av hjelp for å forflytte seg. Den innsatte er rolig og har ikke vist noe farlig atferd. Samtidig har den innsatte fått fire anmerkinger i løpet av fengselsoppholdet, men dette var på et tidspunkt hvor den innsatte hadde mistet et familiemedlem og var i dyp sorg.

Det kan være gode grunner til at dette skal tilsi at sikkerhetsmessige grunner ikke taler mot, selv om vedkommende har fire anmerkninger. En datamaskin som ikke er programmert til å ta høyde for dette vil da uansett avslå søknaden.

Den automatiserte bestemmelsen i eksempelet er altså snevrere og mindre fleksibel enn den opprinnelige regelen. Dette vil gi en uriktig rettsanvendelse. Når slike skjønnsmessigvilkår gjøres til programkode vil det derfor ofte være behov for et omfattende arbeid. Alle relevante tolkningsspørsmål må vurderes og må bli en del av den rettsregelen som gjøres til programkode. Den automatiserte rettsanvendelsen skal ikke gi en dårligere rettssituasjon enn manuell rettsanvendelse.

Skjønnsmessige regelverk er altså vanskelig å transformere til programkode. Det kan være så tid- og ressurskrevende at det ikke er hensiktsmessig. Videre kan det være slik at det konkrete regelverket forutsetter en skjønnsmessig vurdering av en slik art at det ikke på en forsvarlig måte kan gjøres til programkode.

[Delvis automatisering](https://www.digdir.no/datadeling/hel-eller-delvis-automatisering/2901) kan være et godt alternativ dersom regelverk inneholder skjønnsmessige bestemmelser som ikke kan eller bør automatiseres.

**Regulering av automatiserte avgjørelser**

Nav-lovens § 4a annet ledd regulerer automatiserte avgjørelser i arbeids- og velferdsetaten og gir et rettslig grunnlag i nasjonal rett i henhold til personvernforordningen artikkel 22. Bestemmelsen viser at avgjørelser som bygger på skjønnsmessig rettsanvendelse som utgangspunkt ikke kan automatiseres i Arbeids- og velferdsetaten. Det er likevel tillatt såfremt det ivaretar forsvarlighetskravet og avgjørelsen er utvilsom.

*"Arbeids- og velferdsetaten kan treffe avgjørelser som utelukkende er basert på automatisert behandling av personopplysninger, herunder personopplysninger som nevnt i personvernforordningen artikkel 9 og 10. Behandlingen **må sikre** partens krav til **forsvarlig saksbehandling**og være forenlig med retten til vern av personopplysninger. Avgjørelsen kan ikke bygge på skjønnsmessige vilkår i lov eller forskrift, **med mindre avgjørelsen er utvilsom**. Den registrerte har rett til manuell overprøving av avgjørelsen." [vår utheving og kursivering]*

En liknende bestemmelse finnes i utlendingsforskriften § 17-7c.

Til spesifikke anbefalinger for å lage automatiseringsvennlig regelverk
