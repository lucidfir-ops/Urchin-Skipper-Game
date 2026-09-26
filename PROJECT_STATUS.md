# Urchin Skipper — current status
Updated 2026-09-25 · Latest game: safe confirmations, richer unmarked coasts, continuous taxi passes, environmental cues and development tools.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) is the approved design authority. [Previous status](docs/history/2026-09-25-coasts-and-safety/before/PROJECT_STATUS.md) preserves the coasting/traffic handoff and earlier changes.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, synchronize selected source/assets into `.github-backup/checkout/`, verify there, and commit/push to [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. Create new dated local TEMP itch.io and local/Wi-Fi exports. Preserve older exports and report any upload failure. [Full policy](AGENTS.md#github-backup-and-temp-exports).

Use the separate minimal repository, never the full workspace's large older import history. Include new required source/assets; retain the checkout's stricter ignore rules. Ordinary clones can use their own `main`. Dependencies, caches, exports, player data, credentials and unrelated history stay excluded. [Publication, selection and verification receipts](docs/github-backup-review/README.md) stay local. GitHub CLI/credential helper: `.runtime/github-cli/2.101.0/bin/gh`, account `lucidfir-ops`.

## Design authority

[bible.md](bible.md) is the single living specification, permanently fixing two working diver berths. September 25 supersedes late-coast quality/mark tuning, taxi crossing probability and the development credit cap; explicitly preserves Maelstrom weather, Knifepoint current and existing nearby-rival interaction. Live Godmode is an approved development exception, off by default. [Request/media provenance](docs/DESIGN_CONSOLIDATION.md#september-25-coasts-and-safety). The longer crew/relationship document remains a proposal beyond approved speech behavior.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) and [approved reference images](docs/reference/bible/README.md) remain intact. Preserve the orthographic camera, harbour reference and separation of decoration from simulation geometry. Implementation and tests do not establish full-Bible compliance.

## Current implementation

- Unfit-crew departure and Sleep/Rest/Dock work require an “Are you sure?” menu, initially on Cancel. Existing crew eligibility remains; confirmation never makes an unfit diver able to work.
- All fifteen maps have 65 beds; marks per coast are 13/5/4/3/2, with the remainder unmarked. Starter footprints/marks and all existing bed identities, stocks and depletion are preserved. Later shortfalls gain contour-following hidden infill. Quality bands, including clumps, are 60–85 / 65–90 / 70–95 / 80–100 / 90–100%. Old catches and dated reports retain their values.
- Home aggregate fishing pressure rises without more nearby boats. One/two physical rival visits, roughly 40% nearby-day eligibility and 2% rare-team eligibility are unchanged. Taxis prioritize safely routable straight passages through sampled active bubbles, never home on moving divers, and bend around hulls with forward motion. Actual terrain/hull obstructions retain safety checks.
- Fatal surface strikes from any vessel leave a large red pool; lesser injuries leave small stains. Grounding silt, damaged-boat sheen and rough-water spray describe existing state only. Factory/retrofit bow thrust is another 20.5% gentler; twin-jet pivot, neutral/current steering and stopping momentum are unchanged.
- Water current arrows have a separate saved switch from the dashboard instrument: Easy on, Realistic off, independent of coast. Permit purchases open a conspicuous receipt with Frank’s lost-fishermen tale, explicit upgrade advice and boatyard/planning links, never an upgrade gate.
- Accounts permits repeated $5,000 development loans, with ordinary debt/interest. Pause → Debug mode → Godmode prevents new damage/injuries and fuel expenditure, saves its choice and shows a banner. Existing losses, weather/current, collision geometry and dive readiness remain.
- Earlier coasting, sparse rivals, keyboard fills/menu/almanac, deployment/recovery, UI layouts, crew orders/fatigue, grounding/rescue, markets, artwork and USB Xbox mappings remain. [Previous implementation](docs/history/2026-09-25-coasts-and-safety/before/PROJECT_STATUS.md), [player guide](HOW_TO_PLAY.txt).

## Verification and latest exports

Authoring lint, formatting, **473 tests** and production build pass. The selected public checkout passes **472 tests plus one intentional private-save skip**, lint/format/build. All **174 compiled files** match authoring/public/local export; both ZIPs pass CRC/hash verification. New regressions cover coast quality/counts, depleted-save migration, confirmations, permits, borrowing, independent arrows, taxi avoidance/bubble commitment, fatal strikes and saved/cross-day Godmode. Chromium/Firefox menus, keyboard Cancel, portrait/touch receipt/rescue and save/reload checks pass; synthetic controller flows pass. Runtime visuals are inspected, including the fatal pool with the normal compact emergency menu. Canvas ordinary/seven-vessel scenes pass existing software budgets; forced software WebGL remains slow. The natural helm-driven voyage returns 300 lb on time, with fit crew, 100% hull and $101.31 net. [Evidence and limits](docs/history/2026-09-25-coasts-and-safety/README.md).

Release identity: **TEMP · SEP 25 · COASTS & SAFETY**.

- [itch.io TEMP ZIP](exports/2026-09-25-coasts-and-safety-release/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-25-coasts-and-safety-release/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-25-coasts-and-safety-release/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers. Earlier preflight ZIPs are preserved; use this `-release` pair.
- Older exports, raw recordings, careers and the design archive remain intact. TEMP ZIPs stay local for the designer's itch upload. Exports exclude player profiles; do not recreate deleted checkpoints. [Preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): confirmations on keyboard/controller/touch; late-coast unmarked exploration and sample quality; Home depletion over multiple days; taxi avoidance and prompt surface recovery; current-arrow independence; permit warnings; repeated loans/Godmode; bow-thruster feel and cues. Test Maelstrom in a stronger purchased boat. Synthetic controller tests do not establish physical USB/Deck behavior.

Physical tablet FPS, the previously recorded blank first departure and phone automatic rotation remain unresolved device acceptance items. The blank scene has not been reproduced or diagnosed; use the troubleshooting log during a device replay. [Tablet details/profiling route](docs/PERFORMANCE.md#september-24-tablet-recording). Continue night/fog, storms, falling-tide rescue and long-season economy checks. Full-Bible compliance and long-season balance remain unfinished. [Failure notes](docs/FAILURE_NOTES.md).
