# Historical v1.7 implementation decisions

Historical record only. This document is no longer a design authority or fallback specification; see the [current design authority](../PROJECT_STATUS.md#design-authority). The entries below retain implementation history from before adoption of the definitive v2 Bible.

The bug-fix milestone was finished first: `checkpoints/latest-playtest-fixes-verified-20260911T050155Z.tar.gz` (restoration verified). [Bug decisions and verification](history/2026-09-11-latest-fixes/DECISIONS.md).

## Integrated slices

1. **A livelihood:** saved working days, persistent vessel condition/fuel, different hull capacities/dimensions, named crew with shares and behavioral differences, landing accounts, injuries, contacts/progression, boat/equipment purchases, financing, and a controller harbour office. Default launch becomes career; `?prototype=1` and `?practice=1` retain the mechanics laboratory and its meaningful regressions.
2. **Read the coast:** shoreline-following career grounds, persistent observed knowledge, actual equipment capabilities, weather/forecasts/night, travel/range/load tradeoffs, and configurable information assists. The normal fishery is not the old laboratory matrix.
3. **A working fleet:** rival harvest/results and tips, simplified fishery preparation/inspections, crew/natural events, rare restrained references, title/art/audio, and complete multi-day playtests. These use the same economics/environment/stock rather than separate minigames.

## State and accounting

- `world` remains authoritative during a trip. `career-state.js` contains business actions/settlement; `career-data.js` contains tunable fictional CAD prices, fleet, crew, equipment and contact thresholds. `crew.js` composes individual behavior with fatigue. No difficulty preset changes those physical coefficients.
- `career-save.js` serializes a versioned, checksummed snapshot. Terrain/current exports are reconstructed from deterministic data; resource ledgers, diver IDs/state and selected clump IDs restore references to the actual live patches. Primary and verified previous saves remain separate; failed writes do not erase the last good save. Original human sources and assets remain untouched.
- Fuel is purchased when bunkering. Consumed fuel is an operating-cost line in the receipt, but is not deducted from cash a second time at offload. Superseded by the [September 11 feedback decisions](FEEDBACK_IMPLEMENTATION.md): each diver earns 40% of their own landed catch value, with no daily guarantee. Insurance is paid once at departure; repairs are quotes until purchased. Income/crew/fees/interest/insurance settlement happens once per trip ID. Cash movement and operating return are distinct named result fields.
- Each owned boat retains its condition, fuel and equipment. Changing boats cannot repair the one left behind. Total loss removes physical use; a covered claim replaces part of its value. Crew injury/fatality survives day advancement and reload. Dock work advances a full day and pays a small wage; it is a slow recovery option, not free instantaneous money.
- The starter hull keeps its confirmed physical behavior. Career fleet dimensions/capacity/mass extend the existing boat spec; hull contact, log/crew collisions and recovery use that same spec. Prototype default parameters remain unchanged.
- Natural-scale fisheries, current/weather and prices are invented gameplay data. No real fishing coordinates or regulatory claim is represented. DFO content will be a small fictional ruleset, not legal advice or a reproduction of regulations.

## Content restraint

Divers have original procedural portrait illustrations and short working biographies. R. Robinson and Dave Kaimana are light references in names/background, with no copied character artwork. The canonical Shy Hull Wood vessel/radio line belongs to rare fleet content. Unexplained events should be extremely rare and have no impossible simulation effects disguised as real readings.

## Verified milestones

- Livelihood slice: 147/147 automated tests; build; controller-only harbour → hire → buy equipment → actual autonomous harvest/recovery → offload → next day → browser reload/save restoration. Screenshots inspected at both target layouts. Full environmental/equipment behavior and non-laboratory career grounds are the next slice; installed equipment records already persist.

## Coast, instruments and weather

- New careers use ground recipe version 2: twelve elongated contour-following reefs per area, 2,000–3,000 lb each, on suitable depth/slope bands and away from dead water or the strongest persistent flow. The exported seabed and coastal/kelp artwork remain unchanged. Career arrival is at the sector entrance. Older saves without this recipe flag retain their original grounds; future ground changes need another version.
- Tide/current time continues across career days. Almanac preview samples that same epoch without advancing the working day. Wind, wave height, visibility and darkness come from a deterministic daily weather plan. Forecast timing is deliberately coarse and uncertain; the receiver improves that information. Passage time uses hull speed, load and sea conditions, with its fuel deducted from the same tank as local running. Local career burn now uses the compressed working clock instead of the prototype fuel coefficient.
- Plotters retain observed depth tracks; crew reports record sampled quality and the visit day, never omniscient remaining stock. Manual controller marks persist independently of equipment. Radar samples actual surface debris; a forward scanner measures a narrow fan of bottom depth. Lights restore unlit night pickup reach, a hauler shortens bag preparation, and stabilizers reduce wave yaw. The physical boat, collision hull, deck decoration and recovery footprint scale together.
- Easy, Realistic and Custom presets live in the career save. Information toggles are independent; none changes stock, prices, currents or crew skill. Realistic hides ground outlines/dots and unsurveyed chart shading while preserving local sounder, visible shallow reef/kelp cues, bubbles/floats and purchased instruments. Menus pause the simulation, including weather and inspection clocks.

- Coast/equipment slice verified with 153 automated tests, production build and extended controller career browser flow. The first screenshot review caught new screen classes being removed by the generic panel toggle on unchanged frames; all career screen types now keep their menu layout and background-HUD suppression.

## Working fleet, catch care and consequences

- Three named working skippers have distinct preferred areas and daily plans. Their abstract operations harvest the exact live/saved reef clumps using the same stock deduction helper as divers. A paused game pauses their progress. Offload commits the rest of the day's fleet results once; those reports appear at the next harbour office. No rival catch is invented after a reef is depleted.
- Recruitment restores a bounded 1.8% of original clump stock per lay/working day, never above its original ceiling. This is a tunable abstraction for accessible stock, not a biological growth claim. Reports retain their visit day because a remembered ground can be depleted or recover. Long career balance still needs human playtesting.
- Careful picking adds a 2.5-second check at each bag's first productive work and excludes small product. Quick picking skips it; crew judgement and fatigue determine a small retained fraction. At-sea deck sorting requires both divers aboard, takes real simulation time and prevents new deployment; helm control remains available. Sorting/removal conserves bag/deck/discarded totals.
- An occasional fictional DFO call asks for recovered divers and low relative speed before boarding. Inspection time advances normally at sea; an outstanding call can instead add time at harbour and miss offload. A trip's licence status and retained small catch determine a simple assessment. Checks, fines, removals and records are idempotent across save/reload. No real legal guidance is implied.
- At most one optional sea/crew event is considered per day, usually none. Rough-water events add an actual drift impulse and nearby floating timber; they do not directly reduce hull health. An already damaged drive may cough briefly; a tired aboard crew member may request a short warm-up. Otherwise occasional wildlife provides quiet context. Rare radio content uses the referenced Shy Hull Wood line, with no forced impossible physics.
- Original vector title/library artwork has reproducible SVG/PNG exports. Procedural radio cues and wind/sea mixing extend the existing sound system. Underwater divers remain bubbles only, and the orthographic boat-following view is preserved.

## Career durability and navigation

- The logbook exports a checksummed JSON backup. Starting another career first archives the current valid save; archived careers are controller-selectable and restoring one archives the career being left. A failed save/archive leaves the current career in place. Exported saves can be kept in `data/careers/` so project checkpoints include them. Browser-profile localStorage is now protected player data, not disposable runtime output.
- New-day/new-career transitions clear navigation history before entering the harbour. Back cannot reopen yesterday's receipt with a new world's empty result. Session Ended saves before offering Back, saved-trip Retry, Launcher/title and actual Exit; failed saving is reported.
- A full navigation/harvest/recovery/return pilot pass succeeded with no vessel or crew damage and an on-time 300 lb landing. It uses real helm commands and authoritative physics, with no teleports, synthetic catch, weather changes or bypass of the harbour boundary. Separate controller suites cover the player input/menu layer.

- A delayed offload can push the following departure past 08:00; next-day setup uses actual shipping time plus a short turnover, and harbour waiting cannot be undone with Early start. Exported backups can be imported via the browser file picker; this advanced file operation is separate from the controller-only working loop.

- Integrated first pass verified: 161 automated tests, production build, career/controller/save/import/archive flow, complete rendered natural voyage, and all preserved keyboard, prototype, environment, feedback/startup, overnight and isolated controller/launcher suites pass. The final checkpoint label is `v17-full-game-first-pass-verified`. Balance across many working days and physical Game Mode routing remain playtest priorities; see [current status](../PROJECT_STATUS.md).
