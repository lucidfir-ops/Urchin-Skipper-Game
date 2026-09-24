# September 15 follow-up: itch.io TEMP

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Authority: the designer's follow-up feedback accompanying [the DFO photo](../feedback/9-15.jpg), amending the [Definitive v2 Bible](../archive/design/2026-09-23/Urchin_Skipper_Bible_Definitive_v2.docx). This supersedes the affected behavior in [the earlier September 15 pass](FEEDBACK_SEPTEMBER15.md). No new video was present with this report; the written navigation report and supplied photo were actionable.

## Decisions and implementation

- Harbour: retain the supplied scene and Training Mode cabinet. Put the nine actions into three aligned rows so the existing directional focus system has simple paths. From Sail: up to crew, up again to Weather & tides; from crew: right to Your boats. Training remains next to the painted arcade at lower right.
- DFO: an explicit 1.4 simulation-second casting-off transition follows inspection. Deployment stays blocked until release. Under that transition the patrol moves to clear navigable water, drops docking mode, takes a water route and drives away at patrol speed. If no navigable exit exists (including an entirely dry test fixture), the transition completes its exit. Fines are finalized once before casting off; saves during departure resume without a second fine. Older physical inspections still complete.
- World pace: one browser preference scales the fixed-step simulation accumulator, default +25%, adjustable from +0% to +100% in Settings (slider and controller buttons). Clock, bag work, movement, exposure, fatigue, traffic, fuel and recovery all advance together. Individual picking weights and simulation-time constants remain unchanged. At +25%, 40 simulation seconds take 32 wall-clock seconds. Menus still pause. Training speed is an additional multiplier.
- Open-water scouting: alternate ±45° legs every seven simulation seconds around the instructed direction. On sloping coastal bottom, bias the course along the contour. At 5 m turn deeper; at 20 m turn shallower and hold the correction for seven seconds to prevent boundary jitter. Awareness and direct movement to visible worthwhile ground remain intact; local movement within an existing patch retains its harvesting rules.
- Ground recipe v6 adds 26 unmarked patches to each sector, for 13 marked + 52 unmarked. At least 75% of the additions are within 90 m of dry shoreline; near/far add 20 coastal and six offshore grounds, while the narrow middle sector's additions are all coastal. New elongated grounds follow the local depth contour. Existing reef IDs, positions, stock and chart history are preserved on migration.
- Touch: a transparent target follows the boat sprite. Dragging toward bow/stern adjusts throttle and port/starboard adjusts rudder, relative to the heading at gesture start. Release holds both commands; tap resets both to zero. Existing sticks and physical mappings remain available. Menu, cancellation, blur and rotation clear held touch sources. A previously omitted continuous-scene forwarding entry for Centre rudder was corrected too.
- Picking vocabulary: Very fast / Fast / Slow / Very slow replaces Fast / Good / Mediocre (the reported “bad” tier) / Slow. Rates, colors, quality labels and original prototype fixture names stay unchanged.
- Night starts at 19:30 (ends at 06:00). Unlit deploying/searching/harvesting divers immediately start their normal warned ascent. New descent requires the **Diver flashlights** upgrade. No flashlight upgrade existed in the build, so the routine tuning choice is $450 for both divers, fitted to the active boat. Deck/working lights remain a separate upgrade.
- Fatigue: underwater work accrues twice as fast at night. First four game hours of underwater work accrue at half the former rate; hours four to eight use the former rate; subsequent work uses 1.5×. Skills still apply. Finishing short days therefore leaves materially less fatigue; overnight/rest recovery and early-start costs remain.
- Darkness adds enough logs to double the existing daytime field, once per generated sector field. New logs avoid the boat and surfaced/underwater crew when placed. Logs persist through saves without multiplying again.
- Working lights retain port recovery illumination and add a visible forward cone that clears part of the darkness veil. Camera and simulation geometry remain unchanged.
- Boatshop: controller focus / mouse hover / keyboard focus previews the highlighted hull. Activating it opens a confirmation with the exact hull and price. Cancel is initially selected. Confirmation purchases only that recorded hull; failure leaves the dialog open with the reason.
- Weather & tides retains the current-day detail and adds seven seeded daily outlooks. Timing estimates become less certain further ahead; the forecast equipment still helps. Preview does not advance or mutate the world.
- Fullscreen: an explicit button is visible whenever touch mode is enabled, including title and menus. It invokes the browser fullscreen API and handles unsupported or disallowed views with a readable fallback. Native mobile/iOS behavior remains a physical-device check.

## Packaging

Recommended upload: `exports/2026-09-15-itch/UrchinSkipper-TEMP-ITCHIO.zip`. Its `index.html` is at the archive root; all production assets use relative URLs. It contains the static game and license notices, with no host runtime, player data or profiles. `START-HERE-ITCH-IO.txt` specifies the upload and fullscreen options. The title and `BUILD.txt` identify this TEMP edition.

The optional `Urchin Skipper TEMP.zip` in the same dated folder contains the exact same build plus Windows/Mac/Linux/Deck and LAN helpers. The local/LAN host still needs Node.js 22+. Previous versions are retained.

## Designer verification received

Confirmed YES: supplied harbour/arcade and Training Mode; right-stick scrolling in all three sail plans and visible departure remedy; DFO portrait, 100 m wait and invitation/docking (with the separate overlap/stuck-departure report now addressed); recovery/boarding timing; independent twin-jet pivot and bow thrust; supplied title/boat/chart artwork and training entrance.

Touch was only checked for startup and visible buttons. Physical other-device play, shallow pickup, recall, renewed orders checks and unmarked items in the supplied checklist remain unverified by the designer. The favorable chart/logbook paper treatment is retained.

## Verification

Focused regressions and browser acceptance are recorded in [the acceptance folder](history/2026-09-15-itch/acceptance/README.md). Local checks do not establish actual itch.io publication, physical device performance or controller feel.
