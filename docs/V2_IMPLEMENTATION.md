# Definitive v2 implementation pass

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Authority: [Bible](../archive/design/2026-09-23/Urchin_Skipper_Bible_Definitive_v2.docx) and the designer's September 14 implementation request. This is an implementation ledger, not a replacement design document. Originals and old checkpoints remain untouched.

## Explicit September 14 amendments

- Island Tender: 25 knots unloaded, 15 knots at full catch capacity.
- R3 opens information assists. Easy careers cycle Easy → Realistic → All Off; Realistic careers cycle Realistic → All Off. Custom widgets remain configurable and saved. Realistic includes exact deck/diver readouts, clock/offload, helm instruments and chart ground markings. A separate portrait-only diver selector reveals selection without underwater state. These instructions supersede Bible sections 11/18 where their earlier Realistic restrictions differ.
- Keep Test Mode's current location; designer will supply the dock/arcade background later.
- Use the supplied Channelmaster image for title/save/load and named boat images for fleet purchases and activity. Add similarly specified sister boats. Rival sprites serve seeded opponent teams. One seeded nine-ships sprite belongs to hidden loyal Shy Hull Wood crew; other nine-ships sprites are 5-knot tourists that avoid bubbles. Taxis: 30 knots, avoid boats, ignore bubbles. DFO: 25 knots, approach fishing vessels, wait 100 m away, block deployment during the visit; inspection currently costs time only (section 16).
- Add simplified depth/time exposure, surface recovery and persistent repeated-day DCS risk. Conservative divers stop earlier; reckless divers can ignore limits. Gameplay abstraction, never a real-world dive-planning tool.

## Bible differences to reconcile

- Section 19: Y deploys/boards; X handles bags; nearby A summons an underwater diver after a 2–5 s response with audible clanging. Preserve remapping/device identity, release gates and orthographic presentation.
- Sections 8/9: surface when the entire working patch is exhausted; do not search another patch. Air reserve 20; ordinary scouting limit 70 s, better crew 15 s; individual orders persist.
- Section 4: shoal grounding constrains motion without hull damage; impact hazards remain separate.
- Section 16: physical other-vessel traffic and randomized crews replace abstract-only competition and scheduled-only inspections.

## Work ledger

- [x] Stabilization: chart cap, cheap validated saves, HUD updates, session/screen decomposition, meaningful performance checks.
- [x] Shared menu/controller fixtures/math/random/formatting; broaden lint; remove confirmed dead code and unused exports.
- [x] Verify stabilization milestone and restore-check checkpoint.
- [x] V2 controls, assists, diver selection and new-game tuning, save migrations.
- [x] Generated chart material, supplied title and fleet artwork, purchasable sister vessels.
- [x] Physical rivals, taxis, tourists and DFO; persistent crews, loyalty and transfers.
- [x] Next Bible slices: exhausted-ground/air/scout behavior, recall, harmless grounding, training controls.
- [x] Simplified dive exposure and repeated-day DCS behavior, persistent crew consequences.
- [x] Automated/browser/controller/visual acceptance, playable build and current documentation.

Final accepted-build checkpoint outcome is recorded separately in [the restore/hash record](../checkpoints/v2-implementation-verified.json), so the archived documentation need not be changed after its own verification.

Pre-edit checkpoint: `pre-v2-stabilization-20260914T111107Z.tar.gz`, 328 files restored and hash-verified. Physical Deck routing/FPS remains a hardware playtest, distinct from automated coverage.

## UX / new-game increment

Implemented R3 assists (old unmodified R3-order shortcuts migrate; explicitly remapped buttons retain ownership), Easy/Realistic/All Off naming and per-career cycles. Realistic starts exclude Easy-only aids. Custom widget sets persist in their own mode slots. Legacy Medium migrates to new Realistic; legacy Realistic migrates to All Off. New careers choose difficulty on the first-boat screen. Realistic includes the requested instruments and exact readouts. Disabling full diver indicators while enabling portraits shows identity/selection only. Island Tender is 25/20/15 knots at empty/half/full catch.

