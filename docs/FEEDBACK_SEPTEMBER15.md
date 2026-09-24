# September 15 designer feedback

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

Authority: explicit designer amendments to the [Definitive v2 Bible](../archive/design/2026-09-23/Urchin_Skipper_Bible_Definitive_v2.docx), supplied with [September 14 playtest photo](../feedback/9-14.jpg). The conflict with §16’s time-only inspections was reported before implementation. Originals are preserved.

## Decisions

- Replace harbour artwork with the supplied `harbour-training-mode-v1.png`, copied byte-for-byte. Training uses a plain button beside its painted cabinet.
- Remove player-controlled catch care and all sorting gameplay. Each harvested bag has one hidden diver-specific undersize roll, default 1%. Each successful roll represents one undersized urchin. DFO independently detects each at 25%, assessing $1,000 each to the boat at settlement; no crew-share deduction. Rolls survive save/reload. Ten bags have a 9.56% probability of at least one occurrence; five in fifty remains possible but very unlikely. Frank’s only explanation is the requested sentence.
- Keep the guaranteed opening inspection within the season’s first two days, then use a seeded 10% independent daily visit chance, with no missed-day backlog. A completed visit cannot repeat that day.
- DFO waits 100 m clear until invited and all divers are aboard. Direct skipper dialogue, sideways docking and swept hull separation replace the hidden menu hunt. A short transition finishes positioning after a bounded approach, irrespective of shoal depth; this is the expressly authorized temporary inspection exception. The player’s normal grounding model remains intact.
- Boarding takes two additional seconds with or without a bag; bag-only turnaround is unchanged. Weather fades distant bubbles to half opacity for high waves or rain, quarter for both, and zero beyond fog visibility.
- Twin-jet neutral pivot moves to right-stick up/down (up port, down starboard); left-stick sideways remains bow thrust. Single-jet handling is preserved. Keyboard and touch receive corresponding pivot actions.
- Designer confirmed 32 major slots: picking, awareness, fatigue and tank occur five times each; air, current and swimming occur four times each. Ada combines a picking major with air/tank minors, and every diver retains three distinct abilities. Hidden mystery crew remain outside the hireable roster. Audit found 34 visible divers in the old generator (13 rival pairs plus eight contacts); new careers use 12 rival pairs for the requested 32. The two surplus legacy profiles remain readable, and already-hired surplus divers remain in old careers. Existing opponents and experience are preserved.
- Diver orders belong to the person and persist through trips, days, berth changes and reloads. Preserve the existing implementation and add lifecycle regression coverage.
- Sister vessels receive independently varied passage fuel consumption, feeding their existing fuel planning, travel and live engine calculations.
- Rebuild a dated TEMP distribution with local assets and cross-platform manual/LAN hosting, excluding careers, profiles and logs. Retain previous copies.

## Verification

285 tests, lint, formatting and production build pass. Controller, touch, career/voyage and traffic checks pass, including Chromium/Firefox frame budgets. Runtime harbour, scroll, DFO and touch screenshots were inspected. The updated TEMP ZIP has verified contents and serves the same bundle. [Acceptance records and reproduction](history/2026-09-15-feedback/acceptance/README.md).

Physical controller/touchscreen and other-device testing remains the designer’s follow-up; automated input is software coverage only.
