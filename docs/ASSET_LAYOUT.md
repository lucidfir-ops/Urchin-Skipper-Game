# Canonical artwork and duplicate cleanup

The designer authorized cleaning the local file layout and deleting exact duplicates after tests. This supersedes the old requirement to retain separate source and distribution copies of identical artwork. The selected public GitHub backup is now published; follow the [current backup and release workflow](../PROJECT_STATUS.md#github-backup-and-release-workflow).

## Layout

- `public/assets/`: canonical game originals (PNG and editable SVG), plus distinct prepared runtime derivatives. Preserve originals here; this directory is not disposable.
- `assets/source/`: unique source artwork, contact sheet, extraction manifest and provenance notes.
- `assets/assets/`: unique supplied concept/reference sheets.
- `assets/vectors/`: Python authoring recipes and unique art studies.
- `assets/generated-review/`: new sheet extractions and vector recipe output awaiting review. Ignored by Git. Recipes do not overwrite canonical artwork. Inspect outputs before adopting any replacement; preserve the previous original before intentional edits.
- `assets/asset-integrity.json`: verified original SHA-256 fingerprints, byte sizes, canonical paths and former paths.

## Cleanup scope

80 redundant artwork files (80.17 MiB) were identified under `assets/`, matching 79 surviving files under `public/assets/`. Every proposed removal was verified by SHA-256 and direct byte comparison against its canonical survivor. The extra alias is `assets/source/workboat-overhead-v1.png`, which is identical to the fleet's `harbour workhorse.png`.

The 37 catalogued boat PNGs continue to be checked against original fingerprints. A separate regression checks every consolidated canonical asset against its recorded fingerprint and size. These expected values are preserved source evidence, not regenerated during tests.

Public asset filenames, bytes and game URLs remain the same. Different versions, processed textures, unique reference artwork, human documents, feedback, player data, archives and existing exports are outside the removal scope. Historical notes and embedded SVG metadata retain their original paths as provenance; the manifest resolves removed paths to surviving files.

Sheet extraction now creates a fresh `assets/generated-review/boat-sheet-individuals/` directory and refuses to reuse it. Python vector recipes write under `assets/generated-review/fleet-vector/`; their replace flag only applies to review output. The shipped SVGs include subsequent edits, so running an older recipe is not a lossless restore of those files.

## Verification

Completed: the original vessel-art regression passed before edits; all 411 unit tests and the production build passed both before and after removal. Lint and formatting checks for the edited JavaScript passed. All three Python vector recipes generated review files successfully in an isolated temporary directory. Every duplicate was compared directly to its survivor immediately before deletion; the complete set of 167 public asset paths and SHA-256 values was identical before and after cleanup. No UI/art bytes changed, so browser rendering checks were not rerun.

The initial sandboxed suite failed only on the launcher HTTP companion, matching the existing September 22 failure note. Running the suite outside that sandbox passed; launcher coverage was retained. The production build reports its existing large-chunk advisory.

No Git history changes or uploads were performed.