230 automated tests pass; lint/build pass. Chromium and Firefox v2 UX suites pass through both new-career difficulties, R3, cycles, portrait selection, compact UI and save/reload. Screenshots inspected. Restore-checked checkpoint: `v2-ux-verified-20260914T115133Z.tar.gz`, 357 files.

## Core diver increment

Implemented Y deployment/boarding, X bag work, nearby A recall with one clang and a deterministic 2–5 s response, mutually exclusive throttle/thruster stick commands, immediate whole-patch exhaustion ascent, safe 20-unit air reserve, 70/15-second scouting defaults and remembered individual orders. Grounding constrains without hull/drive damage. Explicit remaps retain priority over new default shortcuts.

236 automated tests, expanded lint/format and production build pass. Chromium v2, controller and keyboard fishing/recovery checks pass. The broader rendered run stopped at an obsolete assertion that inspected hidden All Off telemetry; the corrected prototype continuation is being rerun. No physical controller or medical realism certification is claimed.

Core checkpoint: `v2-core-before-art-20260914T120812Z.tar.gz`, 359 files restored and hash-checked. The subsequent prototype rerun exposed a one-frame/100 ms HUD delay after recovery; significant state/catch/notice transitions now refresh immediately while ordinary telemetry remains bounded. The complete prototype continuation passes after that correction.

## Artwork / sister vessels

Supplied Channelmaster art is used on title and save/load panels. All 37 selected boat PNGs are copied unchanged into the runtime catalogue; tests compare hashes to the originals. A shared runtime framer omits neighbouring sheet fragments and caches at most 320×640 canvases instead of keeping full-resolution textures. Six sister models use the same propulsion and speed profiles, with 4% more capacity/mass/price, 0.2 m more length and 20 L more fuel. Family-compatible upgrades and independent saves are tested. No new dependency.

The imagegen skill produced [a material atlas](../assets/source/charts/README.md), not invented navigation geometry. Actual coast/depth masks, ground outlines, currents, labels and tracks remain authoritative. Runtime title, compact title, load screen, charts, purchase previews and all 37 framed boats were visually inspected.

239 tests pass; lint/build and production vessel/prototype suites pass. Chromium automatic Canvas normal scene: 16.67 ms/frame mean, 16.70 ms p95, CPU p95 8.10 ms. Forced software WebGL remains slow (66.76 ms mean); not a physical Deck measurement. Physical NPC behavior and DCS are next, not included in this art acceptance.

## Stabilization evidence

Verified milestone: `checkpoints/v2-stabilization-verified-20260914T114006Z.tar.gz`; 354 files restored and hash-checked. Retained with the pre-edit archive.

The 86-module source import graph is acyclic. All installed direct packages have an active role: Phaser is the sole runtime dependency; the rest provide building, lint/format or browser verification.

The expanded lint, formatting and production build pass; 225 automated tests pass. Source responsibilities now include `career-session`, `session-state`, `hud-view`, and separate screen navigation/action/render/feedback controllers. Main scene orchestration is about 280 lines; PlaytestUI is 346. No new dependencies. The audio RNG intentionally remains local to its sample synthesis loop; its output is unchanged by the shared world RNG extraction.

Isolated production Chromium/Firefox performance, controller and iteration suites pass. Chromium normal scene: 17.31 ms mean / 16.8 ms p95 with automatically selected Canvas, versus 79.16 / 83.4 ms forced software WebGL. Firefox retained WebGL: 16.85 / 17.14 ms. Chromium zoomed-out storm career: 28.89 / 33.4 ms, CPU p95 14.6 ms. See [method and budgets](PERFORMANCE.md). Gameplay, chart and compact-menu screenshots were inspected. The last arithmetic extraction preserves identical bearing formulas and is covered by regressions.

The earlier concurrent controller attempt failed on reload when another runner shut down its shared test server. Sequential reruns passed, including authenticated launcher exit. Verification runners must not share ownership of a server concurrently.

## Physical fleet and people

