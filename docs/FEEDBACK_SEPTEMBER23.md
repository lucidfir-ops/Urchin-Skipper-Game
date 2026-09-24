# September 23 touch and portrait amendment

The designer requests a local TEMP itch.io ZIP, superseding earlier GitHub requests. Local additive exports are the delivery workflow. No GitHub work or publication is part of this pass.

The latest request explicitly replaces Tiny UI mode with adjustable Tiny Touch Controls, groups touch settings, adds control opacity, repairs portrait/fullscreen and harbour header sizing, and asks for a tablet assessment and gameplay recommendations. These are presentation/implementation changes under the DOCX §§3, 18, 20 and the explicit amendment to the Settings reference in §23. The authoritative DOCX and approved harbour artwork remain untouched. Recommendations are proposals, not amendments or implemented gameplay changes.

## Feedback review

Reviewed both recordings in `feedback/9-23/` across their complete timelines using timestamped frame sequences and local audio transcripts; inspected all five screenshots. Original media is preserved, with hashes in the release history.

- Phone recording (1:43): 0:00–0:12 landscape persists despite physical rotation described in narration; the 0:12 fullscreen tap precedes portrait at 0:15. Later rotation works. 0:57–1:30 demonstrates shrinking UI Scale making the harbour header cover its top button row, then reset reducing it.
- Tablet recording (3:42): portrait helm use, diver deployment, bags, zoom changes, and landscape around 2:36. Narration explicitly questions whether the sound creates some of the choppy impression. This is not a frame-rate benchmark.
- `Screenshot_20260922_223737_Firefox.jpg` is the phone arrangement reference: instruments across the top, chart/load/current below, boat in the centre, action buttons above the two sticks and diver cards below. Saved user layouts retain priority. Additional enabled information windows remain available.

## Decisions and implementation

- **Touchscreen Options** opens from title, Settings and Pause, including Frank's lesson and the prototype. Back returns to its opener. Title options do not advance or replace the career.
- **Tiny Touch Controls Mode** selects 70%; controls scale is adjustable 50–150% in 5-point increments. Below 100% is Tiny; toggling it off restores 100%. Existing valid touch-scale preferences remain. Sliders and controller buttons share the same settings.
- **Controls opacity** supports 0–100% in single percentage points, with 5-point controller adjustments. It changes action/gear buttons and both sticks. Menu/help and information windows retain visibility. A preview and reset are provided. The touch-specific Adjust UI and Show information controls also live here, with their on-water shortcuts retained.
- Retire Tiny's UI multiplier and separate active Tiny layouts. Its old preference and saved rectangles remain stored for old exports; ordinary saved portrait/landscape arrangements are preserved. UI Scale stays independent.
- Reattempt orientation unlock after page/focus/visibility/viewport/fullscreen events and touch gestures; a bounded delayed retry covers late host launch. No forced portrait/landscape lock. OS/browser/host restrictions still apply. Optional logging records viewport/fullscreen/orientation transitions.
- Harbour header uses content height and local 44-pixel navigation buttons rather than inverse menu scaling. Preserve the approved harbour composition, button locations and panning. Portrait defaults place load/current below the instrument row and keep default action prompts clear of the measured helm area; saved placements are not overwritten.
- Engine audio pitch no longer resets every engine loop on every frame. Quantize pitch to 0.01, limit meaningful audible-loop updates to 20 Hz, and stop redundant gain changes at their target. Preserve procedural sounds, gear distinctions, simulation and handling. The opt-in troubleshooting log now includes frame/CPU phases, renderer, viewport and audio context details every five seconds.

## Reports and acceptance

- [Tablet assessment](DOOGEE_TAB_E3_MAX_REPORT_2026-09-23.txt)
- [Gameplay recommendations for designer review](GAMEPLAY_RECOMMENDATIONS_2026-09-23.txt)
- [Verification and release history](history/2026-09-23-touch-and-portrait/README.md)
- [Physical playtest checklist](../PLAYTEST_GUIDE.md)
