---
veileder: "KI Norges veiledning om kunstig intelligens i offentlig sektor"
utgiver: "KI Norge (Digitaliseringsdirektoratet)"
kilde: "https://ki.norge.no/veiledning/gjor-dataene-ki-klare/forsta-behandling-av-sensitive-personopplysninger/anonymisere-og-pseudonymisere"
hentet: "2026-11-14"
---

# Anonymisere og pseudonymisere data

Når du bruker særlige kategorier av personopplysninger bør du som hovedregel anonymisere dataene. Hvis ikke det er mulig kan du pseudonomisere dem. Forskjellen er at anonymisering gjør at dataene ikke lenger kan spores tilbake til en person, og at de dermed ikke lenger regnes som personopplysninger.

Virksomheten bør bruke anerkjente metoder for anonymisering og pesudonymisering, i tråd med den internasjonale standarden ISO/IEC-20889. Ved valg av metode bør virksomheten vurdere risiko for muligheten for reidentifisering, blant annet i samsvar med [Datatilsynets veiledning om anonymisering av personopplysninger](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/hvordan-anonymisere-personopplysninger/) ,i tråd med personvernforordningen (GDPR).

## Anonymisere data

Målet er å fjerne koblingen til enkeltpersoner slik at dataene ikke lenger kan knyttes til en identifiserbar person. Når data er anonymisert på en tilstrekkelig måte omfattes de ikke lenger av personvernlovgivningen.

Du bør derfor alltid vurdere om dataene kan anonymiseres uten at det går vesentlig utover formålet. For eksempel at du kan analysere skjevhet i data også etter en anonymisering. Selv om anonymisering kan gjøre analysen noe mindre presis, bør du likevel anonymisere dataene.

## Pseudonymisere data

Hvis anonymisering ikke er mulig uten at det går vesentlig utover formålet bør du vurdere å pseudonymisere dataene.

Pseudonymisering betyr at du skjuler identiteten til enkeltpersoner ved å erstatte identifiserende opplysninger som fødselsnummer, med en kode eller et pseudonym. Samtidig lagres informasjonen som kobler koden til personen separat og sikres godt.

Når du pseudonymiserer data bør du

- erstatte direkte identifiserende opplysninger med pseudonymer
- beskytte koblingen mellom pseudonym og identitet
- begrense tilgang til denne koblingen til et fåtall autoriserte personer

Pseudonymiserte data regnes fortsatt som personopplysninger og er derfor omfattet av GDPR. Selv om risikoen reduseres er det fortsatt mulig å identifisere personer indirekte.

## Når du ikke kan anonymisere eller pseudonymisere

Hvis anonymisering eller pseudonymisering ikke er mulig uten at det i stor grad svekker analysen kan du bruke dataene uten å anonymisere dem. I slike tilfeller må du

- dokumentere hvorfor anonymisering ikke er hensiktsmessig
- begrunne hvilke konsekvenser anonymisering ville hatt for analysen

## Eksempel på å anonymisere og pseudonymisere

Fødselsnummer erstattes med en kode. Selve datasettet inneholder kun disse kodene, slik at personene ikke kan identifiseres direkte. Samtidig lagres en separat og godt sikret koblingsnøkkel som gjør det mulig å knytte kodene tilbake til riktige personer ved behov, koblingsnøkkelen er kun tilgjengelig for autoriserte brukere.
