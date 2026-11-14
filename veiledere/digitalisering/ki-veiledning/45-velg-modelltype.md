---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-modelltype"
hentet: "2026-11-14"
---

# 2. Anskaffe, utvikle eller videreutvikle

1. [Undersøk markedet](https://ki.norge.no/veiledning/kom-i-gang-med-ki/undersok-markedet)
2. [Forstå prismodeller](https://ki.norge.no/veiledning/kom-i-gang-med-ki/forsta-prismodeller)
3. [Velg modelltype](https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-modelltype)
4. [Velg kjøremiljø](https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-kjoremiljo)
5. [Utarbeid kravspesifikasjon](https://ki.norge.no/veiledning/kom-i-gang-med-ki/utarbeid-kravspesifikasjon)

## Velg modelltype

«Åpen» og «lukket» modell handler om du får se hvordan KI-modellen bearbeider og vektlegger informasjon, hvordan modellen kommer frem til et svar. Dette kalles "vekter".

En åpen modell deler disse vektene med alle, og gir deg muligheten til å laste dem ned og kjøre dem på egen infrastruktur eller på egne skybaserte kontoer. Eksempler inkluderer Llama-serien (Meta) og Mistral.

En lukket modell viser deg bare svaret. Koden og vektene er hemmelige. Modellene eies av en enkelt leverandør, for eksempel OpenAI, Anthropic og Google.

### Hvilken modell passer til hva?

For oppgaver med høy sensitivitet, bør du velge åpne vekter-modeller eller lukkede modeller i privat sky. Vær oppmerksom på at det innebærer betydelige kostnader til infrastruktur og vedlikehold. Eksempler på oppgaver med høy sensitivitet er når KI skal behandle personopplysninger eller sikkerhetsstemplet informasjon.

For mindre sensitive oppgaver, som intern kommunikasjon og generelle søk, kan lukkede modeller være et praktisk alternativ, så lenge passende sikkerhetstiltak som for eksempel kryptering eller dataredaksjon er implementert. Det er også viktig å ha en bevisst holdning til om leverandøren bruker data i modelltrening.

Fordeler og ulemper med lukkede modeller

De lukkede modellene er ofte de mest avanserte på markedet, spesielt for komplekse oppgaver. Leverandøren håndterer all infrastruktur, oppdateringer og sikkerhet og du har tilgang til kundestøtte og serviceavtaler.

De åpne modellene yter litt dårligere enn de lukkede, men mange mener at dette gapet er i ferd med å minske raskt.

Ulempene med de lukkede er at du har mindre kontroll. Du vet ikke nøyaktig hvordan modellen fungerer, hvilke data den er trent på, eller hvordan den tar beslutninger. Dataene dine blir sendt til leverandørens servere, så du er avhengig av leverandørens garantier om at data ikke brukes til trening. Det er sjelden du kan forhandle om brukervilkårene, de kan gå i din disfavør, for eksempel ved at det kan bli vanskelig å bytte tjeneste senere.

Kostnader er også et element her. Prisene kan være høye og uforutsigbare ved stort volum (token-basert). Dette fører til at virksomheten har en større avhengighet til leverandøren og blir påvirket av prisendringer og funksjonsendringer.

Fordeler og ulemper med åpne modeller

Fordelene med en åpen modell er at du kan inspisere den, justere den og forstå hvordan den fungerer bedre. Du har kontroll på dataene fordi de forblir i virksomhetens eget nettverk. Ingen data sendes til eksterne leverandører.

Det kan potensielt gi bedre kontroll over kostnader ved at du betaler for infrastruktur (servere/GPU-er) istedenfor per token. Ved høyt volum kan dette bli billigere. Det gir også mer forutsigbarhet og mindre sårbarhet for leverandørens fremtidige beslutninger.

Dette er en mer krevende løsning for virksomheter. Det krever mer egen kompetanse på drift, sikkerhet, oppdatering og skalering. Virksomhetene har et tydeligere ansvar, for sikkerhet og eventuelle feil i modellen.

[Les mer om valg av modell i rapporten "KI-assistenter i arbeidslivet"](https://www.regjeringen.no/contentassets/6332353676204e90a0ab94f9c968f967/no/pdfs/veileder-til-bruk-av-ki-assistenter.pdf)

[Neste stegVelg kjøremiljø](https://ki.norge.no/veiledning/kom-i-gang-med-ki/velg-kjoremiljo)
