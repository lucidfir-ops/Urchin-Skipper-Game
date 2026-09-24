# September 16 — clear water view and adjustable information windows

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Designer amendment: add a small touchscreen button that hides most UI, including Frank’s lesson, because step 7 obscures the divers. Make text windows scrollable, including the helm information outside menus, and allow resizing. Produce both new TEMP editions.

## Decisions and behavior

- **Hide UI / Show UI** sits below Fullscreen during touchscreen play. It hides Frank, lesson callouts, helm/diver cards, clock, pickup information, instruments, navigation information and other informational overlays. Sailing/action controls, Menu, Fullscreen and an active DFO radio interaction remain available. Menus still open normally. The visibility choice is temporary for this running page; reopening the UI shows the current lesson and readings, without changing assists, tutorial progress or the simulation.
- Gameplay information windows accept native swipe, wheel and focused keyboard scrolling. Helm/diver content no longer shrinks or ignores pointer gestures, and pickup details previously suppressed on touch can be reached by scrolling. Existing menu scrolling remains available.
- Corner grips resize the helm/diver window, Frank, pickup information, clock, instruments, navigation, help, ground information, test information and action feedback. Drag the grip; double-tap it to restore the default size. A focused grip also accepts arrow keys and Home. Resizing and scrolling never issue bound helm commands.
- Sizes last for the page session, separately for portrait/landscape and touch/desktop. Returning from a menu preserves size and scroll. Rotation cancels an in-progress resize; window size stays within the viewport. Reload restores automatic sizing and visible UI. Live updates keep the scroll container and captured resize control intact.

## Authority and scope

Compatible with definitive Bible §§1, 3 and 18: this implements the explicit designer presentation amendment while keeping the orthographic camera, physical floats/bubbles, recovery geometry, assists and simulation intact. It extends the existing modular information groups. The [previous Frank presentation](FEEDBACK_FRANK_TRAVEL_NAVIGATION.md) remains available whenever the UI is shown.

## Implementation and reproduction

`src/hud-windows.js` owns the stable resize controls; `src/hud-windows.css` contains scrolling, bounds and corner anchoring. The existing 10 Hz HUD refresh places the controls. `touch-controls.js` owns the transient visibility toggle. `keyboard-controls.js` gives focused window navigation keys to scrolling/resizing.

Run `npm run verify -- --unit-only`, then browser suites `hud-windows`, `hud-windows-firefox`, `controller` and `keyboard-feedback`. The new browser flow covers tutorial step 7, live scrolling, corner dragging, menu round trips, hidden-view steering, both phone orientations, 150% helm text and desktop keyboard ownership. Chromium also sends native touch gestures; Firefox uses touch taps and native wheel/mouse dragging. These checks do not establish physical phone or controller behavior.

After verification, build additive packages with `python3 scripts/package-temp.py --output exports/2026-09-16-ui-windows`. Title identity: **TEMP · SEP 16 · UI WINDOWS UPDATE**. Both editions contain identical game bytes. Previous TEMP editions, profiles, careers and checkpoints remain preserved.

[Acceptance evidence](history/2026-09-16-ui-windows/acceptance/README.md).
