# What the automated checks mean

The count in `PROJECT_STATUS.md` is the latest completed test run, not a claim that every gameplay situation is covered. A test is a repeatable example or invariant: it catches accidental changes to behavior we intend to preserve. Several tests exercise multiple boats, sectors or situations; many possible experiences still need a person at the helm.

Latest September 15 feedback acceptance: 285 tests plus lint/format/build; [current reports, screenshots and build fingerprint](history/2026-09-15-feedback/acceptance/README.md). The previous [273-test touch milestone](history/2026-09-14-touch-feedback/acceptance/README.md) and [263-test v2 milestone](history/2026-09-14-v2/acceptance/README.md) remain preserved. Reports are not reused as proof of a different build. Remaining hardware and long-duration checks are below.

| Broad coverage | Why it exists |
| --- | --- |
| Boat acceleration, latched throttle/rudder, reverse, water-relative speed, local drift, grounding leverage, propulsion differences and shallow access | Preserve the designer-confirmed handling while changing nearby systems. |
| Spatial/current sampling, separate current/tide timing, forecast nonmutation, depth/shore exposure, generated sectors and habitat fields | Keep planning, physics and rendering tied to one environmental state; catch data and coordinate mistakes. |
| Diver orders, local search and clump depletion, stock conservation, air, bag timing and partner dispersion | Prevent duplicated catch, premature exhaustion and stationary or shared-path harvesting regressions. Quality rules are checked mechanically, not endorsed as fun or realistic. |
| Nearest eligible port pickup, paused progress, explicit bag/descent/boarding choices, capacity overflow and tank refill | Keep physical boat positioning authoritative and prevent stranded crew or duplicate bags. |
| Hull versus stern-drive contact, low-speed timber nudging, severity/speed damage, surface-diver injury/fatality and rescue accounting | Make consequences consistent, preserve injured/deceased outcomes and prevent rescue or refitting from bypassing them. |
| Physical harbour exit, deadlines, delayed shipping, water/quality loss and expenses | Ensure the day's payoff is calculated once and late arrival has the intended economic effect. |
| Input ownership, saved per-device mappings, raw-layout guardrails, release gates, remapping, audio and launcher exit | Catch stuck controls, cross-device map drift and broken startup/exit flows. |
| Seeded rival rosters, balanced growth, loyalty/transfers, shared-stock physical fishing, water routes, taxi collision/bubble behavior, DFO alongside boarding/schedule and save continuation | Exercise bounded other-boat behavior without silently double-counting catches or resetting crews. |
| Persistent dive exposure, surface intervals, consecutive days, hidden adherence, DCS medical return and guarded training controls | Ensure fresh tanks/saves/hires cannot erase risk; distinguish game balance from medical accuracy, and keep training separate from real saves. |

Browser smoke checks additionally launch **the actual Phaser game** with keyboard and synthetic gamepad input. They navigate menus, recover catches, inspect privacy/layout, exercise timed/fixture collision outcomes, and capture screenshots for visual review. Long dives and exact deadlines use explicitly identified time jumps; collision cases use explicit obstacle/crew placement. Those are integration checks, not an autonomous naturalistic playtest.

## Still requires playtesting

- Physical Xbox and built-in Steam Deck behavior, desktop paddles/shortcuts, Bluetooth reconnect and device switching. A synthetic browser pad cannot test Steam/KDE routing.
- Handling feel, low-ahead current matching, fair collision thresholds, log readability, medical/rescue clarity and the extra post-bag choice under pressure.
- Diver QA/audit judgment, natural path choices and air/workload balance across varied drops and conditions.
- Visual readability, sound, comfort and sustained FPS on the real Deck/tablet. Screenshots and brief browser runs are not long-duration performance evidence.
- Real-world habitat, tide/current accuracy, economy, longer NPC interactions and exposure calibration. The game's data and coefficients are deliberately synthetic/provisional; its dive model is not medical guidance.

## Reproduce

`npm run verify` runs lint, formatting, simulation/input/launcher tests, the production build, and sequential browser/controller checks. It starts or reuses the production test server on port 5180 and uses isolated browser contexts. The normal launcher serves the same build on port 5173, preserving the existing save origin.

