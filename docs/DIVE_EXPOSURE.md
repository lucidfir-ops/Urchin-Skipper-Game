# Dive exposure — game abstraction

Historical technical rationale. Current approved exposure rules and calibration are consolidated in [Bible §9](../bible.md#9-bag-timing-air-exposure-and-surface-behavior). References to amendments and supersession below describe the implementation history; this document is not a separate design authority.

September 14 designer amendment; Bible §9. This module is **not a dive computer, US Navy table implementation, medical prediction or real dive-planning tool**. It intentionally uses fictional accelerated game budgets. Do not use its numbers to plan a dive or infer fitness to dive.

The qualitative premise—depth/time exposure, repetitive and consecutive-day diving, surface intervals and individual variation—is informed by the [CDC diving-injury overview](https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/scuba-diving-decompression-illness-and-other-dive-related-injuries.html) and [DAN overview](https://dan.org/health-medicine/health-resources/diseases-conditions/decompression-illness-what-is-it-and-what-is-the-treatment/). These sources do **not** validate the fictional calibration below. The latest request for simplified tables supersedes the Bible's initial accurate-US-Navy-model suggestion.

The subsequent [touchscreen and fishing amendment](FEEDBACK_TOUCH_AND_DIVING.md) supersedes the original numerical calibration below: longer depth/air budgets, shorter surface half-life, full-bag readiness, visible nitrogen load and Nitrox.

## Implementation decision

`dive-exposure.js` owns one bounded record per career person: short exposure load, slower repeated-day strain, accumulated hazard, deterministic injury threshold, consecutive days, today's bottom time and clock. Terrain supplies actual depth. Roughly 20-foot water permits most of a working day; deeper grounds force increasingly frequent breaks. Conservative divers stop earlier; ordinary divers adhere to a higher limit; Roy and one seeded opponent can ignore tables. The traits and random threshold are hidden from normal menus. Their behavior and surface requests communicate personality.

Air reserve remains a separate, safe automatic ascent. New tanks, bags, boarding, hires and reloads never clear exposure. Surface intervals recover load; slow strain carries into following days. Rest and skipped transit/day time recover through the same function. Held training clocks still accrue simulated exposure; holding a clock is not immunity.

Symptoms are assessed at surfacing, once per crossed threshold. Suspected DCS ends the player's fishing, allows recovery and medical return/rescue, and records a five-game-day injury absence. This is a game consequence, **not a medical recovery recommendation**. Existing collision injuries, deaths and historical consequences remain intact. Save validation rejects malformed exposure without reconstructing a world during autosave.

No exact hazard percentages or trait labels are exposed during ordinary play. The portrait-only selector remains identity-only; full diver info now shows the fictional nitrogen meter and readiness at a stated depth. Test Mode may deliberately reset or manipulate fictional exposure; it cannot change the real career.
