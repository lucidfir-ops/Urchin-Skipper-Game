# Urchin Skipper — current status
Updated 2026-09-23 · Latest game: working-day handling, deck/pickup, markets, crew and equipment.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) is the approved design authority. [Previous status](docs/history/2026-09-23-working-day/before/PROJECT_STATUS.md) preserves the earlier touch/portrait and documentation handoff.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, synchronize the selected source/assets into `.github-backup/checkout/`, verify there, and commit/push to [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. Create new dated local TEMP itch.io and local/Wi-Fi exports. Preserve older exports and report any upload failure. [Full policy](AGENTS.md#github-backup-and-temp-exports).

Use the separate minimal repository, never the full workspace's large older import history. Include new required source/assets; retain the checkout's stricter ignore rules. Ordinary clones can use their own `main`. Dependencies, caches, exports, player data, credentials and unrelated history stay excluded. [Exact publication, selection and verification receipts](docs/github-backup-review/README.md) are local authoring records. GitHub CLI/credential helper is configured at `.runtime/github-cli/2.101.0/bin/gh` as `lucidfir-ops`.

## Design authority

[bible.md](bible.md) is the single living specification. September 23 consolidation permanently fixes two working diver berths, confirms **Shy Hull Wood** and retains the approved Settings reference within reason. This follow-up explicitly authorizes the working-day changes now recorded in relevant Bible sections. [Implementation notes](docs/WORKING_DAY_2026-09-23.md) explain the build; the [longer crew/relationship document](docs/CREW_RELATIONSHIPS_PROPOSAL.txt) remains a proposal beyond its shipped surface-bubble first pass.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) and [approved reference images](docs/reference/bible/README.md) remain intact. [Source mapping](docs/DESIGN_CONSOLIDATION.md). Preserve the orthographic camera, harbour reference and separation of decoration from simulation geometry. Historical amendments, tests and implementation notes do not override the Bible.

## Current implementation

- Boat reload repairs a stale harbour selection from the owned saved trip hull. Renderer textures own copied canvases and receive an explicit initial GPU upload; preview caches remain separate. Automated checks cover all twelve hulls, both art modes and both renderers. The original intermittent device symptom was not conclusively reproduced.
- Neutral handling uses water-relative bow/stern loads: shaft rudders turn in current, legs/outboards have weaker passive authority, jets have none. Legs/jets turn beam-on more readily; wind acts independently. Larger hulls have more environmental exposure and stopping/turning momentum; cargo adds inertia. Powered maneuvering regressions remain intact.
- Fixed-size red deck bags stay inside the rails, overlap and form layers. Visible surfaced-diver cues show distance/readiness; short cartoon bubbles express the actual sampled catch/fatigue. Last recovered quality and per-bag inspection/dumping are available. Dumping takes original hauling time, reserves deck work and survives reload.
- Harbour office/departure planning offer optional capped buyer orders, with two initial contacts and premium/bulk contacts unlocked by sales and safe returns. Partial qualifying loads receive a premium; excess/low quality sells normally. Return-now estimates include travel/aging. Saved legacy agreements are honored once; new days offer a fresh choice. Crew shares follow actual bag earnings.
- Offload receipts include up to three factual trip highlights. Chart reports retain witness, age, sampled position and tide context; save sample marks and follow their bearing/distance without revealing hidden bed boundaries.
- Two persistent rival teams sometimes encroach on actively worked beds and physically reduce shared stock. Nearby names/radio identify encounters, including Shy Hull Wood. Taxi itineraries more often cross worked ground and actual fast close passes trigger warnings. Existing traffic participation and unusual-event/rare-radio cadence remain.
- Owned upgrades have saved per-hull switches with operating guards for fuel, divers and deck work. Working lights automatically run after dark, can be disabled and cast cached feathered light pools. New browser pace defaults to **+50%**; explicit saved preferences remain.
- Touchscreen Options, saved independent portrait/landscape layouts, orientation recovery, reduced audio scheduling, prepared artwork/all fifteen maps, validated saves and prior device fixes remain. [Previous acceptance](docs/history/2026-09-23-touch-and-portrait/README.md). Asset bytes/runtime paths remain preserved by the [canonical asset layout](docs/ASSET_LAYOUT.md).
- Harbour pause/planning, return/offload timing, fatigue/freshness, crew progression/exposure, two-diver orders, separate bag/recovery actions, grounding assistance and original physical maps remain. [Player guide](HOW_TO_PLAY.txt). No new sinking system or severe-weather departure prohibition was added.

## Verification and latest exports

The full local suite passes **424 tests**. Lint, formatting and production build pass. Chromium Canvas/WebGL and Firefox Canvas pass every owned hull's sea-save reload identity/pixel checks, page reopen, art switching, buyer selection, equipment persistence, timed dumping, surface speech/readiness and phone deck-menu access. Runtime screenshots are inspected. [Detailed acceptance and limits](docs/history/2026-09-23-working-day/README.md).

The synthetic-controller journey passes remapping, bag/boarding actions, range pause, restart, held-input gating, disconnect and launcher exit. Normal and seven-vessel Canvas scenes pass the existing software frame/CPU budgets; the saved day-17 career runs through live tide updates and two autosaves without page errors. The standalone public checkout passes lint/format, **423 tests with one excluded private-save check skipped**, and build; all **174 compiled game files** match the authoring build byte-for-byte. Physical device behavior remains unverified by these checks.

Release identity: **TEMP · SEP 23 · WORKING DAY**.

- [itch.io TEMP ZIP](exports/2026-09-23-working-day/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-23-working-day/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-23-working-day/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.
- Previous exports remain in `exports/2026-09-23-touch-and-portrait/` and older dated folders. TEMP ZIPs stay local for the designer's itch upload.

Exports exclude player profiles and retain identical compiled game bytes. Preserve older exports; do not recreate deleted checkpoints. [Data preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): reopen actual itch/Android sessions, compare neutral hull handling, inspect full deck loads and lights, fish buyer targets, dump poor samples, revisit chart marks, and observe taxi/rival pressure. USB Xbox remains the known-good physical input baseline; automated gamepads do not establish physical controller behavior. Built-in Deck, actual phone/tablet rotation, speakers/headphones, crowded night/fog sessions and sustained device FPS still need hands-on checks.

Long-season market/crew balance and full-Bible compliance remain unfinished. The economic sensitivity harness passes its existing thresholds using explicitly selected orders; it does not establish real player progression. [Failure notes](docs/FAILURE_NOTES.md) retain significant causes and successful alternatives.
