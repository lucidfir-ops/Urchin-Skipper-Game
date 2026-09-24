# Urchin Skipper — current status
Updated 2026-09-24 · Latest game: automatic embedded rotation recovery, clearer neutral rudder response and gentler bow thrust; crew/coasts update preserved.

Read this first, then task-relevant source/tests/references. The [living Bible](bible.md) is the approved design authority. [Previous status](docs/history/2026-09-24-rotation-and-helm/before/PROJECT_STATUS.md) preserves the crew/coasts handoff.

## GitHub backup and release workflow

Standing instruction: after each completed, verified game update, synchronize the selected source/assets into `.github-backup/checkout/`, verify there, and commit/push to [lucidfir-ops/Urchin-Skipper-Game](https://github.com/lucidfir-ops/Urchin-Skipper-Game), branch `main`. Create new dated local TEMP itch.io and local/Wi-Fi exports. Preserve older exports and report any upload failure. [Full policy](AGENTS.md#github-backup-and-temp-exports).

Use the separate minimal repository, never the full workspace's large older import history. Include new required source/assets; retain the checkout's stricter ignore rules. Ordinary clones can use their own `main`. Dependencies, caches, exports, player data, credentials and unrelated history stay excluded. [Exact publication, selection and verification receipts](docs/github-backup-review/README.md) are local authoring records. GitHub CLI/credential helper is configured at `.runtime/github-cli/2.101.0/bin/gh` as `lucidfir-ops`.

## Design authority

[bible.md](bible.md) is the single living specification. September 23 consolidation permanently fixes two working diver berths, confirms **Shy Hull Wood** and retains the approved Settings reference within reason. The subsequent crew/coasts request explicitly authorizes the changes now recorded in relevant Bible sections; [provenance](docs/DESIGN_CONSOLIDATION.md#september-23-crew-and-coasts-follow-up). The subsequently approved video omissions are incorporated in §§5 and 19; [video-follow-up provenance](docs/DESIGN_CONSOLIDATION.md#september-24-video-follow-up). Numerical fatigue/weather/handling tuning is an implementation choice. The [longer crew/relationship document](docs/CREW_RELATIONSHIPS_PROPOSAL.txt) remains a proposal beyond approved speech behavior.

The [former DOCX and retrieval mirror](archive/design/2026-09-23/README.md) and [approved reference images](docs/reference/bible/README.md) remain intact. [Source mapping](docs/DESIGN_CONSOLIDATION.md). Preserve the orthographic camera, harbour reference and separation of decoration from simulation geometry. Historical amendments, tests and implementation notes do not override the Bible.

## Current implementation

- Embedded touch play requests any orientation where supported and automatically claims child fullscreen permission on a normal touch when the host already owns fullscreen. Successful orientation requests survive resizes; context changes retry safely. Inline/mouse play and intentional fullscreen exits are preserved. Physical Android/itch rotation remains a hands-on check.
- Near-neutral shaft rudders now answer light water-relative flow visibly on loaded boats, with no invented force at matched drift. Powered handling stays unchanged. Shared factory/retrofit bow-thruster force is reduced by 20%, retaining useful docking authority and speed fade. General reverse/wind tuning and starter weather limits are preserved.
- Bag and boarding actions choose the nearby eligible diver regardless of portrait selection, and pin any active deck operation. One bag press lands catch and sends that person back down with a fresh bag if eligible. Selection still controls intentional deployment, scouting and individual orders.
- Bubbles explain low air, exhausted ground, failed quality/bag-time orders and other refused descents. Local rejected samples can be reported on unmarked ground without exposing distant beds. Unchanged reports stay quiet across repeated surfacings/reloads; crew personalities vary casual chatter. Direct refused requests always get an answer. Adjacent reports are spaced apart.
- Orders now include a maximum bag time, counting picking separately from scouting. Slow bags surface partial; quality and rate reports use actual observations. Individual orders persist through days, berth changes and reload. Narrow phone Orders use one scrolling column.
- Taxis commit to straight navigable passes and continue toward an exit, sometimes crossing worked ground. They avoid turning back toward passed waypoints. Moving surface impacts injure; fast overruns can kill. Underwater divers remain safe. Existing rival stock competition, traffic participation and rare-event cadence remain.
- Fatigue builds faster while working and recovers by 60 percentage points overnight: ordinary work is mostly recovered by morning; exhaustion still carries some cost. Nitrogen exposure stays separate. Home Coast gusts/current/waves cap at 8 knots / 0.6 knots / 0.8 m with local shelter retained; later coasts keep progressively severe storms. Forecasts and Frank explain the difference.
- Falling water can leave a hull seated on a shoal. Wait on the water for flotation or request the existing paid radio rescue ($350 commercial tow/handling). Menus pause time. Original coast geography, generated beds and stock identities are unchanged. No sinking system or weather departure ban was added.
- Prior working-day features remain: neutral hull/current handling, loaded inertia, layered deck bags, timed dumping, buyer contracts, individual earnings, witnessed chart marks, trip highlights, equipment switches and working lights. Saved hull identity/upload fixes and +50% default pace remain. [Previous implementation](docs/WORKING_DAY_2026-09-23.md).
- Touchscreen Options, saved portrait/landscape layouts, orientation recovery, reduced audio scheduling, prepared artwork, validated saves and prior device fixes remain. [Previous device acceptance](docs/history/2026-09-23-touch-and-portrait/README.md). Asset bytes/runtime paths remain preserved by the [canonical asset layout](docs/ASSET_LAYOUT.md). [Player guide](HOW_TO_PLAY.txt).

## Verification and latest exports

The full local suite passes **446 tests**; lint, formatting and production build pass. The standalone public checkout passes **445 tests and one intentional private-save skip**; all **174 compiled files** match. New regressions cover light-flow rudder response, both helm signs, no-flow/no-jet behavior, unchanged powered steering, reduced useful thrust and orientation permission/race handling. Existing crew/coasts, starter-weather reverse, grounded rescue and save checks pass. [Detailed acceptance](docs/history/2026-09-24-rotation-and-helm/README.md).

Chromium and Firefox pass real cross-origin fullscreen/touch checks with simulated mobile orientation permissions, deliberate exit, ordinary inline/mouse use, four training replays and log download. Portrait/landscape runtime screenshots are inspected. Headless Firefox uses a fixed fullscreen display, so its phone layouts are checked outside fullscreen. The synthetic controller journey passes remapping, bag/boarding, range pause, restart, held-input gating, disconnect and launcher exit. These checks do not establish physical sensor/controller behavior. [Prior crew/coasts browser and performance evidence](docs/history/2026-09-24-crew-and-coasts/README.md), [backup receipts](docs/github-backup-review/README.md).

Release identity: **TEMP · SEP 24 · ROTATION & HELM**.

- [itch.io TEMP ZIP](exports/2026-09-24-rotation-and-helm/UrchinSkipper-TEMP-ITCHIO.zip) · [upload instructions](exports/2026-09-24-rotation-and-helm/START-HERE-ITCH-IO.txt).
- [Local/Wi-Fi TEMP ZIP](<exports/2026-09-24-rotation-and-helm/Urchin Skipper TEMP.zip>) contains identical game bytes and desktop/LAN launch helpers.
- Previous exports remain in `exports/2026-09-24-crew-and-coasts/`, `exports/2026-09-23-working-day/` and older dated folders. TEMP ZIPs stay local for the designer's itch upload.

Exports exclude player profiles and retain identical compiled game bytes. Preserve older exports; do not recreate deleted checkpoints. [Data preservation policy](data/README.md#september-16-preservation-amendment).

## Outstanding playtesting

Follow [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md): check Android/Firefox rotation after ordinary host launch, loaded light-current helm and gentler bow thrust. Continue to work both nearby divers without portrait changes, scout unmarked ground with strict orders, compare early/late-day fatigue and next-morning recovery, observe taxi passes, and test starter storms plus a falling-tide stranding. USB Xbox remains the known-good physical input baseline; automated gamepads do not establish physical controller behavior. Actual itch/Android sessions, built-in Deck, phone/tablet rotation, speakers/headphones, crowded night/fog scenes and sustained device FPS still need hands-on checks.

Long-season market/crew balance and full-Bible compliance remain unfinished. The economic sensitivity harness passes its existing thresholds using explicitly selected orders; it does not establish real player progression. [Failure notes](docs/FAILURE_NOTES.md) retain significant causes and successful alternatives.