Thirteen seeded public opponent teams use the thirteen rival sprites, varied speed/turning and generated divers with persistent experience and employment. One additional loyal hidden team uses a seeded nine-ships sprite; its skipper/divers are absent from ordinary roster and results. The Bible §17 rare Shy Hull Wood radio Easter egg is explicitly retained, separate from ordinary player information. Non-loyal crew can be poached or leave after sustained poor conditions, between days; loyal/hidden crews cannot be poached even by the contact unlock.

`traffic`, `traffic-motion`, `water-route`, `traffic-view` and bounded settings separate movement, water routing and presentation. At most seven actors; 10 Hz NPC decisions/movement, interpolated through ordinary rendering. Taxis use 30 knots and ignore bubbles while avoiding boats; tourist nine-ships use 5 knots and avoid player/rival bubbles. DFO uses 25 knots, routes to a 100 m stand-off, locks deployment, waits for recovered crew, then consumes configurable game time without new fines or confiscation. Historical fines remain historical. Actual local rival picking removes the same clump stock; offscreen sectors use bounded aggregate work and cannot double-harvest the active sector. These are first-pass NPC simulations, not a full duplicate of the player's SCUBA/helm state machine.

Traffic routes/timers/positions survive saves. Optional traffic/exposure fields migrate without disturbing old trips. 250 tests passed at the traffic milestone; its production traffic and complete career/voyage checks passed. The latter returned a naturally picked 300 lb bag on time, 100% hull, both crew fit and $95.45 operating return. Restore-checked checkpoint: `v2-traffic-before-dive-exposure-20260914T124453Z.tar.gz`, 455 files.

## Dive exposure and training increment

[Dive exposure decisions and limits](DIVE_EXPOSURE.md) record the fictional calibration and medical boundary once. Player and physical rival divers accrue exposure; conservative divers stop earlier, ordinary divers observe limits, and Roy plus one seeded opponent can ignore them. Per-person risk survives tanks, bags, hiring, saves and multiple days. Suspected DCS appears at surfacing, ends fishing and records a five-game-day absence without blocking medical recovery/return. Air reserve remains independent. Ordinary menus do not expose hidden adherence traits or numerical hazard; portrait-only mode remains identity-only.

256 tests passed with exposure enabled. The focused training increment adds guarded state/bag/air/ground manipulation, level/delevel controls, explicit health reset, encounter spawning, 0.25×–4× simulation speed and single-step. All career mutations are Test Mode-only; normal saves cannot be overwritten. Boat/equipment unlock now reaches the highest rank, with funds and normal purchase menus retained. This is the next independently tested §21 slice; the designer's future arcade background is deliberately not fabricated.

The production training/DCS controller flow passes at 1024×640, including exact preservation of the real save. Screenshots inspected. Completing this pass is not a claim that every Bible feature is finished or physically playtested.

## Final acceptance

263 automated tests, expanded lint, formatting and production build pass. All 19 browser/controller stages pass through a broad production run and focused continuations after explicitly documented fixture corrections. This is not represented as one all-in-one successful invocation: the original failed aggregate reports remain preserved. [Evidence, build fingerprints, successful stages and limitations](history/2026-09-14-v2/acceptance/README.md).

The final source graph has 101 reachable modules, 13,004 lines and no circular imports. Main orchestration is 311 lines; PlaytestUI is 352. No new dependency. The current 63 MB build includes 47 MB of unchanged supplied boat PNGs, rendered through bounded lazy canvases. Generated chart material remains subordinate to real geometry. All 107 protected inputs match the pre-pass archive; the terrain authoring recipe changed only by formatting and reproduces identical exports.

The final complete voyage landed 300 lb on time with 100% hull, both crew fit and $97.05 operating return. Normal, seven-vessel and storm benchmarks pass unchanged headless budgets in Chromium and Firefox; [sample details](PERFORMANCE.md#final-build-samples). Physical Deck controls/FPS, sustained cache-rebuild costs, long-run stock/economy/exposure balance and richer NPC decisions remain future verification/iteration work. Test Mode's dock/arcade background still awaits the designer's image.
