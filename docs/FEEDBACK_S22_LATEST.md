# September 17 · compact information, menus and repeat training

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Designer amendment: the three transcripts in `feedback/` (`Screen_Recording_20260916_163908_Firefox.txt`, `screen-20260917-005745.txt`, `screen-20260917-010101.txt`) plus the explicit request for gradients inside the existing circles, separate diver cards and repeat tutorial training. Originals are preserved. This supersedes affected UI/training decisions in [the preceding correction](FEEDBACK_BOAT_CARD_HARBOUR.md).

## Decisions and implementation

- The existing touch circles show persistent commanded throttle/rudder through directional gradients and arrows. Release still holds commands; the established neutral, steering, bow and jet mappings remain.
- Diver cards are outside the boat card in both input modes. Touch places two short crew cards and a wider boat strip beneath the controls, using the existing bottom clearance without raising the controls. Nitrogen remains a meter with readiness; its percentage and forecast depth are omitted from the compact card. Full boat information remains scrollable/resizable. Turning off diver indicators leaves identity-only portrait selection when that option is enabled.
- Information windows have separate move, close and resize controls. Moves persist per input mode/orientation in this browser; resizing retains the existing per-session behavior. Reset window positions and sizes restores the current layout. Close changes the corresponding saved option. Hide UI only masks the current set and Show UI restores it. Frank's live text is transparent with a shadow for contrast; the tutorial suppresses unrelated windows. New optional controls-reference/recent-message windows start off to avoid duplicating touch controls.
- **UI / difficulty options** groups ordinary panels first and information/handling assists below. Each option has a separate ON/OFF control and explanation; narrow screens place the explanation next to the selected option. Easy, Realistic, All Off and a restorable Custom preset are explicit. Realistic uses portrait selection instead of underwater indicators; the career's existing difficulty ceiling still protects hidden assistance. UI options remain configurable in either career difficulty.
- Live Current is a separate panel, so disabling the boat card does not hide its arrow, speed and bearing. Weather and fitted electronics share their own independently hideable group.
- Text/UI scale now includes 50–150%. Touch control scale is a separate saved 70–150% preference. At enlarged control sizes, narrow screens wrap the gear buttons to keep all actions reachable.
- Charts opened directly at sea return to the water with Back; charts reached through menus retain their immediate parent. Orders gains the same top-left Back control as radio history and the other menus.
- Boat selection starts with no selected card and an explicit “Pick a boat first” prompt. Details and purchase controls activate only after a selection; payment still starts on Cancel.
- Clicking a keyboard-diagram key opens a scrollable action picker. Close changes nothing; assignment uses the existing conflict checks and preserves the other device. This does not guess physical controller/Deck layouts.

## Training authority and preservation

The latest explicit request replaces the player-facing developer arcade described in Bible §21. This conflict was reported before implementation and treated as the designer's subsequent amendment. The dock, title and Settings now lead to **Training Mode**, repeating Frank's existing cove tutorial. A practice copy of the active boat first offers boat handling, bow thruster/twin-jet lessons when fitted, one lesson per purchased equipment item, and night practice when lights/flashlights are fitted. Continue advances the preparatory instruction; ordinary tutorial steps retain their gameplay progression and skip controls. The same cove remains the practice area.

Training saves the real career before entry, works on a clone, and restores the original world on exit. Practice money, stock, health and charts cannot overwrite real saves. A reload restores the real saved career. The internal developer fixtures remain for regressions; Test Mode and Prototype Lab are removed from the normal title flow. The approved §23 harbour composition is unchanged.

## Verification and exports

Focused acceptance: `npm run verify -- --browsers-only --suite=s22-latest` and `--suite=s22-latest-firefox`, plus applicable HUD, shop, keyboard and controller checks. `tests/s22-latest.test.js` covers career isolation, equipment/night preparation, preset restoration and save migration. Final results and screenshots are recorded in [acceptance](history/2026-09-17-small-screen-training/acceptance/README.md).

Additive recipe: `python3 scripts/package-temp.py --output exports/2026-09-17-small-screen-training`. Both usual TEMP packages contain the same built game and exclude player profiles. Older exports, feedback media, transcripts, documents and authoring assets remain preserved. Physical Samsung S22/tablet/controller checks and the actual itch.io upload remain user playtests.