```sh
npm run verify -- --unit-only
npm run verify -- --browsers-only --suite=iteration
npm run verify -- --browsers-only --suite=firefox
npm run verify -- --browsers-only --suite=career
npm run verify -- --browsers-only --suite=feedback
npm run verify -- --browsers-only --suite=overnight
npm run verify -- --browsers-only --suite=rendered
npm run verify -- --browsers-only --suite=controller
npm run verify -- --browsers-only --suite=v2
npm run verify -- --browsers-only --suite=vessels
npm run verify -- --browsers-only --suite=traffic
npm run verify -- --browsers-only --suite=training
npm run verify -- --browsers-only --suite=training-firefox
npm run verify -- --browsers-only --suite=performance
npm run verify -- --browsers-only --suite=performance-firefox
npm run verify -- --browsers-only --suite=touch-feedback
npm run verify -- --browsers-only --suite=touch-feedback-firefox
npm run verify -- --browsers-only --suite=september15
npm run verify -- --browsers-only --suite=september15-firefox
```

The touch-feedback suite taps the title/harbour/arcade/boat comparison/sail/order/pause/settings flow at phone sizes; Chromium additionally sends two simultaneous browser touch contacts and verifies release/cancellation. Explicit flat-water, boat placement and exposure fixtures check hidden labels, reveal/current/nitrogen screenshots and actual DFO approach/boarding. These fixtures are distinct from the natural working-voyage regression. No physical mobile device or Safari run is implied.

The September 15 suite uses real mapped controller presses to scroll all three sail-plan panes, resolve the harbour Test Mode crew case, acknowledge/invite DFO, complete shallow docking and operate independent twin-jet pivot/bow-thruster axes. `scripts/verify-september15.js` runs the broader two-engine acceptance sequentially against an already running production server. Its optional `--resume` retains passed stages only for the same bundle. The browser voyage uses the unit voyage's fixed career seed, with natural evolving weather, harvest, helm and settlement.

The rendered suite includes the original prototype day and all-area environment checks; those can also be selected individually as `prototype` and `environment`. `npm test` and `npm run build` remain available separately. `npm start` serves an already-built game; `npm run dev` remains the development server. Freeze source/helper edits during browser runs and run substantial browser suites sequentially.

Reports and screenshots live in disposable `test-results/`. The final successful suite reports supersede failed exploratory runs; do not treat a stale aggregate report as evidence of the current build. Runner sandbox limitations and known failure causes are in [failure notes](FAILURE_NOTES.md). Restoration checks validate archive contents and hashes separately from gameplay tests.

## Latest playtest regressions

`tests/latest-fixes.test.js` covers neutral-only differential thrust, diagonal-stick isolation, preserved momentum, .9/1.1 m jet contact/refloat at multiple speeds, 2/3/5 kn searching-diver holding/slip, braced harvesting with conserved stock, 3–5 kn channel peaks, exact forecast/live agreement and cliff/beach coexistence. The second video's working-diver instruction supersedes the earlier swept-off-while-picking expectation. The feedback browser command also runs `scripts/latest-checks.js` with a pad present before page initialization at sparse index 2, then checks the actual HUD, almanac, helm and compact Session Ended / B flow. `deck-smoke.js` covers Retry, Launcher/title, cancellation and actual authenticated companion exit.

- v1.7 coast/equipment slice: 153 named automated tests passed; build passed. Extended `--career-only` controller flow covers early start, weather outlook, saved assists, chartplotter/marks, radar/scanner, and fog/low-light rendering at 1024×640. Screenshots reviewed. Original prototype regression tests remain in the same suite.

## v1.7 integrated first pass — 2026-09-11

