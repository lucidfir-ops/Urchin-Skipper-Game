# Data ownership and restoration

| Category | Location | Treatment |
| --- | --- | --- |
| Source / configuration | `src/` (excluding generated exports), `world-source/`, `scripts/`, `tests/`, package manifest/lock, HTML/CSS and notes | Preserve authoring inputs; retain verified playable releases in additive exports. |
| Irreplaceable input | Living `bible.md`, archived human design documents, approved images in `docs/reference/bible/`, feedback video, canonical original artwork in `public/assets/`, unique references/source in `assets/`, future `data/raw/` | Preserve original documents/images; make approved design edits in the living Bible with version history. Never preprocess original assets in place. |
| Generated game data/assets | `src/generated/`, prepared `public/assets/fleet-runtime/` derivatives, runtime textures, future `data/derived/`, `dist/` | Rebuild from recipes and raw inputs; retain dated game exports for playable version restoration. |
| Career / player data | Dedicated `.runtime/firefox-profile/` browser localStorage; exported `urchin-career-day-*.json` | Irreplaceable progress. Keep the profile. Use Skipper logbook → Export career backup and copy exports into `data/careers/` for independent preservation alongside game exports. Starting another career archives the previous one in the same profile. |
| Disposable output | `node_modules/`, `.npm-cache/`, `.browser-cache/`, `.runtime/` launcher logs/session files (excluding the browser profile), `test-results/` | Disposable except for the live browser profile. The running browser profile is excluded from source checkpoints; never delete it as routine cache cleanup. |

No raw GIS data is included yet. Future `data/raw/<publisher>/<dataset-version>/` should contain untouched downloads plus a source manifest with checksum, acquisition date, licence and attribution. Generated/cleaned/interpolated versions go elsewhere.

Canonical artwork now lives in `public/assets/`: the supplied title, fleet originals, harbour art and atlases serve directly as game assets. Unique source art stays under `assets/`. [Asset layout and verification](../docs/ASSET_LAYOUT.md) records the designer-authorized cleanup; [fingerprints and former paths](../assets/asset-integrity.json) preserve provenance. Canonical originals are irreplaceable, even inside `public/`. `npm run build` copies game assets to disposable `dist/`.

## Git source and local game exports

The designer subsequently requested a minimal public GitHub backup, proceeding one step at a time, and authorized local duplicate cleanup. The verified minimal repository is now published; future verified game updates follow the [standing GitHub-plus-TEMP workflow](../AGENTS.md#github-backup-and-temp-exports). Local additive TEMP ZIPs remain the game-delivery workflow. [Backup review](../docs/github-backup-review/README.md). The setup below describes the existing local Git state, not the minimal public selection.

The September 23 GitHub setup tracks editable source, tests, scripts, design documents, original artwork and required runtime assets. It preserves the existing additive game-export workflow. `.gitignore` excludes dependencies, caches, `dist/`, `exports/`, `feedback/`, careers, browser profiles, credentials, environment files and machine-local state; ignored files remain on disk. Curated design/verification history remains source documentation, while raw `.log` files stay local.

Generate new itch.io and local/Wi-Fi ZIPs with the unchanged `scripts/package-temp.py`; see the [root README](../README.md#itchio-game-zips). Git uploads do not package or publish those ZIPs. Source-only clones can run the synthetic unit regressions without any saved player data; an optional private-save regression also runs when its original or archived local feedback file exists.

## September 16 preservation amendment

The designer deleted the large checkpoints and now uses `exports/` to preserve previous playable game versions. Do not run routine source checkpoints or recreate deleted archives. Keep older exports and create each new release in a new dated folder; `scripts/package-temp.py` verifies ZIP contents against the built files. Extract a retained local/Wi-Fi ZIP into a new directory to run that version, or upload the matching itch.io ZIP. These exports preserve game builds, not the editable source, design documents or player saves; retain those originals separately in place.

The old checkpoint tool remains available for explicitly requested source recovery work. Its historical policy included accumulated exports in each archive, causing unnecessary duplication; it is no longer the routine release workflow. Live browser profiles remain outside game exports. Use the game's logbook to export irreplaceable careers.

The living [bible.md](../bible.md) is the definitive design. The [former DOCX](../archive/design/2026-09-23/Urchin_Skipper_Bible_Definitive_v2.docx) and older PDF are historical originals; keep them intact. Approved images are preserved under [design references](../docs/reference/bible/), including the harbour composition formerly embedded in §23. Historical amendment ledgers retain provenance rather than independent design authority.

September 15: `public/assets/harbour/harbour-training-mode-v1.png` is a byte-identical copy of the supplied source. Portable packages are reproducible generated exports; see [TEMP recipe](../DEVELOPMENT_NOTES.md#september-15-feedback). Existing TEMP archives/profiles outside this workspace are retained.


September 15 follow-up: the preferred static web export is `exports/2026-09-15-itch/UrchinSkipper-TEMP-ITCHIO.zip`; the adjacent local/LAN ZIP uses the same verified dist bytes. Both are reproducible with `scripts/package-temp.py` and exclude live browser profiles. [Decision/recipe](../docs/FEEDBACK_ITCH_TEMP.md#packaging). New hidden ground is additive recipe v6; old reef coordinates/stock survive migration.

September 15 keyboard update: both new, additive exports are under `exports/2026-09-15-keyboard/`. [Control migration and packaging](../docs/FEEDBACK_KEYBOARD_CONTROLS.md) preserve all older copies and player data.


September 16: portable launches can create `.player-data/firefox-profile/` inside an extracted TEMP directory, including one under `exports/`. These are live player data, preserved in place and excluded from source checkpoints. Export their careers from the game's logbook before transferring them. New profile-free TEMP exports live under `exports/2026-09-16-s22/`; [recipe and behavior](../docs/FEEDBACK_S22_FRANK.md).
