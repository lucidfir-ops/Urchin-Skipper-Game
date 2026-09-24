# September 21 playtest amendment

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Source: designer's September 21 request and preserved files in `feedback/9-21/`. The DOCX remains authoritative except for these explicit subsequent amendments. No original feedback, reference, portrait, career or previous export is replaced.

Decisions: later instructions supersede earlier ones: replace experimental fit with Tiny mode; re-enable portrait while preserving desktop landscape; missed evening offload uses 06:00 next morning and earliest departure 09:00. Harbour menus pause time. Ordinary planning begins 05:00, with a later, rested departure available. Late/night fishing remains possible with equipment and consequences. Easy reverse grounding assistance is the requested exception to Bible §§18/20 shared physics (reported before implementation); Realistic retains wind-limited escape. Deep beds remain within §5's 70-foot limit. Tide-locked fishing basins explicitly extend §4's previously deferred tidal stranding. Existing nine maps, currents, eddies, logs, nitrogen behaviour and eight finished portraits are preserved.

The supplied diagnostics contain only build/browser headers. Day-15 career confirms the old random shipping delay produced 09:11 planning. Day-17 shows Milo's previous absence but no recorded cause; do not invent a retrospective diagnosis.

Implemented:
- [x] Clear morning/offload/day planning; cumulative fatigue, level 20, stat comparisons and medical history.
- [x] Portrait/Tiny defaults, bare chart, instrument artwork, clock selection, layout indicators/cancel/save fixes.
- [x] Reliable raster/vector vessels and diagnostic save export; training/input regression.
- [x] Correct single/twin jet pivot visuals and handling; Easy grounding; throttle feedback.
- [x] Two additional coasts/six physical maps; generous hidden stock and tidal challenge geometry.
- [x] More rival fishing/pressure with visible bubbles, bags, speed-based arrival/return.
- [x] Whales/fines/DFO, rock sea lions/diver interference, restrained birds.
- [x] Remaining unique crew portraits, installed-equipment boat blueprint, visible keyboard bindings.
- [x] Final browser verification and additive TEMP exports (receipts are recorded in the linked release history).

Art: built-in imagegen skill; source atlases and generation briefs retained in [the art record](../assets/source/september21/README.md). Generated assets are presentation only and never collision geometry.


Tuning and implementation details:

- Fatigue now starts affecting swimming, picking, air use and holding current at 8%; work accrual is 0.00065 per simulation second before modifiers, ordinary overnight recovery 6.5 percentage points, full rest adds 22 points. Work after dark still doubles accrual. Returns after 19:00 add 2.5 points per late hour. Level 20 permits extreme specialists while bounding air/fatigue savings at 65%. Nitrogen kinetics and surface-interval rules are unchanged.
- Neutral/forward/reverse are distinct original procedural loops. Engine gain rises from 0.055 at idle to 0.675 at full command before master volume; pitch rises with load/speed. Surfacing triggers a two-note 1.85 kHz whistle, fading to silence at the existing 65 m sound range. Powered wash responds before the hull gains speed. Existing water, recovery, warning, radio and thunder sounds remain.
- Preserve every original sector recipe/output. Maelstrom and Outer Reaches permits cost $60,000/$100,000 and each contain three maps. Additional beds are additive and unmarked; boulder-basin picking is rate 45 (about ten seconds per full bag for a fresh baseline diver), quality 1.0. Their scalloped drying rims and gates use authoritative bathymetry, with a tide-dependent sheltered current. Jet-only basins have a natural high tide too low for the conventional draft. Debug overrides can exceed that natural tide.
- Approximately 78% of ordinary rival teams are selected daily; daily target catches multiply by 1.6 and regional background pressure rises. Slow boats choose a reachable home ground instead of attempting an impossible remote round trip. Visible fishing uses bubbles, pickup movement and bag accumulation against shared stock; offshore accounting remains an aggregate approximation. Economic sensitivity now reaches Frontier in the second season in the aggressive fixture instead of requiring season one. This is an intended consequence of increased pressure, not a claim of final balance.
- Surfaced orca/humpback strikes cost $35,000/$50,000 once per animal and increase patrol scheduling through day +6. Submerged whales cannot be hit. Rock sea lions have intermittent 45 m harassment windows reducing picking to 55%, without injuries. Geese join the bounded wildlife scheduler.
- Original 8 portraits plus a new 28-tile atlas cover the generated diver roster. UI render geometry remains separate from collision geometry. Hull/load use a damaged silhouette and bag stack instead of circular gauges. Atlas housings surround live SVG/HTML readouts. Clock selection retains the original digital face.
- Quota-state version 3 migrates older 3-map/9-map records before exposing all 15 maps. Automatic saves stay lean; user-exported JSON includes the current bounded troubleshooting snapshot. Failed image loads are retried and logged. No root cause is asserted for an unreproduced physical Deck crash.

Verification and exports: [release history](history/2026-09-21-playtest-feedback/README.md). [Current playtest guide](../PLAYTEST_GUIDE.md). The provided feedback and JSONs remain unchanged; no original design document, harbour reference, save or previous export was replaced.
