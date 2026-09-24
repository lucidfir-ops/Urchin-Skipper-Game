# September 16 — boat card, approved harbour and title scrolling

Designer amendment: restore the separate boat information card while retaining Hide UI / Show UI and Frank's scrollable, resizable tutorial. Keep the harbour composition added to definitive DOCX §23, with Settings at top right, Talk to Frank at bottom left and Chandlery at centre left. On the Samsung S22, scroll title options inside their card without moving the backdrop. References: [four screenshots and approved harbour](../feedback/9-16/), and the embedded image in the [sole authoritative DOCX](../Urchin_Skipper_Bible_Definitive_v2.docx).

## Decisions

- Restore the existing helm/diver card during touch tutorials, including throttle, rudder, speed, heading, depth, fuel, condition and diver readings. At small landscape sizes it sits to the left of the boat and Frank sits to the right; in portrait the cards stack above the boat. Both keep independent scrolling/resizing and obey Hide UI / Show UI. Assist preferences and simulation are unchanged.
- Restore the approved full-screen harbour artwork, inset translucent heading and three-by-three button arrangement, applying only the three requested relocations. Compact phones pan the complete composition with its buttons. Preserve current Boatyard/shop functionality and Back/Forward navigation.
- The title backdrop fills the viewport; only the bounded options card scrolls. Card bounds account for the saved UI scale and mobile bottom clearance.
- The designer moved the PDF to `archive/`; it is historical. The DOCX remains the only design authority. §23's approved harbour reference is protected against future unsolicited redesign.
- The designer deleted checkpoints because of growth and designated exports as playable version preservation. Stop routine checkpoint creation; preserve additive exports and all original authoring inputs. Exports contain the playable release, not a complete source/document backup. The former checkpoint script included all accumulated exports in every new archive, duplicating their contents.

## Reproduction

Run `npm run verify -- --unit-only`, then the `s22-title`, `hud-windows`, `harbour-shops` browser suites and their `-firefox` counterparts. `controller` covers synthetic pad routing/menu reachability. Native Chromium gestures verify that the title card scrolls while the backdrop stays at the viewport origin, and that HUD hiding/resizing still works. Inspect runtime screenshots in both phone orientations and the 1280×800 harbour against the DOCX reference. Physical S22 and USB Xbox testing remains a separate designer check.

Additive packages: `python3 scripts/package-temp.py --output exports/2026-09-16-boat-card-harbour`. Title identity: **TEMP · SEP 16 · BOAT CARD & HARBOUR FIX**.

[Acceptance evidence and export fingerprints](history/2026-09-16-boat-card-harbour/acceptance/README.md).
