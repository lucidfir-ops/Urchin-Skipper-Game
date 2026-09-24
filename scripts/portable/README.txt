URCHIN SKIPPER — TEMP LOCAL / WI-FI COPY — SEPTEMBER 21 PLAYTEST UPDATE

For itch.io browser play, upload the separate UrchinSkipper-TEMP-ITCHIO.zip.
That is the recommended distribution; players only need a browser.
This folder is the optional local / Wi-Fi version of the same build.

Extract this entire folder before playing. It can be moved or renamed. The built
game, world data and artwork are local; no npm install/build or internet is needed
once Node.js 22+ and a browser are installed. Node.js itself is not bundled.

WINDOWS
Install Node.js 22+ if needed, then double-click Play Windows.cmd. Your default
browser opens. Use Firefox or Chromium/Chrome/Edge for the tested browser engines.

MAC
Install Node.js 22+ if needed. Run Play Mac.command. If macOS will not execute a
downloaded script, open Terminal in this folder and run:
  node scripts/start-portable.js
Safari has not been verified. Use Firefox or Chromium/Chrome for this playtest.

LINUX / STEAM DECK
Run Launch Game.sh (or: bash "Launch Game.sh") for the dedicated Firefox session.
It uses its own .player-data/firefox-profile and port 5197. Add this launcher as a
separate non-Steam game if wanted. Existing shortcuts and saves are untouched.
USB Xbox is physically confirmed; built-in Deck controls still need human testing.
Manual browser alternative on any computer:
  node scripts/start-portable.js

PHONE / TABLET ON THE SAME WI-FI
On the host computer, close any running TEMP server, then run:
  node scripts/start-portable.js --lan
Windows also has Host for Phone or Tablet.cmd.
Open the printed network URL on the phone/tablet. Enable Touchscreen mode on the
title. The host computer stays running. The devices need the same reachable Wi-Fi;
allow the host app through the local-network firewall if your system prompts.
No app, Node.js or files need to be installed on the phone/tablet.

Manual launch helpers keep a terminal open. Close the tab and press Ctrl+C in that
terminal when finished. The dedicated Deck/Linux launcher also handles Exit Game.
Do not open dist/index.html directly; the browser needs the included local server.
Only one copy can use port 5197 at once. URCHIN_PORT can choose another free port.

WHAT TO TEST IN THIS UPDATE
- Confirm TEMP · SEP 24 · CREW & COASTS on the title.
- Neutral, forward and reverse have different engine sounds. Throttle strongly
  increases volume/pitch and visible wake/wash. Surfacing divers whistle, with
  distance reducing volume. Test on the speakers/headphones you normally use.
- Portrait is supported again. Phone defaults shrink the information windows;
  Touchscreen Options groups touch mode, scale (50–150%) and opacity (0–100%).
  Tiny Touch Controls selects 70% controls; UI Scale is separate.
- Arrange UI saves bottom-edge cards, shows visibility and graphic/text choices,
  and asks before discarding unsaved changes. Portrait and landscape keep separate saved layouts.
- Harbour menus pause time. Normal planning starts at 05:00, with a rested 07:00
  alternative. A missed evening offload lands at 06:00 and permits 09:00 departure.
  Sleep advances to the next day. Flashlights permit tiring late/night fishing.
- Crew reach level 20; Base/Trained/Today stats and medical history explain new
  changes. Fatigue builds faster, recovers slower and has stronger effects.
- New portraits, instrument housings, hull silhouette, load bags, chart-only
  minimap, selectable owned clocks and an installed-equipment boat blueprint.
- Six additional difficult maps retain all nine earlier grounds. Expect remote
  deep beds, headland eddies, jet-only gates and rich tide-locked boulder basins.
- More rivals fish shared stock, with visible bubbles/bags. Surfaced whale strikes
  bring fines and DFO attention; rock sea lions can slow divers. Geese/gulls/eagles
  add restrained activity. Test balance over several seasons.
- With a jet, right-stick vertical pivots the stern (tight twin, wider single).
  Left-stick horizontal operates an installed bow thruster. Keyboard overlays
  show your actual mappings; keyboard use in menus selects keyboard mode.
- Easy helps powered reverse escape grounding against wind; Realistic keeps the
  engine-versus-wind struggle. Dry tidal gates still require a rising tide.
- Recheck Raster -> Vector -> Raster and repeated Training/Hide UI transitions.
  Failed boat images retry; exported career JSON includes troubleshooting data.


SAVES AND SHARING
This archive includes no player profiles or careers. Manual-browser saves belong
to that browser at the chosen address. Dedicated Linux saves are in .player-data.
Use Skipper logbook export/import to move an existing career. Keep your own exports.
When sharing a played folder, exclude .player-data and .runtime (private saves/logs).
The archive itself is clean and ready to share. Older TEMP copies remain separate.
MANIFEST.sha256 records every shipped file. licenses/ contains engine notices.

AUTOMATION BOUNDARY
Chromium/Firefox checks and simulated controllers establish software routing.
Physical Windows/macOS/Android/iOS and controller tests remain to be done.
