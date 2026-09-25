# Development notes

Current design: [bible.md](bible.md). Build state: [PROJECT_STATUS.md](PROJECT_STATUS.md#design-authority). These notes describe implementation, not a separate design specification. [v1.7 development](docs/V17_DEVELOPMENT.md), earlier [prototype notes](docs/history/2026-09-11-v17/DEVELOPMENT_NOTES.md) and feedback records linked below are historical implementation evidence only. Dated references to authority or current decisions below describe that increment; approved current design is consolidated in the living Bible.

## September 24 rotation and helm

[Acceptance and limits](docs/history/2026-09-24-rotation-and-helm/README.md). `rotation-policy.js` deduplicates explicit `lock('any')`, caches success through ordinary resizes, retries on context changes and prevents stale failures from unlocking a newer context. `fullscreen.js` uses the next trusted touch to claim child fullscreen only inside an already-fullscreen host. Inline views, mouse play and deliberate exits keep their behavior. The embed checks model mobile orientation permission while exercising real cross-origin fullscreen/touch in Chromium and Firefox; physical phone rotation still needs a device check.

`water-loads.js` gives real low-speed longitudinal flow more readable rudder lift near neutral, fading by 8% throttle and in strong flow. It remains zero at matched drift and preserves shaft/leg/jet distinctions. Bow force is reduced 20% through the shared factory/retrofit specification. Run the rotation/helm unit tests and `npm run verify -- --browsers-only --suite=device-embed` (or `device-embed-firefox`).

## September 24 crew and coasts

[Implementation and acceptance](docs/history/2026-09-24-crew-and-coasts/README.md). One-command bag exchange uses the nearby diver; selection remains for deployment/orders. `crew-moments.js` keeps bounded per-diver report memory; `diver-observations.js` samples only local awareness; `maxBagSeconds` and the picking-only clock persist in saves. `regional-conditions.js` limits live Home Coast conditions and forecasts while habitat authoring keeps its original field. Taxi crossing routes commit once and look past reached waypoints. Deeply seated hulls wait for water or the existing paid rescue transition. Run `npm run verify -- --suite=crew-coasts` (or `crew-coasts-firefox`) and the synthetic controller flow.

## September 23 working day

[Implementation and limits](docs/WORKING_DAY_2026-09-23.md). `water-loads.js` distributes neutral hydrodynamic resistance and appendage lift; `equipment-controls.js` centralizes enabled gear; `deck-work.js` persists one timed discard job; `buyer.js` supplies seeded optional orders and contacts. The offload quote caps eligible premium and preserves crew attribution. `crew-moments.js`, `day-story.js` and dated chart reports only describe observed facts. New regression entry: `npm run verify -- --browsers-only --suite=working-day` (and `working-day-firefox`).

## September 22 preparation and performance

[Implementation and evidence](docs/history/2026-09-22-performance-and-device-fixes/README.md) follow the [designer amendment](docs/FEEDBACK_SEPTEMBER22.md). All fifteen sector grids remain eager static imports. `loading.js` gates play on required interface/vessel artwork and the current sector's first terrain paint. A sector change prepares its local raster before controls resume; it does not fetch another terrain dataset. Failed image loads offer Retry. `terrain-painter.worker.js` generates terrain materials and tide pixels using two transferred reusable buffers; blocked/timed-out workers use yielded row/pixel work on the main thread.

`background-save.js` posts one snapshot for worker serialization/checksum, then commits through the original protected backup/day-save policy. A manual save or world replacement cancels outstanding commits. Page-hide/manual saves remain synchronous. Paused unchanged worlds skip interval saves. Restricted storage failures still report without interrupting play.

`SurfaceCache` bakes water/debris/kelp commands at the existing 15 Hz only for Canvas; it draws the canvas directly without pixel readback. WebGL retains native animated geometry because repeated texture uploads regressed the measured software path. `CoastDetailCache` now also bakes close-view facets into a bounded 2048-square texture. Depth/collision geometry is unchanged. Shared sector grids are immutable; only per-career patches/clumps are cloned. Test fixtures that alter depth must first copy their grid.

Artwork recipe: `PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/prepare-runtime-art.js` prepares 69 small PNGs for 74 catalogue/mode entries under `public/assets/fleet-runtime/sep22/`, recording original hashes/framing in `src/generated/vessel-runtime.json`. Originals remain untouched and available. Aliases share a decoded canvas. Do not regenerate derivatives during normal build or play. Local delivery prepares Brotli/gzip text before readiness and uses ETags; itch supplies its own HTTP delivery.

## Runtime and state

The production server serves the game on loopback port 5173 by default; `npm start -- --lan` enables local-network phone/tablet testing. Vite is available for deliberate development. Phaser renders the rigid orthographic scene and supplies the existing Matter engine. `main.js` owns the active world. `simulation.js` advances one authoritative fixed-step state. The UI consumes abstract remappable actions and freezes simulation while a menu, focus or input gate is active. Rendering never owns stock, depth, current, crew or money.

| Responsibility | Source |
| --- | --- |
| World construction / terrain queries | `world.js`, `terrain.js`, `sectors.js`, `career-terrain.js` |
| Session replacement / career transitions / transient reset | `main.js`, `career-session.js`, `session-state.js` |
| Environment / planning | `environment.js`, `weather.js`, `almanac.js`, `day.js` |
| Hull motion / contacts / hazards | `boat.js`, `boats.js`, `hull-contact.js`, `collision-geometry.js`, `hazards.js`, `propulsion.js`, `diver-safety.js` |
| Diver autonomy / resource work / recovery queries | `simulation.js`, `diver-current.js`, `diver-recall.js`, `diver-escape.js`, `harvest-ground.js`, `hidden-ground.js`, `crew.js`, `diver-recovery.js` |
| Persistent people / fictional dive exposure / isolated training | `crew-roster.js`, `crew-skills.js`, `dive-exposure.js`, `training-tools.js`, `test-mode.js` |
| Career balance / business actions / saves | `career-data.js`, `career-state.js`, `career-save.js`, `starter-career.js` |
| Working fleet / fishery / physical traffic | `fleet-life.js`, `fishery.js`, `inspection-schedule.js`, `patrol.js`, `traffic.js`, `traffic-motion.js`, `water-route.js`, `sea-events.js` |
| Information and equipment observations | `assists.js`, `knowledge.js` |
| Input and shared menu behavior | `input.js`, `input-profiles.js`, `touch-controls.js`, `controller-view.js`, `menu-buttons.js`, `menu-navigation.js` |
| Shops / scenic harbour | `shop-actions.js`, `shop-view.js`, `harbour-view.js`, `harbour-shops.css` |
| Screens / HUD | `playtest-ui.js`, `screen-*`, `career-ui.js`, `career-chart.js`, `expedition-actions.js`, `day-view.js`, `almanac-view.js`, `hud-view.js`, `dom-view.js` |
| Geometry-bound chart / surface / vessel presentation | `terrain-view.js`, `ocean-view.js`, `coastal-art.js`, `coast-detail-cache.js`, `water-surface.js`, `chart-art.js`, `chart-material.js`, `vessel-art.js`, `traffic-view.js` |
| Weather / diver feedback / audio | `weather-view.js`, `presentation.js`, `crew-portrait.js`, `audio.js` |
| Shared arithmetic / formatting / complete-frame metrics | `math.js`, `format.js`, `frame-metrics.js`, `renderer-choice.js` |

`C` remains the prototype/mechanics baseline. Career hulls compose their dimensions/capabilities through `boatSpec`; simulation, collision, recovery and drawing use that same result. Career-only records remain conditional where the prototype's existing data shape matters. New saves carry a ground-recipe version so later world changes need not silently reinterpret old stock or diver references.

September 14 decisions: [v2 implementation ledger](docs/V2_IMPLEMENTATION.md). A world setter routes all replacements through one transient-state reset. Saves validate the previous envelope/schema without reconstructing it. Screen action lists are built once per render; hidden/unchanged HUD work is skipped. Shared seeded generator factories preserve the old sequences; the tight audio-sample loop and offload's one-shot scalar hash intentionally remain local. Rendering LOD/caches change decoration only. Original boat PNGs remain unchanged; runtime canvases are bounded. [Performance budgets](docs/PERFORMANCE.md) and [dive-model boundaries](docs/DIVE_EXPOSURE.md) document their separate limits.

The later [touchscreen and fishing amendment](docs/FEEDBACK_TOUCH_AND_DIVING.md) records v5 hidden-ground migration, seeded skill/schedule rules, dive calibration and the exact-source starter-art exception. Touch uses Pointer Events through the existing abstract input resolver. The boat-shop candidate changes on explicit selection, never during rendering or focus traversal.

## Local commands

```sh
npm test
npm run build
npm run dev -- --port 5173 --strictPort
PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/browser-smoke.js
PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/browser-smoke.js --career-only
PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/browser-smoke.js --feedback-only
PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/browser-smoke.js --overnight-only
PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/deck-smoke.js
python3 scripts/backup-project.py --label major-pass-verified --restore-check
```

The career browser harness includes controller navigation, real autonomous fishing, save/archive/export/import, and a complete voyage test using `scripts/voyage-pilot.js`. That pilot controls actual helm/physics and must not be mistaken for a player-facing autopilot or physical controller evidence. [Test coverage and limits](docs/TESTING.md).

## Launching and protecting data

`scripts/launch-deck.sh` identifies/reuses only this project's server, starts its authenticated exit companion, and runs the dedicated Firefox profile. The Flatpak path supplies `/run/udev:ro` only to that launch; [controller findings](CONTROLLER_NOTES.md) explain why startup enumeration differs from hotplug. No global shortcut mapping is required by the implementation.

The launcher profile's browser storage now holds career saves. Preserve `.runtime/firefox-profile/`; only launcher logs/session URLs in `.runtime/` are disposable. Export/import backups through the logbook and keep copies in `data/careers/` for source-checkpoint inclusion. Backups exclude the live browser profile to avoid copying inconsistent browser databases. [Data categories / restore](data/README.md).

Original human designs, raw inputs and boat artwork are retained. Terrain exports and brand graphics have authoring recipes; [art provenance](assets/README.md). Keep all source edits and build output stable until a checkpoint's restore check completes.


## Video / transcript pass

Current rationale, tuning and save compatibility: [feedback implementation](docs/FEEDBACK_IMPLEMENTATION.md). Shared `operating-state.js` gates power; `preparation.js` derives fuel/range advice from boat/day data. `menu-navigation.js` supplies geometry-based focus with explicit secondary-control exceptions. `career-data.js` holds the revised economy/fleet/crew/equipment balance. `balanceVersion: 2` migration preserves legacy installed tank volumes without changing the save envelope. See [tests and scope](docs/TESTING.md#video--transcript-pass--2026-09-11).


## Second video iteration workflow

Run `npm run verify` for the sequential acceptance pass: lint, format check, `npm test`, production build, Chromium/Firefox iteration flows, career/voyage, feedback, overnight/compact, prototype/environment, rendered day and controller/launcher. Browser tests use the production server at loopback port 5180 and isolated contexts; they do not use the player’s Firefox profile. `-- --unit-only`, `-- --browsers-only`, and `-- --browsers-only --suite=firefox` support focused diagnosis. The execution sandbox must permit local browser/launcher processes. Results are under `test-results/verification-*.json`.

`npm start` serves `dist` at 127.0.0.1:5173. Steam uses the same production server and original browser origin/profile. `npm run dev` is for deliberate development only. Do not run it on 5173 while launching the production game. `URCHIN_PORT` selects a test server port; `URCHIN_TEST_URL` and `URCHIN_TEST_BROWSER` configure harnesses. Source/helper edits stop while browser suites run.

Harbour operations are descriptors in `src/career-actions.js`; focus indices no longer determine their meaning. Harbour art/layout are in `src/harbour-view.js` / `src/harbour.css`. Wind loads and visual directions share `src/wind-motion.js`; season values are in `src/season.js`. Save validation accepts historical optional fields while rejecting invalid core numeric/entity state. The additive ground-v3 recipe retains original terrain and reef/clump identities. Decisions and balance values: [second-video record](docs/history/2026-09-11-second-video/DECISIONS.md).


## September 12 feedback and cleanup

Latest decisions, reproduction evidence, boat values and save compatibility are recorded in [the September 12 record](docs/history/2026-09-12-feedback/DECISIONS.md). Recovery eligibility stays pure in `diver-recovery.js`; simulation owns transitions and records diver samples before bag clearing. `expedition-actions.js` supplies stable departure, weather, chart and assist actions. `input-profiles.js` adds missing shortcut fields without discarding established device bindings. `starter-career.js` implements the one-time funded boat choice for new player careers; old saves bypass it. Frank's per-hull advice and the yellow SVG export are authored in `frank-advice.js` and `catch-sheet.js`; their screen styles live in `feedback-ui.css`.

`npm run verify -- --browsers-only --suite=september12` runs that production regression; `--suite=september12-firefox` selects Firefox. Both remain included in full verification. The full rendered suite includes prototype/environment checks, so the default run skips duplicate standalone invocations. The September 14 decomposition and current responsibilities are recorded above; this section is historical feedback context.

## Local feedback transcription

The isolated `.runtime/whisper/` tool now defaults to Whisper `large-v3` with CPU INT8 and batch 1; `small.en` remains available explicitly. Run `.runtime/whisper/venv/bin/python .runtime/whisper/transcribe.py 'videofeedback/recording.mp3'`. Use `--output 'videofeedback/recording.large-v3.txt'` to retain an earlier transcript, or `--model small.en` for the faster previous model. The helper refuses to overwrite media/text, verifies input checksums and publishes completed text only after the full run. Model downloads use `.runtime/whisper/download-model.py`; offline recognition uses cached weights and uploads no recordings. See [.runtime/whisper/README.md](.runtime/whisper/README.md) for the commands, pinned package list and local configuration backup. Source checkpoints exclude these reconstructible runtime tools and include the original feedback media/text.

Upgrade verification on 2026-09-12: local large-v3 excerpt and full latest recording pass, along with default-selection and overwrite guards; original video/audio/earlier text hashes match. The improved-model output is `videofeedback/2026-09-12 00-49-57.large-v3.txt`. The source/data milestone label is `whisper-large-v3-verified`; it preserves the feedback and documentation, while the excluded runtime tools retain their separate local configuration backup.


## September 15 feedback

[Decisions and verification](docs/FEEDBACK_SEPTEMBER15.md) supersede previous catch-care, DFO, pivot and roster notes. `fishery.js` saves a per-person bag sequence and one integer occurrence per bag. `vessel-contact.js` uses swept oriented rectangles; `patrol.js` adds independent low-speed translation and a bounded docking transition. Orders retain the existing person-record lifecycle. The new harbour PNG is copied unchanged from `assets/source/` to `public/assets/harbour/`.

TEMP recipe: after `npm test`, `npm run build` and browser acceptance, run `python3 scripts/package-temp.py --output <new-directory>`. It refuses an existing destination, includes `dist/`, dependency-free hosting/session helpers and engine licences, and generates/verifies a ZIP plus SHA-256 manifest. It never copies careers, profiles, logs or development inputs. Portable server defaults to port 5197; optional `--lan` enables same-network devices. Platform launch helpers and readme are authored under `scripts/portable/`.


## September 15 itch.io TEMP follow-up

[Decision ledger](docs/FEEDBACK_ITCH_TEMP.md) records this amendment once. `time-speed.js` owns the browser pace preference; the scene scales only its fixed-step accumulator. `diver-search.js` handles open scouting. `coastal-ground.js` is the additive v6 authoring recipe. `touch-boat.js` projects gestures into hull coordinates. `fullscreen.js` handles browser fullscreen. Existing scene, geometry, camera and physical input ownership remain.

Build and package after verification:

```sh
npm run verify -- --unit-only
npm run verify -- --browsers-only --suite=itch-feedback
npm run verify -- --browsers-only --suite=itch-feedback-firefox
python3 scripts/package-temp.py --output exports/2026-09-15-itch
```

The output directory must be new; the packager never replaces an existing export. `UrchinSkipper-TEMP-ITCHIO.zip` is the preferred browser upload, with root index.html and notices. `Urchin Skipper TEMP.zip` remains optional for local/LAN hosting. Both use the same dist bytes. Vite base `./` plus relative runtime artwork URLs supports nested hosting. CSS public-asset URLs are rewritten by Vite. The browser suite rejects out-of-subdirectory requests and checks a separate-origin iframe with fullscreen permission. Archive limits follow [itch.io's current guidance](https://itch.io/docs/creators/html5).

Keep old checkpoints/exports. All new personal/device testing goes into the current playtest guide; synthetic controller and headless-browser results do not establish physical input or mobile performance.


## September 15 keyboard/remapping amendment

[Decisions and migration](docs/FEEDBACK_KEYBOARD_CONTROLS.md). `keyboard-controls.js` owns old-default migration and browser event protection; `keyboard-view.js` renders the live keycaps. `controller-view.js` selects one diagram and scopes reset/remapping to its device. Keyboard Escape has its own menu-stack close path; pad Menu/B keep history. Shift-alone actions wait for key release so modified shortcuts do not cycle detail levels. No simulation or controller mapping changes.

Reproduce with `npm run verify -- --unit-only`, `npm run verify -- --browsers-only --suite=keyboard-feedback`, `--suite=keyboard-feedback-firefox`, `--suite=controller`, and the existing itch-feedback suites. Additive TEMP recipe: `python3 scripts/package-temp.py --output exports/2026-09-15-keyboard`.


## September 16 Samsung S22 / Frank

[Decision ledger](docs/FEEDBACK_S22_FRANK.md) owns the new UI, inspection, safety, insurance, purchase and introductory-career behavior. `career-intro.js` owns the separate deterministic cove and lesson progress; `intro-view.js` owns the briefing/aboard/chart UI. Session hooks create and finish only explicitly opted-in new-career lessons. `insurance.js`, `purchase.js` and `ui-scale.js` keep their respective policy separate from screen composition. Browser acceptance adds `--s22-feedback-only`; all assets remain locally bundled.

Source checkpoints also exclude nested portable `.player-data` directories. Preserve those live profiles in place and export their careers through the logbook; they are not disposable source-cache data.

## September 16 — lesson cues, departure fade and title bookmark

[Designer decisions](docs/FEEDBACK_FRANK_TRAVEL_NAVIGATION.md) are authoritative for this increment. `lesson-cues.js` draws port/stern hull rails and readable callouts; `intro-view.js` supplies the scrollable lesson readout. `departure-transition.js` stores only the elapsed fade on the day, derives a render-only continuation pose and calls the existing harbour settlement after 2.2 seconds. `main.js` advances this animation at real-time speed, retaining focus/menu locks. Saves validate and restore an in-progress fade.

`screen-navigation.js` now maintains backward and forward view stacks per [the clarification](docs/FEEDBACK_MENU_HISTORY.md). Public Back visits each prior menu and then title; Forward retraces them. Internal `previous()` remains for Cancel, completed purchases and Menu. History is guarded by world identity and phase; world replacement or a new navigation branch clears the appropriate stack. Never replay a purchase callback through Forward. Focused browser recipe: `URCHIN_TEST_URL=http://127.0.0.1:5180/ PLAYWRIGHT_BROWSERS_PATH=.browser-cache node scripts/browser-smoke.js --frank-navigation-only` (add `URCHIN_TEST_BROWSER=firefox` for Firefox). The controller regression also exercises Back/Forward and retained Menu release gating.

## September 16 gameplay windows

[Decisions and reproduction](docs/FEEDBACK_HUD_WINDOWS.md) document the touchscreen visibility toggle and scrollable, resizable HUD groups. `hud-windows.js` places stable corner controls beside live content, with explicit CSS anchor directions and per-orientation session sizes. Focused window scrolling/resizing is excluded from boat key routing. Browser acceptance uses `--suite=hud-windows` / `--suite=hud-windows-firefox`.

## September 16 harbour and shops follow-up

[Designer decisions and reproduction](docs/FEEDBACK_HARBOUR_SHOPS.md) record the clarified top-of-shop Your boat control, explicit purchases, scenery anchoring and lesson guidance. Candidate fields are transient view state retained in navigation history and cleared on world replacement. Optional saved `intro.scoutSeconds` is bounded to 0–60. Labels use the actual polygon boundary and screen-space clearance without changing simulation geometry.

## September 16 boat card, approved harbour and title fix

[Designer amendment](docs/FEEDBACK_BOAT_CARD_HARBOUR.md) restores the touch tutorial's separate helm card, preserves DOCX §23's harbour composition and confines title scrolling to `.title-copy`. The harbour's `.wharf-content` keeps artwork and the approved button grid in one coordinate space, with the original full-viewport composition at 1280×800. Compact screens pan it. Routine checkpoints are retired in favour of additive verified game exports per the designer; see [preservation](data/README.md#september-16-preservation-amendment).

## September 17 small-screen UI and training

[Decision ledger](docs/FEEDBACK_S22_LATEST.md) records this amendment. `assist-options.js` and `assist-view.js` separate explanations and UI/difficulty groups; `hud-windows.js` keeps movement/close/resize controls outside live markup. `s22-ui.css` places independent compact boat/diver windows in the existing bottom clearance. `touch-scale.js` is independent of text scaling. `binding-picker.js` uses existing remapping conflict protection. `training-replay.js` prepares a copied career and equipment lessons before the existing `career-intro.js` sequence; `career-session.js` owns original-world restoration. No training progress is saved over the career.


September 17 shoreline hazards: [single decision/implementation record](docs/FEEDBACK_SHORE_HAZARDS.md) covers fixed-feature generation, physics/chart/sounder agreement, visible uncharted crowns, persisted weather cohorts and the additive export recipe.
# September 20 device update

Decisions for this increment: [landscape device amendment](docs/FEEDBACK_SEPTEMBER20_DEVICES.md). Primary modules: `hud-defaults`, `instruments`, `device-feedback.css`, `layout-editor`, `screen-navigation`, `troubleshooting-log`, `screen-fit`, `kelp-cache`. Day-start snapshots are additive keys in `career-save`; no player data is pruned. This increment's exports use `python3 scripts/package-temp.py --output exports/2026-09-20-device-feedback` and refuse an existing output directory. Historical DOCX reference recipe/preservation: [archived editing script](archive/design/2026-09-23/add-settings-reference.py.txt); this recipe is retired and must not target the archived original. Storage inventory: `scripts/audit-storage.py` (read-only scan).

Acceptance: `npm run verify -- --unit-only`, then `npm run verify -- --browsers-only --suite=device-feedback`, `--suite=device-embed`, and an isolated `--suite=performance` run. Physical controllers and Android GPU/FPS remain separate from synthetic browser evidence. [Acceptance record](docs/history/2026-09-20-device-feedback/README.md).

## September 24 deployment and tablet feedback

[Acceptance and unresolved device issues](docs/history/2026-09-24-deploy-and-tablet/README.md). The new production journey is `npm run verify -- --browsers-only --suite=tablet-feedback` (or `tablet-feedback-firefox`). It covers actual touch deployment without changing portrait, the old labelled minimap shortcut, default deck load, preparation/reload, viewport changes and retained dry-weather/control rendering. Use existing `performance` / `performance-firefox` suites in isolation. Shared target selection lives in `src/diver-recovery.js`; direct pinned IDs remain authoritative for input consistency. Recall uses hull clearance in `src/diver-recall.js`.

## September 24 coasting and traffic

The [living Bible](bible.md#16-other-boats-rivals-and-inspections) and [keyboard provenance](docs/DESIGN_CONSOLIDATION.md#september-24-keyboard-follow-up) supersede earlier local encounter tuning. `water-loads.js` smoothly limits the forward high-speed passive force couple while keeping the light-flow term. `rival-plan.js` owns full-hull berths, conservative tide clearance and deterministic daily visit/nearby/mystery decisions; `shipSeen`/`shipNearby` in the daily fleet persist limits across saves and sector changes. Existing actors receive a safe berth route on first update; already shallow saved boats can escape with their former narrower clearance before resuming full-hull clearance. `traffic.js` holds working berths, conserves clump stock, moves to another ground when necessary and marks departures. Ordinary taxis select distant water entries/exits, with a 30% eligible working-area pass; route intent does not track moving divers. One-metre water-route samples avoid narrow-shoal aliasing. `traffic-coasting.test.js` and `--suite=traffic-coasting` / `traffic-coasting-firefox` provide focused regression/production evidence. [Local review, measurements and limits](docs/history/2026-09-24-traffic-and-coasting/README.md).
