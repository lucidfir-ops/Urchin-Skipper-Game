# Urchin Skipper — current status
Updated 2026-09-23 · Documentation: living Bible consolidation. Latest game: touch controls, portrait recovery and audio scheduling.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) consolidates current approved design; historical amendments are provenance only. The designer's [GitHub backup and release workflow](#github-backup-and-release-workflow) retains additive local TEMP itch.io ZIPs. [Local duplicate-artwork cleanup](docs/ASSET_LAYOUT.md) is complete. [Status before this documentation cleanup](docs/history/2026-09-23-bible-consolidation/before/PROJECT_STATUS.md) is preserved.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, commit and push the selected source/assets to public GitHub and create new dated TEMP itch.io and local/Wi-Fi exports. Preserve older exports; report the commit, export paths and any upload failure. [Full policy and exclusions](AGENTS.md#github-backup-and-temp-exports).

Public backup: [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. First successful source upload: `3b6d59d59a5f51358b40bb860e53098b7b2cbc07`. The minimal repository is `.github-backup/checkout/` in the full authoring workspace, separate from the large local import history. Publish from that repository; synchronize future selected source changes into it before verification and pushing. Existing clones can use their own `main` normally.

The initial standalone 533-file checkout passed fresh `npm ci`, lint, formatting, 410 unit tests (one private-save regression skipped) and production build. The selected backup now also includes the living Bible, its references and the narrowly scoped preserved design archive. Dependencies, generated ZIPs, private data and unrelated historical screenshots remain excluded. [Selection and verification receipt](docs/github-backup-review/README.md) are local authoring records.

GitHub CLI is installed locally at `.runtime/github-cli/2.101.0/bin/gh`; browser authentication as `lucidfir-ops`, public visibility, push permission and the HTTPS credential helper are confirmed. Credentials stay outside the backup. Routine verified game updates now use the standing GitHub-plus-TEMP export workflow.

## Design authority

[bible.md](bible.md) is the single current design authority. The designer authorized this consolidation, permanently fixed two working diver berths per boat, confirmed **Shy Hull Wood**, and reconfirmed the Settings reference within reason. Future approved decisions update the relevant Bible sections in place. Proposals, implementation notes and tests do not establish design approval or full compliance.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) are archived byte-for-byte; [reference images](docs/reference/bible/README.md) retain their original bytes. The DOCX includes the September 20 Settings addition; previous blanket wording that it was unchanged was inaccurate. [Source mapping and supersession](docs/DESIGN_CONSOLIDATION.md). Preserve the orthographic camera, approved harbour and separation of decoration from simulation geometry.

## Current implementation

- **Local asset cleanup:** 80 byte-identical copies consolidated into 79 canonical files under `public/assets/`, saving 80.17 MiB. All 167 runtime asset paths/bytes are unchanged. Originals are protected by recorded hashes; recipes write review output separately. [Layout, provenance and verification](docs/ASSET_LAYOUT.md).

- **Touchscreen Options** is available from title, Settings and Pause, including Frank's lesson. It groups touch mode, Tiny Touch Controls, 50–150% control scale, 0–100% opacity, reset, Adjust UI and Show information. Native sliders, preview and controller adjustments save per browser. Menu/help remains visible. Tiny's old UI multiplier is retired; ordinary saved portrait/landscape arrangements and old-export preferences remain stored. UI Scale stays independent.
- Rotation unlock retries on focus, visibility, viewport/fullscreen changes and touch, with one delayed retry. The harbour header sizes to its information and no longer grows over Settings at low UI Scale. Portrait defaults follow the phone reference with independent instruments, chart/current/load below and prompts above the measured helm area. Saved layouts retain priority.
- Engine pitch updates avoid unchanged per-frame Phaser loop rescheduling. Opt-in local logs now include frame/CPU summaries, audio context and orientation transitions. Physical Android confirmation is outstanding. [Tablet assessment](docs/DOOGEE_TAB_E3_MAX_REPORT_2026-09-23.txt).
- September 22's prepared artwork/all fifteen eager maps, terrain worker/fallback, immutable grids, validated saves, cached render/simulation work, short Chart tap repair and independent instrument fixes remain. [Technical evidence](docs/history/2026-09-22-performance-and-device-fixes/README.md).
- Harbour time pause, 05:00 planning, 07:00/Sleep options, delayed offload, fatigue/freshness, level-20 crew progression and fictional nitrogen/surface-break mechanics remain. Nine original maps plus six added sectors, rivals, wildlife, Easy grounding assistance and Realistic handling remain. Right-stick jet pivot and installed bow thruster remain; USB Xbox is the known physical baseline.
- Named restore/day-start saves, migration and troubleshooting exports remain. No gameplay proposal was implemented: [fun recommendations for designer review](docs/GAMEPLAY_RECOMMENDATIONS_2026-09-23.txt). Original assets/media, careers and prior exports are preserved.
- [Brief how-to-play text](HOW_TO_PLAY.txt) is ready for the itch.io release description. Controls, separate bag/redescent actions and return timing were checked against the current build; this documentation addition changes no game bytes.

## Verification and latest exports

Bible consolidation: all 23 original sections reconciled with recorded amendments and fresh designer answers; four archived files and three reference images hash-verified, and all 56 links in the new documents resolve. The 412 selected runtime/test/config files are unchanged. Local `npm test` passes all 411 tests and production build matches the existing release's 174 files byte-for-byte. The synchronized public checkout passes lint, formatting, 410 tests (one private-save check skipped) and build. This is a documentation-only update; the following playable exports remain current.

Local asset cleanup: 411 tests, lint, edited-JavaScript formatting and production build pass after removal. No new gameplay export was needed; existing exports remain intact. The following browser/device acceptance describes the unchanged gameplay release.

410 unit regressions, lint, formatting and production build pass. Chromium and Firefox pass persistent touch settings/native slider dragging, title career preservation, harbour hit tests across 50–150% UI Scale, 50–150% touch controls across five viewports, opacity escape/reset, rotation recovery and game-owned fullscreen. Both pass audio scheduling/gear checks and existing normal/crowded frame-time budgets. Chromium passes tablet/S22/Deck synthetic-controller journeys, nested cross-origin hosting with host-owned fullscreen in both orientations, and the saved-layout/offline-preparation regression. Runtime screenshots are inspected. [Current acceptance and limits](docs/history/2026-09-23-touch-and-portrait/README.md).

Release: **TEMP · SEP 23 · TOUCH & PORTRAIT**.

- [itch.io TEMP ZIP](exports/2026-09-23-touch-and-portrait/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-23-touch-and-portrait/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-23-touch-and-portrait/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.

Exports are additive, profile-free and verified against the compiled build. Preserve older exports; do not recreate deleted checkpoints. [Data preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): actual phone/tablet rotation on itch with OS auto-rotate, speakers/headphones, USB Xbox/built-in Deck, crowded night/fog trips and full seasons. Desktop browser tests do not certify physical input, tablet FPS or elimination of intermittent hangs. The measured audio improvement removes one demonstrated cost; remaining device hitches need the new local logs. Long-season balance and full-Bible compliance remain unfinished. [Failure notes](docs/FAILURE_NOTES.md) retain significant lessons.