- 161 named automated tests pass, including career accounting, live save/reference restoration, additive archives, late-shipping departure limits, crew/hull differences, weather/current agreement, equipment observations, stable crew reports, rival stock conservation, sorting, inspection idempotence, rough-water events and multi-day persistence. Production build passes; the existing Phaser bundle-size advisory remains.
- `--career-only` passes the controller harbour/hiring/equipment/forecast/assists/chart/recovery/offload flow, next-day Back, save/reload, DFO boarding, Exit/B/Launcher, fresh career/archived career and export. Import is checked through the browser's file picker. The exported JSON independently decodes and retains crew, money and chart marks.
- The same command runs a complete rendered career voyage using real helm and physics, an unchanged spatial tide/current/weather state, autonomous search and a natural full bag, maneuvered recovery, physical return and actual offload. The final run landed 300 lb on time with hull at 100%, both crew fit and a positive working return. This is a scenario check, not a claim of optimal piloting or final economy balance.
- Title, original SVG/PNG library art, shoreline-shaped grounds, kelp, night/fog, equipment, DFO, recorded charts, fleet reports and harbour receipts were inspected at 1280×800 and/or 1024×640.
- Original v1.6/v1.7 design sources, Easter egg PDF, source/distribution workboat images and the dependency lockfile match the pre-fix checkpoint hashes (eight files). No dependency or original-art replacement was used.
- Final preserved-baseline regressions pass: default browser suite (keyboard fishing, complete two-diver prototype day and all three coastal areas), feedback/startup suite (including a preconnected sparse-index Xbox), overnight/boatyard/forecast/rescue suite, and isolated controller remapping/recovery/hotplug/Back/Retry/Launcher/authenticated Exit. These runs reported no page errors. Final source/build checkpoint label: `v17-full-game-first-pass-verified`, with restoration and hash checks.

Physical Xbox/Deck Game Mode input and sustained hardware FPS/audio still need an actual device playtest. Synthetic preconnected pads, reconnects, keyboard emulation and controller menu checks establish software routing only. Browser profiles containing career data must be retained separately from source checkpoints; use exported JSON copies as additional protection.


## Video / transcript pass — 2026-09-11

