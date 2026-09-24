# Playtest guide — September 23 touch and portrait

Use [the new itch.io TEMP ZIP](exports/2026-09-23-touch-and-portrait/UrchinSkipper-TEMP-ITCHIO.zip), or [the local/Wi-Fi TEMP ZIP](<exports/2026-09-23-touch-and-portrait/Urchin Skipper TEMP.zip>). Confirm **TEMP · SEP 23 · TOUCH & PORTRAIT**. Older exports remain available. [Decisions and scope](docs/FEEDBACK_SEPTEMBER23.md).

Keep testing the familiar 14-inch landscape setup. Portrait is enabled again. Open **Touchscreen Options** from the title, Settings or Pause. Try 70% Tiny controls and 40–60% opacity; UI Scale remains separate. Harbour fills the display. Physical phone/tablet/Deck performance, speakers and USB Xbox controls still need human playtesting.

## September 23 checks

- From title → Touchscreen Options, turn touch mode on, drag both sliders, then Back. Continue the same career. Repeat from Settings, sea Pause and Frank’s lesson Pause; Back returns to the opener. Toggle Adjust UI / Show information here or with their on-water shortcuts.
- Compare 50, 70, 100 and 150% controls in both orientations. Tiny selects 70%, then you can fine-tune it. Action buttons, gear buttons and both sticks resize; instrument windows keep their own size. Set opacity to 43%, leave and reload. At 0%, Menu/help stays visible so Reset remains reachable.
- Match the supplied phone screenshot’s top instruments, chart/load/current below and bottom helm/diver cards. Existing personal layouts still win; Arrange UI → Reset positions opts into the new defaults. Default action prompts should sit above the controls when their scale changes. Optional text cards still follow your information choices.
- Cold-launch the itch page in portrait with OS auto-rotate enabled. Rotate before touching the game’s Fullscreen button, then after entering/leaving fullscreen and after switching away/back to the browser. Portrait recovery should no longer depend on that particular button. Actual hosted Android behavior still needs this physical check.
- At UI Scale 50/60/70/100/150%, return to Harbour. Pan to Settings on a narrow phone. The header should hug its contents and remain clear of the top row of buttons.
- Compare steady idle, forward and reverse with speakers and headphones. Audio now avoids rebuilding engine loop schedules every frame. Compare motion with volume on/off, initially without screen recording. If choppy, enable Troubleshooting log before a short repeat and download afterward; it now includes frame and audio/viewport details. [Tablet assessment](docs/DOOGEE_TAB_E3_MAX_REPORT_2026-09-23.txt).

## Retained regression checks

- Wait for preparation to finish, then tap Chart quickly and release. The chart should stay open. Repeat while using touch helm controls; closing it must not steer or reopen it.
- With OS auto-rotate enabled, rotate phone/tablet both ways on water and while Arrange UI is open. Clock and pounds remain visible. Make a change in portrait, rotate, change landscape, Save, then revisit both orientations. Adjust UI drag/resize controls should remain usable. On itch, enable Mobile friendly and allow any orientation in the host settings.
- Check red digits stay inside the clock face at default/custom sizes. Minimap → Chart only should show just the map, without labels, backing, border or controls. Graphic mode retains chart controls.
- Reverse and pivot while zoomed in. Propulsion wash and diver bubbles disappear under the opaque hull; deck artwork stays clear. Confirm the existing instrument artwork and landscape arrangement look familiar.
- Work for several minutes, including tide changes and at least two ten-second autosaves, then reload the career. Compare crowded coast/night/fog scenes and training transitions. Initial artwork is prepared up front; a new sector may briefly show preparation while its local raster is painted. No terrain download is deferred into a trip.

## Continuing gameplay checks

