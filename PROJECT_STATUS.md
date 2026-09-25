# Urchin Skipper — current status
Updated 2026-09-24 · Latest game: gentler coasting, sparse working rivals, committed taxi passages and keyboard feedback.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) is the approved design authority. [Previous status](docs/history/2026-09-24-traffic-and-coasting/before/PROJECT_STATUS.md) preserves the deployment/tablet handoff and earlier changes.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, synchronize selected source/assets into `.github-backup/checkout/`, verify there, and commit/push to [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. Create new dated local TEMP itch.io and local/Wi-Fi exports. Preserve older exports and report any upload failure. [Full policy](AGENTS.md#github-backup-and-temp-exports).

Use the separate minimal repository, never the full workspace's large older import history. Include new required source/assets; retain the checkout's stricter ignore rules. Ordinary clones can use their own `main`. Dependencies, caches, exports, player data, credentials and unrelated history stay excluded. [Publication, selection and verification receipts](docs/github-backup-review/README.md) stay local. GitHub CLI/credential helper: `.runtime/github-cli/2.101.0/bin/gh`, account `lucidfir-ops`.

## Design authority

[bible.md](bible.md) is the single living specification, permanently fixing two working diver berths. The newest keyboard/video decisions supersede frequent local rival crowding and excessive full-speed neutral yaw; they retain low-current rudder response, Shy Hull Wood's identity and earlier confirmed gameplay. [Request/media provenance](docs/DESIGN_CONSOLIDATION.md#september-24-keyboard-follow-up). The longer crew/relationship document remains a proposal beyond approved speech behavior.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) and [approved reference images](docs/reference/bible/README.md) remain intact. Preserve the orthographic camera, harbour reference and separation of decoration from simulation geometry. Implementation and tests do not establish full-Bible compliance.

## Current implementation

- Full-speed/full-helm neutral now gives a small coasting arc. Five-second empty/loaded shaft diagnostics fall from 81–101° to 6–8°. Low-flow current/rudder response, powered control, no-flow rule, thrusters and stopping momentum retain regressions.
- Ordinary rival visits are capped at one or two per seeded day across sector changes/reloads. They prefer marked productive beds, approach full-hull safe berths with low-water clearance, stop with working divers/bags, remove shared stock, then move on or leave. One nearby opportunity is allowed on roughly 40% of days. Existing saved visitors are preserved and count against the limit. Shy Hull Wood is eligible on only 2% of days.
- Taxis choose long committed routes between distant map edges; a tunable 30% opportunity may cross an active working area. Existing taxi cadence, hull avoidance and surfaced-diver collision consequences remain. Route samples now catch narrow shoals; slower turns and bounded recovery avoid circling.
- Keyboard throttle/rudder keys retain command-level fills after release. A clickable central Menu key removes the floating button overlap. **Tide & current almanac button** is explicitly named in Arrange UI, with independent saved visibility. Chart-only remains the fresh default; chosen layouts/presentations persist.
- Gentle surface contact separates the diver sideways without carrying their position along with the bow. Existing harmful-contact thresholds remain. Reverse audio uses softer steady engine/wash instead of the eerie modulated harmonic.
- Automatic aboard-diver deployment, hull-range recall, one-press recovery, default deck-load gauge, tablet rendering improvements, fullscreen wording, crew/quality orders, fatigue, regional conditions, grounding/rescue, buyer orders, red deck bags, careers, artwork and USB Xbox mappings remain. [Previous implementation](docs/history/2026-09-24-traffic-and-coasting/before/PROJECT_STATUS.md), [player guide](HOW_TO_PLAY.txt).

## Verification and latest exports

Authoring lint, formatting, **461 tests** and production build pass. The standalone selected public checkout passes **460 tests plus one intentional private-save skip**, lint/format/build; all **174 compiled files** match authoring and local export. New regressions cover 15 complete rival visits across three seeds/five sectors, changing-tide clearance, stock conservation, saved day limits/old routes, rare-day statistics, long taxi passages, both coasting helm signs and gentle swept contacts. Chromium/Firefox production keyboard/fishing journeys and synthetic controller flows pass; runtime screenshots are inspected. Isolated Canvas ordinary/seven-vessel benchmarks pass the existing software budgets; forced software WebGL remains slow. The natural voyage finishes on time with 100% hull and fit crew after the test pilot was taught to slow near visible timber; damage rules and test thresholds remain. [Evidence and limits](docs/history/2026-09-24-traffic-and-coasting/README.md).

Release identity: **TEMP · SEP 24 · COASTING & TRAFFIC**.

- [itch.io TEMP ZIP](exports/2026-09-24-traffic-and-coasting/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-24-traffic-and-coasting/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-24-traffic-and-coasting/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.
- Older exports, raw recordings, careers and the design archive remain intact. TEMP ZIPs stay local for the designer's itch upload. Exports exclude player profiles; do not recreate deleted checkpoints. [Preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): full-speed neutral with both helm signs and cargo; low-current steering; several full days of distant/nearby rivals and taxi interference; old saved traffic; keyboard fills/menu/almanac; gentle bow/diver contacts and reverse audio on actual speakers. Probabilities describe eligible opportunities, not guaranteed sightings. Synthetic controller tests do not establish physical USB/Deck behavior.

Physical tablet FPS, the previously recorded blank first departure and phone automatic rotation remain unresolved device acceptance items. The blank scene has not been reproduced or diagnosed; use the troubleshooting log during a device replay. [Tablet details/profiling route](docs/PERFORMANCE.md#september-24-tablet-recording). Continue night/fog, storms, falling-tide rescue and long-season economy checks. Full-Bible compliance and long-season balance remain unfinished. [Failure notes](docs/FAILURE_NOTES.md).
