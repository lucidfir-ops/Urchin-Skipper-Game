# Urchin Skipper — current status
Updated 2026-09-24 · Latest game: automatic aboard-diver deployment, phone fullscreen wording and tablet rendering improvements.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) is the approved design authority. [Previous status](docs/history/2026-09-24-deploy-and-tablet/before/PROJECT_STATUS.md) preserves the rotation/helm and crew/coasts handoff.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, synchronize the selected source/assets into `.github-backup/checkout/`, verify there, and commit/push to [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. Create new dated local TEMP itch.io and local/Wi-Fi exports. Preserve older exports and report any upload failure. [Full policy](AGENTS.md#github-backup-and-temp-exports).

Use the separate minimal repository, never the full workspace's large older import history. Include new required source/assets; retain the checkout's stricter ignore rules. Ordinary clones can use their own `main`. Dependencies, caches, exports, player data, credentials and unrelated history stay excluded. [Exact publication, selection and verification receipts](docs/github-backup-review/README.md) are local authoring records. GitHub CLI/credential helper is configured at `.runtime/github-cli/2.101.0/bin/gh` as `lucidfir-ops`.

## Design authority

[bible.md](bible.md) is the single living specification. The September 23 consolidation permanently fixes two working diver berths, confirms **Shy Hull Wood** and retains the approved Settings reference within reason. Subsequent crew/coasts, rotation/helm and tablet decisions are recorded in their relevant Bible sections; [request provenance](docs/DESIGN_CONSOLIDATION.md#september-24-tablet-follow-up). The longer crew/relationship document remains a proposal beyond approved speech behavior. Current implementation and tests do not establish full-Bible compliance.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) and [approved reference images](docs/reference/bible/README.md) remain intact. Preserve the orthographic camera, harbour reference and separation of decoration from simulation geometry.

## Current implementation

- Deploy / board chooses an eligible diver aboard even when the underwater diver is selected. If both aboard divers are eligible, selection chooses who deploys. Nearby recovery and active deck work keep priority; safety checks and pinned input targets remain. Individual orders and future specialist selection are retained.
- Recall reaches five metres from the hull, covering pickup positions including the bow/stern. It remains a local, delayed hull clang. One-press bag take/give and nearby boarding retain selection-independent targeting.
- Title, Settings and Pause now say **Fullscreen & Rotate screen**. This is the requested temporary phone workaround. Existing orientation recovery remains; the designer confirms tablet portrait startup and working neutral-current rudder response. Physical phone automatic rotation remains unresolved.
- Deck load defaults on for fresh Easy/Realistic presets. Saved manual choices and All Off are preserved. Older labelled minimaps have a direct **Chart only** footer shortcut; the labelled Graphic and Plain text options remain in Arrange UI. New minimaps already default to chart only.
- Dry weather shading reuses its full-screen Canvas until visible conditions change. Rain, lightning, fog, rotation/resizing and turning work lights remain responsive. Decorative foam uses elapsed-time cohorts and swept shoreline checks; physical boat/diver/log/current/collision simulation retains its cadence. Unchanged touch text is retained. Troubleshooting downloads now identify this release correctly.
- Prior handling, gentler bow thrust, crew reports/quality/bag-time orders, fatigue, regional weather, taxi passes, grounding/rescue, red deck bags/dumping, buyer contracts, individual earnings, chart marks and equipment switches remain. Saved hull identity, +50% default pace, prepared artwork, validated saves, independent layouts, audio scheduling and known-good USB Xbox mappings are preserved. [Previous implementation](docs/history/2026-09-24-deploy-and-tablet/before/PROJECT_STATUS.md), [player guide](HOW_TO_PLAY.txt).

## Verification and latest exports

Authoring lint, formatting, **454 tests** and production build pass. The standalone public checkout passes **453 tests plus one intentional private-save skip**; all **174 compiled files** match the authoring build and local export. Synthetic controller checks pass remapping, automatic second-diver deployment, bag/boarding, range pause, restart, disconnect and exit. Production Chromium/Firefox touch journeys cover unselected aboard-diver deployment, fresh departure/reload, default load gauge, plain-chart persistence and fullscreen wording in phone/tablet portrait and landscape. Runtime screenshots are inspected. Isolated production renderer/seven-vessel benchmarks pass the existing software budgets. [Detailed evidence and limits](docs/history/2026-09-24-deploy-and-tablet/README.md); [backup publication receipts](docs/github-backup-review/README.md).

An isolated desktop Canvas diagnostic at 864×1296 improved mean frame time from 29.46 to 18.98 ms, with p95 still around 33.3 ms and occasional long stalls. This is not physical tablet FPS. The recorded blank first departure has **not been reproduced or diagnosed**; it is not claimed fixed.

Release identity: **TEMP · SEP 24 · DEPLOY & TABLET**.

- [itch.io TEMP ZIP](exports/2026-09-24-deploy-and-tablet/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-24-deploy-and-tablet/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-24-deploy-and-tablet/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.
- Older exports remain intact, including `exports/2026-09-24-rotation-and-helm/`, `exports/2026-09-24-crew-and-coasts/` and prior dated folders. TEMP ZIPs stay local for the designer's itch upload.

Exports exclude player profiles. Preserve older exports; do not recreate deleted checkpoints. [Data preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): automatic deployment through a full two-diver work cycle; recall around the hull; existing chart-only preferences; phone fullscreen/rotation; sustained tablet FPS and the recorded blank departure. Enable the optional troubleshooting log before reproducing that freeze and download it afterward. Tablet model/browser and a physical device debugging connection were unavailable in this pass. Synthetic browser/controller input does not establish physical device behavior.

Continue crowded night/fog/traffic scenes, speakers/headphones, Deck/controller hardware, loaded light-current handling, starter storms, falling-tide rescue, fatigue and long-season economics. Long-season balance and full-Bible compliance remain unfinished. [Failure notes](docs/FAILURE_NOTES.md) record causes and successful alternatives.
