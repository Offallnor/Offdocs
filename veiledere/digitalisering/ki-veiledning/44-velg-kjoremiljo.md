---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-kjoremiljo"
hentet: "2026-11-14"
---

# 2. Anskaffe, utvikle eller videreutvikle

1. [Undersøk markedet](https://ki.norge.no/veiledning/kom-i-gang-med-ki/undersok-markedet)
2. [Forstå prismodeller](https://ki.norge.no/veiledning/kom-i-gang-med-ki/forsta-prismodeller)
3. [Velg modelltype](https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-modelltype)
4. [Velg kjøremiljø](https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-kjoremiljo)
5. [Utarbeid kravspesifikasjon](https://ki.norge.no/veiledning/kom-i-gang-med-ki/utarbeid-kravspesifikasjon)

## Velg kjøremiljø

Valget av modell er tett knyttet til spørsmålet om hvor den skal kjøres. Med «kjøres» mener vi prosessen fra du stiller et spørsmål til modellen svarer.

Kjøremiljøet påvirker sikkerheten, hastigheten, kostnaden og i hvilken grad du beholder kontrollen over dataene. Før du velger kjøremiljø, bør du derfor stille noen sentrale spørsmål for å ivareta disse aspektene.

- Hvor ligger dataene fysisk?
- Hvor lagres data og hvem har tilgang til dem? Hva skjer med data hvis du avslutter avtalen?
- Hvem har teknisk tilgang til serverne?
- Er det avtale om at data ikke brukes til trening?
- Hvordan er krypteringen av data i transit og ved lagring?
- Har vi evne til å drifte og sikre løsningen selv?
- Hva skjer med dataene hvis samarbeidet med leverandøren avsluttes?

### Velg blant fire kjøremiljøer

Det finnes fire hovedmåter å kjøre KI-modeller på: Privat sky, allmenne skytjenester, på egen infrastruktur og hybrid sky.

- Allmenne skytjenester egner seg best for ikke-sensitiv data og rask prototyping.
- Privat sky egner seg best for virksomheter med moderate sikkerhetskrav som ikke ønsker egen infrastruktur.
- Egen infrastruktur egner seg best for virksomheter som bruker og lagrer sensitiv eller gradert informasjon, for eksempel innen helse, kritisk infrastruktur og forsvar.
- Hybrid sky egner seg best for virksomheter som trenger å håndtere både sensitive og ikke-sensitive data og oppgaver, og som ønsker å kombinere kontroll med fleksibilitet.

Hva er allmenne skytjenester?

Hvis du bruker allmenne skytjenester blir modellen kjørt hos en global leverandør, for eksempel AWS, Azure, Google Cloud, eller direkte hos modell-leverandøren. Data sendes over internett til leverandørens datasentre.

Dette gjør det enkelt å komme i gang, det krever ingen egen infrastruktur og det er skalerbart. Fra et informasjonssikkerhetsperspektiv er dette en mer sårbar løsning, fordi data forlater virksomhetens kontroll. Hvor sikkert det er avhenger av leverandørens sikkerhetspolicy og rutiner og ikke minst lovgivning i landet der datasenteret ligger. Denne løsninger egner seg kanskje best for ikke-sensitiv data og rask prototyping.

Hva er privat sky?

Hvis du bruker privat sky blir modellen kjørt i et skymiljø som er dedikert for virksomheten, ofte med avtaler om at data ikke deles med andre kunder og at serverne ligger i spesifikke regioner eller land, for eksempel Europa eller Norge. Det gjør at du har et høyere nivå av sikkerhet.

Ulempen er at du fortsatt er avhengig av en ekstern leverandør for infrastruktur. Denne løsningen egner seg kanskje best for virksomheter med moderate sikkerhetskrav som ikke ønsker egen infrastruktur.

Hva er egen infrastruktur?

Hvis du bruker egen infrastruktur, kjører modellen på virksomhetens egne servere i eget datasenter. Data forblir fysisk i virksomhetens lokaler og det er liten eller ingen risiko for datalekkasje til eksterne.

Dette krever store investeringer og spesialisert kompetanse på drift, kjøling og sikkerhet. Denne løsningen egner seg kanskje best for virksomheter som bruker og lagrer sensitiv eller gradert informasjon, for eksempel innen helse, kritisk infrastruktur og forsvar.

Hva er hybrid sky?

Hybrid sky er et kjøremiljø som kombinerer skytjenester med lokal infrastruktur for virksomhetens sensitive data eller oppgaver. Skytjenestene kan være enten allmenne eller private for ikke sensitive data eller ikke-sensitive oppgaver.

Denne måten å gjøre det på sikrer god kontroll og ivaretar sikkerhet for senstive data, men gir god fleksibilitet og unngår at man investerer for mye ressurser i lokale infrastrukturløsninger. Hybrid sky krever at virksomheten har klare regler for hvilke data og oppgaver som skal ligge hvor.

[Neste stegUtarbeid kravspesifikasjon](https://ki.norge.no/veiledning/kom-i-gang-med-ki/utarbeid-kravspesifikasjon)
