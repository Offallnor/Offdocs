---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/kom-i-gang-med-ki/koble-data-til-ki"
hentet: "2026-11-14"
---

# 4. Implementere

1. [Koble data til KI?](https://ki.norge.no/veiledning/kom-i-gang-med-ki/koble-data-til-ki)
2. [Innfør og integrer KI-styring i styringsystemet](https://ki.norge.no/veiledning/kom-i-gang-med-ki/lag-styringssystem)
3. [Opplæring](https://ki.norge.no/veiledning/kom-i-gang-med-ki/opplering)

## Koble data til KI?

Når du er klar til å gå i produksjon, må du integrere KI-systemet i eksisterende systemer i virksomheten din. Uavhengig av om du skal utvikle eller kjøpe et KI-system, må du finne ut hvordan teknologien skal koble seg på virksomhetens data.

Du må også teste at integrasjonen er vellykket.

### Du kan velge mellom to hovedmetoder

API, Application Programming Interface**,** er den tradisjonelle måten å koble KI til data. Hver datakilde, for eksempel offentlige registere eller felles SharePoint i virksomheten, får en unik tilkobling.

MCP, Model Context Protocol, er en ny, åpen standard som fungerer som en «USB-port» for KI. Den lar modellen koble seg til ulike datakilder som lokale mapper, databaser eller API-er, ved hjelp av en standardisert driver.

Fordeler og ulemper med API

Ulempen med denne tilnærmingen er at hvis du trenger data fra mange ulike systemer, så må du ha tilsvarende antall koblinger. Når et system oppdateres, må koden for tilkoblingen oppdateres manuelt. Bruk av API gjør også at modellen ikke ser "hele bildet", den ser bare de dataene som er kodet inn for en spesifikk oppgave. Fordelen med API er at det er en etablert og kjent standard, som har vært tilgjengelig i lang tid og som finnes i de fleste systemer.

Fordeler og ulemper med MCP

Dette gjør det enklere å koble sammen mange systemer, i stedet for å bygge mange separate integrasjoner. Modellen får dermed en bedre forståelse av hele virksomhetens, ikke bare fragmenterte biter. Dette er viktig for å unngå feil i saksbehandling der informasjon ligger spredd i flere systemer.

MCP kan brukes der man ønsker å bygge KI-agenter som jobber på tvers av mange systemer uten omfattende manuell programmering. Men før du investerer i MCP, må du sørge for god kvalitet på data og god dataforvaltning i virksomheten. Ved MCP får du bedre oversikt og tilgang på egne data, men det gjør ikke at data i seg selv er strukturerte og av god kvalitet. Ved bruk av MCP er det viktig med klare styringsmekanismer for å unngå at økt tilgang til data fører til feilbruk eller sikkerhetsutfordringer.

[Neste stegInnfør og integrer KI-styring i styringsystemet](https://ki.norge.no/veiledning/kom-i-gang-med-ki/lag-styringssystem)
