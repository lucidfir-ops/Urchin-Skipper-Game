# September 16 — Frank, map departure and title navigation

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Designer amendment following the S22/Frank TEMP: the preceding update has **not yet been playtested**. Add visible tutorial pickup-side guidance, a boat fade at the map exit, and Back/Forward navigation; produce new additive TEMP editions. This extends [the preceding feedback](FEEDBACK_S22_FRANK.md). The definitive Bible remains the design authority; its port-side recovery and orthographic view are retained.

## Decisions and behavior

- Frank points out the green port working rail, its actual pickup sector and the orange stern. Labels have leaders to the boat and remain readable through zoom and turning. His recovery line explains port relative to the bow, Neutral, matching drift and reversing danger. These are presentation cues; collision/pickup geometry and eligibility are unchanged. The marked/unmarked harvest lesson, skip options and existing-career bypass remain.
- On touch screens, Frank's scrollable card includes throttle, rudder, depth and both diver states/catches. It replaces the usual helm panel during the lesson. Portrait dialogue sits above the boat; short landscape puts it on the left and offsets the orthographic follow framing to leave the boat visible. No free camera or simulation geometry change.
- Crossing the designated harbour edge with both divers aboard starts a 2.2-second continuation/fade before offloading. Hull, deck, crew and shadow fade together; a caption explains continued travel. Animation time is independent of the world-speed preference. The existing return transaction still calculates passage fuel, shipping time, inspection and settlement once. Saving mid-fade resumes it; no extra fishing time or fuel is charged for the animation. Other edges and the enclosed day-zero cove retain their existing boundaries.
- Navigation was subsequently clarified by the designer: Back should step through menus to title, and Forward retrace them. The [menu-history amendment](FEEDBACK_MENU_HISTORY.md) supersedes this increment's original direct-to-title interpretation and defines the current behavior.

## Verification and packaging

Focused simulation checks cover physical edge crossing, the visible intermediate fade, save/reload, unchanged time/fuel, once-only settlement, all four edge directions, diver-abandonment rejection and the closed practice cove. Navigation tests cover title/Forward, saved views, stale-world rejection and dismissed purchases. Existing purchase, helm, complete lesson and career regressions remain required.

Browser evidence and package fingerprints: [acceptance record](history/2026-09-16-frank-travel/acceptance/README.md). Physical S22 and actual itch.io upload remain the designer's next playtest; headless touch and synthetic controllers do not establish physical performance or input behavior.

Recipe: `npm run build`, then `python3 scripts/package-temp.py --output exports/2026-09-16-frank-travel`. The two ZIPs contain identical game bytes; the local/Wi-Fi edition adds existing launch helpers. Older exports, profiles, saves and original artwork/documents stay preserved. Title identity: **TEMP · SEP 16 · FRANK & TRAVEL UPDATE**.