1. **Listen to the helm.** Neutral idles quietly. Forward grows louder and higher with throttle; reverse has a distinct whine/flutter. Full throttle should be unmistakable, with stronger wash and wake. Listen for a thin double whistle when a diver surfaces: nearby is loudest, distant fades away. Check the master volume and whether a browser interaction is needed to unlock sound.
2. **Day planning.** Harbour menus pause the clock. A normal day starts at 05:00; choose 07:00 to avoid the early-start fatigue cost, or Sleep → fish next day. Miss 19:00 offload: catch lands at the next 06:00, and the next departure is 09:00. Early departure is unavailable that morning. Later returns add fatigue and age the catch. Diver flashlights allow night work, with double work fatigue; unlit evening departures with no daylight left are replaced by the equipment/rest choice.
3. **Crew.** Compare Base / Trained / Today stats, including precise holding current. Level cap is 20. Fatigue should accumulate noticeably over repeated working days and clear more slowly. Medical & absence history records new sickness, injuries and recovery; old saves cannot explain past unrecorded absences. Nitrogen behaviour is preserved.
4. **Layout.** Phone portrait keeps the boat centre clear and touch actions reachable. Arrange UI shows ON/OFF and graphic/text indicators. Move diver cards to the bottom, save, leave and reload. Change something, Back, then Exit without saving: the previous layout should return. Portrait and landscape retain separate saved layouts; touch size does not switch instrument layouts. Reset positions opts into current defaults.
5. **Instruments.** Hull silhouette cracks as damage increases; deck bags show load. Photographic instrument housings have live readouts without blue cards. Minimap defaults to Chart only, with no labels or control buttons; choose Graphic for chart controls or Plain text. Chart key/touch action still opens the large chart. Arrange UI → Timepiece → Clock face cycles every owned clock, including the original red digital one.
6. **Portraits and boat setup.** Meet the crew includes all remaining diver portraits. Your boat and Chandlery show an equipment blueprint by physical station, including dive gear, drive, sounder and compass.
7. **Input.** Keyboard use in a menu selects keyboard input. On water, WASD and arrow clusters show the actual mapped keys and functions; remapping updates them. With a jet, right-stick up/down commands stern turning: twin opposed jets turn tightly, a single sideways nozzle turns in a wider circle. Left-stick horizontal is bow thrust only when installed. Explicit full-ahead/full-reverse cancels a simultaneous pivot command. Rudder and throttle otherwise remain latched.
8. **Grounding.** Easy allows slow powered reverse toward deeper water despite wind. Realistic keeps the engine-versus-wind struggle. Neither can drive over a dry sill; wait for tide. The final tutorial reminder explains the selected difficulty and morning offload.
9. **Wildlife and rivals.** Watch for V-shaped geese, gull mobs, occasional eagles and rock sea lions. Nearby sea lions can slow picking temporarily. Surfaced whale strikes incur $35,000–$50,000 fines and increased DFO attention. Rival boats work between bubbles and gradually load bags; more skippers now fish and deplete shared beds. Compare fleet reports and stock over multiple seasons.
10. **Raster and saves.** Import the provided tablet career on Deck; switch boat art Raster → Vector → Raster. Both the player and taxis should draw recognizable boats; failed artwork loads now retry. Repeat Tiny Touch Controls/fullscreen Training Mode entry and Hide/Show UI, then return to the real career. Exported career JSON now includes a bounded local troubleshooting snapshot. For intermittent hangs, also enable the detailed troubleshooting log before reproducing and export it after.

## New grounds

All original nine maps remain. Later coasts have fewer chart marks but abundant actual stock. The two new permits each open three maps on the existing season-day 1/3/5 schedule:

- **Maelstrom Coast ($60,000):** Knifepoint Race (shoreline race and headland eddies), Boulder Garden (high-water entry, low-water shelter), Needle Sluice (jet access).
- **Outer Reaches ($100,000):** Seventy Foot Shelf (18–21 m premium ground), Devil’s Elbow (remote deep headland), The Locked Vault (remote, deep, jet-access tidal basin).

Sound the basin gate before entering. At low water even jets cannot leave; the rising tide opens a longer window for jets than deeper boats. The sheltered basin contains exceptionally fast, 100%-quality picking. Bring fuel, rested crew and suitable night/deep-diving equipment. Deep ground remains within the game's existing depth system. Watch tides in the almanac and the actual sounder; Debug tide overrides can demonstrate access, but normal-tide trips are the balance test.

Export a career before a long test. Named restore points and automatic day-start saves remain additive and local to the browser; loading preserves the current career in an archive. Never clear browser storage as a routine test step. New tuning deliberately increases pressure; the enjoyable number of seasons remains a playtest question.
