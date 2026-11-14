---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/analysere-skjevhet-i-data/skjevhet-i-data"
hentet: "2026-11-14"
---

# Skjevhet i data

Et sentralt spørsmål er om dataene KI-systemet bruker er representative for formålet. Selv datasett med høy datakvalitet kan gi skjeve resultater dersom viktige grupper, situasjoner eller variasjoner er underrepresentert. For å unngå det kan du analysere skjevhet i fire trinn.

Skjevhet, eller bias, er en systematisk feil som kan oppstå når dataene ikke er balanserte. Det skjer når enkelte grupper eller typer informasjon er overrepresentert, mens andre er underrepresentert. Dette kan føre til at systemet gir dårligere eller mindre presise resultater for enkelte grupper.

Skjevhet i data kan føre til diskriminering. Dette reguleres av likestillings- og diskriminiseringsloven som forbyr usaklig forskjellsbehandling. Forbudet gjelder uavhengig av om beslutningen tas av mennesker eller KI-systemer.

## Slik kan du analysere skjevhet

Målet med å analysere skjevhet i data er å identifisere og forstå om dataene er ubalanserte og vurdere hvordan dette kan påvirke KI-systemet. Analysen skal også gi grunnlag for å avgjøre om det er behov for tiltak.

I tråd med anerkjente rammeverk for datastyring, slik som DAMA rammeverket, bør dette arbeidet være en del av organisasjonens prosesser med tydelig ansvar, dokumentasjon og oppfølging over tid. Du bør derfor jobbe systematisk med analyse av skjevhet.

Følg disse fire trinnene når du analyserer skjevhet. Underveis bør du dokumentere beslutninger og vurderinger for sporbarhet og etterprøvbarhet. Det viktigste er at vurderingene dine er bevisste, godt dokumentert og tilpasset formålet med KI-systemet.

### 1. Identifiser kilder til skjevhet

Start med å kartlegge hva som kan skape skjevhet i dataene. Dette kan for eksempel være hvordan dataene er samlet inn, hvilke grupper som er representert, eller hvordan dataene er merket. Skjevhet kan også oppstå dersom datasettet ikke er representativt for populasjonen eller situasjonene KI-systemet skal brukes på.

### 2. Vurder skjevhet i dataene

Undersøk om det faktisk finnes skjevhet i datasettet. Bruk relevante metoder for å avdekke ubalanser og vurdere hvor stor påvirkning disse har på resultatene.

Vurder også datakvalitet og om dataene er representative for formålet. I tråd med prinsippene i ISO/IEC 5259-serien for datakvalitet i analyse og maskinlæring bør du vurdere om datasettet er tilstrekkelig dekkende, representativt og egnet for den tiltenkte bruken av KI-systemet.

### 3. Vurder behov for tiltak

Basert på analysen må du vurdere om skjevheten bør håndteres. Dette vil avhenge av kontekst, formål og konsekvenser. I noen tilfeller kan det være riktig å dokumentere og akseptere skjevheten dersom den gjenspeiler reelle forhold. Om du må gjøre tiltak kan du for eksempel

- justere datasettet
- hente inn mer data
- tilpasse modellen
- eller dokumentere og akseptere skjevheten

### 4. Følge opp over tid

I motsetning til mange andre aktiviteter i en KI-prosess er dette ikke noe du gjør bare ved behov. Skjevhet i data kan endre seg. Du bør derfor overvåke dataene og modellens resultater jevnlig. Dette er en del av kontinuerlig datakvalitetsarbeid og god datastyring.

For å følge opp dette bør du

- ha tydelige roller og ansvar for å følge opp datakvalitet og skjevhet
- dokumentere vurderinger og tiltak
- overvåke dataene over tid, siden skjevhet kan endre seg

Det er viktig å være klar over at skjevhet ikke alltid er feil som må fjernes. Ofte gjenspeiler dataene virkelige forhold. Det viktigste er at du forstår skjevheten og hvilken betydning den har for bruken av KI-systemet. Selv om dataene kan være “korrekte” kan de inneholde skjevheter fordi de gjenspeiler historiske eller samfunnsmessige forhold. Derfor er det avgjørende å forstå konteksten dataene er hentet fra.

Dette er i tråd med anbefalinger i ISO/IEC 5259-serien som understreker at datakvalitet, representativitet og skjevhet må vurderes gjennom hele livssyklusen til KI-systemet, ikke bare ved utvikling.

## To typer skjevhet

Iboende skjevhet i data er skjevheter som finnes i dataene fordi de gjenspeiler virkeligheten slik den er registrert.

Eksempel: Et datasett for et smart vanningssystem inneholder mest data fra solrike områder og lite fra skyggefulle områder. Systemet kan da lære at planter generelt trenger mer vann enn de faktisk gjør i skygge.

Kognitive skjevheter er skjevheter som oppstår gjennom menneskelige valg og vurderinger for eksempel i hvordan data samles inn, merkes eller tolkes.

Eksempel: En fagperson antar at én type plante alltid trenger mer vann og legger inn dette som en regel selv om dataene ikke støtter det fullt ut.

Likestillings- og diskrimineringsombudet har laget en veileder om innebygd diskriminseringsvern. Den viser hvordan virksomheter kan avdekke og forebygge diskriminering i utvikling og bruk av kunstig intelligens. Gå til veileder fra Likestillings- og diskrimineringsombudet.
