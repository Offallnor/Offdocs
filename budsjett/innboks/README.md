# Innboks for budsjettdokumenter

Legg budsjettdokumenter her, så legges de inn i `budsjett/` automatisk i løpet av et par minutter.

## Slik gjør du

1. Last ned dokumentet fra regjeringen.no (Word for proposisjoner, Excel for datagrunnlaget).
2. Døp filen om etter mønsteret under. `ÅR` er budsjettåret, for eksempel 2027 for Prop. 1 S (2026–2027).
3. Åpne mappen `budsjett/innboks` på GitHub, velg **Add file → Upload files**, dra inn filene, velg **Commit directly to the main branch** og trykk **Commit changes**.

| Filnavn | Dokument | Havner i |
|---|---|---|
| `prop-1-s-ÅR-aid.docx` | Prop. 1 S for AID | `budsjett/ÅR/prop-1-s-aid/` |
| `prop-1-s-ÅR-tillegg-N.docx` | Prop. 1 S Tillegg N (endring av forslaget, alle departementer) | `budsjett/ÅR/prop-1-s-tillegg-N/` |
| `gul-bok-ÅR.docx` | Prop. 1 S Gul bok | `budsjett/ÅR/gul-bok/` |
| `nasjonalbudsjettet-ÅR.docx` | Meld. St. 1 Nasjonalbudsjettet | `budsjett/ÅR/nasjonalbudsjettet/` |
| `gul-bok-bevilgninger-ÅR.xlsx` | Datagrunnlag til Gul bok (alle departementer, kroner) | `budsjett/ÅR/gul-bok-bevilgninger.tsv` |
| `statsregnskapet….zip` eller `.csv` | Statsregnskapet fra DFØ (statsregnskapet.dfo.no/last-ned), alle departementer | `budsjett/ÅR/statsregnskap/` for hvert år i filen |

Statsregnskapet lastes ned fra DFØ som zip med rådata. Filnavnet må begynne på `statsregnskapet`, og årene leses fra filen. Hele historikken er for stor til å lastes opp i nettleseren (over 25 MB), så velg bare de årene som er nye eller endret, oftest inneværende og forrige år. Et år som allerede ligger inne, skrives på nytt.

Word-filer fra regjeringen.no (Prop. 1 S, Gul bok, Tillegg og Nasjonalbudsjettet) kjennes igjen på forsiden, så de kan lastes opp med navnet de har når de lastes ned, f.eks. `prp202520260001aidddddocx.docx`. Budsjettåret og dokumenttypen leses da fra forsiden. Sier filnavnet og forsiden ulike ting, stoppes filen. Eldre proposisjoner som bare finnes som RTF (i zip-filen fra regjeringen.no) eller EPUB, kan lastes opp som de er. De gjøres om til Word automatisk. Excel-filer og statsregnskapet må fortsatt døpes om.

**Last aldri opp samledokumenter med svar på budsjettspørsmål.** De kan ha svar som ikke er publisert, og alt som lastes opp her, er åpent med en gang. Svarene legges inn fra regjeringen.no.

Du kan laste opp flere filer samtidig. Tall (datagrunnlaget) kan gå lenger tilbake enn tekst (proposisjonene).

## Hva som skjer

- Word-filene deles i én fil per kapittel eller delkapittel. Selve Word-filen slettes etterpå, siden den ligger på regjeringen.no.
- Statsregnskapet summeres per kapittel og post, per måned, per artskonto og per virksomhet. Filen slettes etterpå.
- Excel-filen gjøres om til TSV. Første rad må ha kolonnene `kap_nr`, `post_nr` og `beløp`.
- `budsjett/VEIVISER.md` får en oversikt over hvilke år som ligger i basen.
- **Ny versjon:** Last opp en fil med samme navn, så erstattes den gamle mappen.

## Når noe stopper

Jobben legger ikke inn noe den er usikker på. Filen blir da liggende her, og en fil med samme navn og `.FEIL.txt` forklarer hvorfor. Vanlige grunner:

- Filnavnet passer ikke mønsteret.
- Word-filen har andre stilnavn enn dagens utgaver fra regjeringen.no. Eldre år kan ha en annen oppbygning.
- Excel-filen har ikke de forventede kolonnene.

Rett opp og last opp filen på nytt. `.FEIL.txt`-filen forsvinner når filen er lagt inn.