Final run: **175 named tests pass**, production build passes (existing Phaser chunk-size advisory). New coverage and fault mapping: [feedback implementation](FEEDBACK_IMPLEMENTATION.md#verification--complete).

All of these commands passed during the pass, with focused reruns after fixes:

- `npm test`, `npm run build`.
- `browser-smoke.js --feedback-only`: preserved feedback/startup checks plus the recorded 33 L fuel budget, refuelling, responsive fuel-zero helm, rescue, Exit cancellation, actual rest/dock days, analogue forecast navigation and trigger scrubbing.
- `browser-smoke.js --career-only`: controller career, save/archive/import and a natural rendered working voyage. Substantial suites use fresh Chromium instances. The voyage reports a small real shore contact (~0.2% hull), both crew fit, 300 lb on time and positive operating return; it does not fabricate catch or disable the environment.
- `browser-smoke.js`: keyboard fishing, full two-diver prototype day, all three coastal areas and the existing visual/simulation privacy checks.
- `browser-smoke.js --overnight-only`: preserved boat/tide/night/rescue/clump checks plus compact equipment/crew/lesson/DFO/arrival panels. Right-stick reading and pointer scrolling are exercised.
- `deck-smoke.js`: isolated controller start, controls/remapping/cancel/reset, recovery, hotplug/release gates, Back/Retry/title and authenticated companion Exit. Synthetic input only.

The menu driver sends mapped gamepad buttons through the real DOM/input loop; it never assigns selection or invokes activation directly. Its path planning accounts for spatial layouts and scrolling. Significant failed attempts are retained in [failure notes](FAILURE_NOTES.md). Runtime screenshots in `test-results/` were inspected; they are disposable evidence. Human documents, original art, generated terrain recipe and dependency lockfile retain their original hashes.


## Second video iteration — September 11 playtest, verified September 12 UTC

**189 named automated tests pass**, including 14 new regressions in `tests/second-video.test.js`. Lint reports zero warnings, formatting passes and the production build succeeds. The existing Phaser bundle-size advisory remains. Detailed values and intentional supersessions are in [the second-video decisions](history/2026-09-11-second-video/DECISIONS.md).

The new checks cover:

- Cabin centre of pressure with unchanged total wind load; idle weathercocking and powered countersteering; downwind crest motion and rain direction.
- Harmless parallel hull brushes versus dangerous closing strikes, alongside the preserved injury, fatality, recovery and fuel-zero regressions. Searching still slips in strong flow; the latest braced-harvesting expectation intentionally replaces the old working-diver drift test.
- Licence-charge idempotence, ordered chart tracks, season-boundary survivor recruitment, opening windows and near-shore fallback.
- Additive hidden-shelf generation preserving original reef identities and seabed, actual contour interpolation, old actual fuel/tank migration and rejected invalid numeric save state.
- Workshop isolation from real saves, stable harbour action IDs and scroll-independent controller geometry with Back/boundary wrapping.

Verification uses the built game, including static-serving/launcher tests. Browser menu drivers send mapped inputs through the actual input/DOM loop; they do not invoke the selected service directly. Time jumps and exact-position/strong-weather fixtures are labelled integration checks. The separate natural voyage uses actual helm, untouched environmental progression, autonomous fishing, recovery and boundary offload: **300 lb on time, 100% hull, both crew fit and $41.22 positive operating return** in the rendered run. Its pure-simulation counterpart also passes. These scenarios do not establish final multi-season balance.

Protected-input verification compares 18 design, feedback, original-art and terrain inputs with the pre-edit archive. Every comparison matches, and both new source/distribution artwork pairs are identical. Original videos, audio, transcript, design documents, source terrain and player browser profiles remain intact. Checkpoint restoration separately verifies the archived project.


All of these production suites passed sequentially during this iteration, with affected flows rerun after fixes:

| Suite | Completed coverage |
| --- | --- |
| `iteration`, `firefox` | Chromium and Firefox preconnected/hotplug pads, title/wharf/B, berths, owned boats/shop, licence, Frank, workshop save isolation, rest/dock days, forecasts/departure, L3/R3, sea settings, Exit cancel/title; screenshots at 1280×800 and 1024×640. |
| `career` | Hiring/equipment, recovery/offload, next day, saved assists/electronics, chart knowledge, DFO, save/reload/archive/export/import and a separate natural rendered working voyage. |
| `feedback` | Earlier injury/grounding/recovery checks, sparse-index Xbox startup, current/forecast truth, neutral pivot, recorded low-fuel departure/refuelling, fuel-zero helm/rescue, long menus and rest/dock/forecast controls. |
| `overnight` | Boat packages, keyboard thruster, tides/forecast, Realistic information limits, local clump work, rescue, compact equipment/crew/Frank/DFO/arrival panels, right-stick reading and pointer scrolling. |
| `rendered` | Keyboard fishing, full two-diver prototype day, compass actions, independent bags, audio events, recovery, actual harbour exit, exact/deferred shipping, all three coastal areas and compact layouts. |
| `controller` | Isolated start, throttle/rudder latch, remapping/cancel/reset, release gates, range-paused recovery, hotplug, Back/Retry/Launcher and authenticated companion Exit. |

The retained [verification record](history/2026-09-11-second-video/VERIFICATION.json) contains the successful run timestamps, protected-input comparisons and drawing samples. Exploratory full-run and fixture failures are recorded in [failure notes](FAILURE_NOTES.md); their stale disposable reports are not final acceptance results. No source/helper edits occurred during these browser runs.

The Firefox drawing sample uses 120 frames at each cadence, fully zoomed out: mean drawing 9.025 ms at 60 surface rebuilds/s versus 6.125 ms at 15; mean headless frame interval 34.78 versus 31.50 ms. This is a current-renderer cadence comparison. It does not establish physical Deck FPS or whole-build speedup; Chromium software rendering remained much slower outside the draw function. Physical Steam Game Mode startup/hotplug, sustained hardware FPS/audio and ordinary multi-season balance remain explicit playtest limits.


## September 12 feedback and technical cleanup

**201 named automated tests pass**, including eleven September 12 regressions and one saved input-profile migration regression. Lint has zero warnings, formatting passes and the production build succeeds (74 transformed modules; JavaScript 2,907.85 kB / 853.66 kB gzip, CSS 32.77 kB / 8.20 kB gzip). The existing chunk-size advisory remains; this pass does not claim improved physical Deck FPS. The source import graph remains acyclic.

[Decisions and reproductions](history/2026-09-12-feedback/DECISIONS.md) distinguish proven faults from unconfirmed observations. The new tests cover exhausted-search reuse after boarding, empty bags and independent air, partial deck bags, matched two-knot relative pickup and hull exclusion, immediate chart sampling, one-time starter purchase and old-save preservation, compass arrival labels, stable expedition actions, persistent crew progression, actual/escaped SVG landing data and per-hull Frank advice. Channel Master coverage includes a completed recovery outside the passive 12 m chart-observation radius, with that observation limit preserved for ordinary sampling. The old over-capacity fixture uses an actual Island Tender and confirms all 4,200 lb remain after restore. The existing 33 L passage expectation intentionally changes with the designer's 15 L/h Workhorse tuning.

The `september12` and `september12-firefox` suites navigate the production game using mapped synthetic controller actions. They exercise the funded starter, real ownership/balance text, Frank and crew display, downloaded yellow SVG, early-start consequence, forecast triggers without clock advance, controller setup, compass arrival, RB information toggles, chart reports, and the board/move/fresh-dive sequence. Exact state placement and accelerated stepping in the last sequence are explicit integration fixtures. The new chart checks assert a 50% preview enlargement, clock separation, panel containment and unchanged neighbour rectangles at 1280×800, 1152×720 and 1024×640. Crew levels must fit within the visible detail panel without scrolling. Runtime screenshots are reviewed as well as geometry assertions.

The first full run passed lint/format/unit/build, both new browser flows, existing Chromium/Firefox iteration flows, career/save/archive/import, natural voyage, feedback/fuel/rescue, and overnight/compact panels. Its rendered prototype flow caught a test-driver timing race: ArrowLeft was released before Confirm had necessarily been consumed. Waiting for the instruction screen to close before releasing the arrow preserves the game's existing centre-to-clear compass behavior. The corrected full rendered suite passes, including keyboard fishing, the two-diver prototype, exact/late offload, all three sectors, environment and compact layouts. The final crew-label adjustment is validated by the affected screen suites; it does not alter simulation or controller mapping. Completion records are retained in the September 12 verification record and summarized in `PROJECT_STATUS.md`.

The natural rendered voyage lands **300 lb on time, with both crew fit, 100% hull and $97.02 positive operating return**. Its pure-simulation counterpart also passes ($95.37). These are actual helm/autonomous harvesting/recovery/boundary-offload flows with test acceleration, not physical-controller or final economy evidence.

Thirty-seven original feedback, design, art, terrain and dependency-lock inputs match the pre-edit checkpoint. Browser checks use isolated profiles and never the player's live Firefox profile. Raw media, transcripts, source artwork and older checkpoints remain. Physical Xbox/Deck X/Y and cold-start/hotplug, handling feel, sustained hardware performance, and longer crew/fleet/economy balance remain human playtests.

All nine production suite families now have passing results: September 12 Chromium/Firefox, iteration Chromium/Firefox, career/voyage, feedback, overnight, rendered and controller/launcher. This is a sequential full attempt plus affected-suite reruns, not a claim that the initial interrupted full run passed. The [retained acceptance record](history/2026-09-12-feedback/VERIFICATION.json) contains successful run timestamps, the original failed attempt, final source/build hashes and all 37 protected-input comparisons. Final range-fix verification includes the full unit/build pass, both new browser flows and controller/launcher. Source/helper edits stayed frozen during each browser suite.

## September 13 coverage

`npm run verify -- --suite=september13` runs unit/build checks followed by production controller navigation for title/load/new Test Mode, full-screen harbour, Alt-Tab menu preservation, saved arrival, reference diagrams/dropdown conflict, Easy/Realistic widget visibility, custom RB round trip, timed orders and restoration of the real career. `--suite=september13-firefox` covers Firefox. Both are included in the sequential full runner.

`tests/september13.test.js` covers independent Test Mode data, saved custom assists and per-area approach, timed varied searches, specialized progression and increased tank restoration, mixed-quality selection/harvest conservation, actual ground reporting, day-before buyer premiums, delayed runoff and once-only/exempt early-drive risk. Existing tests retain natural voyages, safety, capacity, old saves and input capture/reconnect coverage. No synthetic pad establishes the physical Xbox/Deck mapping or sustained hardware performance.

Final September 13 acceptance: **219 automated tests**, lint, formatting and production build pass. All eleven production browser/controller suite families pass across the sequential full attempt and affected-suite reruns. The final radio/title changes have new focused regressions and rendered/controller/September 13 UI reruns in both engines. Source/helper edits stayed frozen during each browser run. Fifty-four protected inputs match the pre-edit checkpoint; 72 source modules have no import cycle. The natural career voyage landed 300 lb on time, with 100% hull, both crew fit and $97.02 operating return. Screenshots at full and compact sizes were inspected. See the [retained acceptance record](history/2026-09-13-feedback/VERIFICATION.json) for attempts, source/build hashes, timings and limits.
