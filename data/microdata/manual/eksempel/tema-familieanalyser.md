<!-- kilde: https://microdata.no/manual/eksempel/Tema%20-%20Familieanalyser/ -->
<!-- Brukerveiledningen for microdata.no (SSB og Sikt), hentet automatisk. -->

# Tema - Familieanalyser

Den enkleste måten å finne familietyper på er å bruke eksisterende variabler som f.eks. BEFOLKNING_REGSTAT_FAMTYP eller  BEFOLKNING_REGSTAT_HUSHTYP. Dette lar deg klassifisere personer etter hvilken type familie eller husholdning man tilhører. Også sivilstatus kan man finne via variabelen  SIVSTANDFDT_SIVSTAND.

Familie-/husholdningsmedlemmer finner man via variablene BEFOLKNING_REGSTAT_FAMNR, BEFOLKNING_HUSHNR og INNTEKT_HUSHNR. Alle medlemmer av en familie eller husholdning vil ha et felles id-nummer som lar deg lage aggregert statistikk på familie-/husholdningsnivå som igjen kan kobles på et persondatasett. På denne måten vil man ikke bare ha personlige opplysninger i et datasett, men også familieopplysninger som f.eks. samlet familieinntekt.

Det er også mulig å koble på opplysninger om enkeltindivider i familien:

-

Foreldre: BEFOLKNING_FAR_FNR og BEFOLKNING_MOR_FNR
-

Besteforeldre: BEFOLKNING_FARFAR_FNR, BEFOLKNING_FARMOR_FNR, BEFOLKNING_MORFAR_FNR og BEFOLKNING_MORMOR_FNR
-

Ektefeller/partnere og samboere: BEFOLKNING_EKT_FNR og BEFOLKNING_SAMB_FNR
-

Enslige: Kan finnes gjennom variabelen BEFOLKNING_PARSTATUS
-

Søsken: BEFOLKNING_SOESKEN_FNR. Variabelen fungerer på samme måte som familienummer-variabelen, ved at alle søsken i en søskenflokk får et felles identitetsnummer som peker til eldste person i søskenflokken.

Alle typer familiekonstellasjoner er ikke like enkle å finne direkte, f.eks. familier med barn som ikke bor hjemme.

I denne eksempelsamlingen vises metoder for å finne ulike typer familiekonstellasjoner, både de enkle variantene og de man ikke nødvendigvis klarer å finne direkte via eksisterende variabler.
