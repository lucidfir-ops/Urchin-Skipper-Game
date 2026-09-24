# Urchin Skipper — current status
Updated 2026-09-23 · Latest game: touch controls, portrait recovery and audio scheduling.

Read this first, then task-relevant source/tests/references. The designer's [GitHub backup and release workflow](#github-backup-and-release-workflow) supersedes earlier no-GitHub directions and retains additive local TEMP itch.io ZIPs. [Local duplicate-artwork cleanup](docs/ASSET_LAYOUT.md) is complete. [Previous status](docs/history/2026-09-23-touch-and-portrait/PROJECT_STATUS-before.md) is preserved. Gameplay remains governed by the DOCX and explicit amendments, including [September 21](docs/FEEDBACK_SEPTEMBER21.md) and [September 23](docs/FEEDBACK_SEPTEMBER23.md).

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, commit and push the selected source/assets to public GitHub and create new dated TEMP itch.io and local/Wi-Fi exports. Preserve older exports; report the commit, export paths and any upload failure. [Full policy and exclusions](AGENTS.md#github-backup-and-temp-exports).

The [minimal checkout](docs/github-backup-review/README.md) is prepared at `.github-backup/checkout/` with its own empty Git repository, separate from the full workspace's existing import history. Fresh `npm ci`, lint, formatting, 410 passing tests (one private-save regression skipped) and production build pass there. Exactly 533 selected files are visible to Git; generated/dependency/private files are ignored. First commit and publication remain pending, one step at a time. Public visibility is confirmed by the designer's GitHub screenshot. Git write access remains to be checked by the first push; nothing has been uploaded. Publish from the prepared repository, not the full workspace's large import history.

## Design authority

[Urchin Skipper Bible — Definitive v2](Urchin_Skipper_Bible_Definitive_v2.docx) is the sole definitive design, with explicit subsequent designer amendments taking precedence. The DOCX and §23 approved harbour reference are unchanged. Implementation notes/tests do not establish full-Bible compliance. Preserve the orthographic camera and separation between decoration and simulation geometry.

## Current implementation

- **Local asset cleanup:** 80 byte-identical copies consolidated into 79 canonical files under `public/assets/`, saving 80.17 MiB. All 167 runtime asset paths/bytes are unchanged. Originals are protected by recorded hashes; recipes write review output separately. [Layout, provenance and verification](docs/ASSET_LAYOUT.md).

- **Touchscreen Options** is available from title, Settings and Pause, including Frank's lesson. It groups touch mode, Tiny Touch Controls, 50–150% control scale, 0–100% opacity, reset, Adjust UI and Show information. Native sliders, preview and controller adjustments save per browser. Menu/help remains visible. Tiny's old UI multiplier is retired; ordinary saved portrait/landscape arrangements and old-export preferences remain stored. UI Scale stays independent.
- Rotation unlock retries on focus, visibility, viewport/fullscreen changes and touch, with one delayed retry. The harbour header sizes to its information and no longer grows over Settings at low UI Scale. Portrait defaults follow the phone reference with independent instruments, chart/current/load below and prompts above the measured helm area. Saved layouts retain priority.
- Engine pitch updates avoid unchanged per-frame Phaser loop rescheduling. Opt-in local logs now include frame/CPU summaries, audio context and orientation transitions. Physical Android confirmation is outstanding. [Tablet assessment](docs/DOOGEE_TAB_E3_MAX_REPORT_2026-09-23.txt).
- September 22's prepared artwork/all fifteen eager maps, terrain worker/fallback, immutable grids, validated saves, cached render/simulation work, short Chart tap repair and independent instrument fixes remain. [Technical evidence](docs/history/2026-09-22-performance-and-device-fixes/README.md).
- Harbour time pause, 05:00 planning, 07:00/Sleep options, delayed offload, fatigue/freshness, level-20 crew progression and fictional nitrogen/surface-break mechanics remain. Nine original maps plus six added sectors, rivals, wildlife, Easy grounding assistance and Realistic handling remain. Right-stick jet pivot and installed bow thruster remain; USB Xbox is the known physical baseline.
- Named restore/day-start saves, migration and troubleshooting exports remain. No gameplay proposal was implemented: [fun recommendations for designer review](docs/GAMEPLAY_RECOMMENDATIONS_2026-09-23.txt). Original assets/media, careers and prior exports are preserved.

## Verification and latest exports

Local asset cleanup: 411 tests, lint, edited-JavaScript formatting and production build pass after removal. No new gameplay export was needed; existing exports remain intact. The following browser/device acceptance describes the unchanged gameplay release.

410 unit regressions, lint, formatting and production build pass. Chromium and Firefox pass persistent touch settings/native slider dragging, title career preservation, harbour hit tests across 50–150% UI Scale, 50–150% touch controls across five viewports, opacity escape/reset, rotation recovery and game-owned fullscreen. Both pass audio scheduling/gear checks and existing normal/crowded frame-time budgets. Chromium passes tablet/S22/Deck synthetic-controller journeys, nested cross-origin hosting with host-owned fullscreen in both orientations, and the saved-layout/offline-preparation regression. Runtime screenshots are inspected. [Current acceptance and limits](docs/history/2026-09-23-touch-and-portrait/README.md).

Release: **TEMP · SEP 23 · TOUCH & PORTRAIT**.

- [itch.io TEMP ZIP](exports/2026-09-23-touch-and-portrait/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-23-touch-and-portrait/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-23-touch-and-portrait/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.

Exports are additive, profile-free and verified against the compiled build. Preserve older exports; do not recreate deleted checkpoints. [Data preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): actual phone/tablet rotation on itch with OS auto-rotate, speakers/headphones, USB Xbox/built-in Deck, crowded night/fog trips and full seasons. Desktop browser tests do not certify physical input, tablet FPS or elimination of intermittent hangs. The measured audio improvement removes one demonstrated cost; remaining device hitches need the new local logs. Long-season balance and full-Bible compliance remain unfinished. [Failure notes](docs/FAILURE_NOTES.md) retain significant lessons.
