# Fishing beds and diver portrait brief

Historical September 19 investigation. The inventory and three-map accounting-bed assumptions below describe that earlier build and have since changed. Current approved world/progression and crew design are in [Bible §13](../bible.md#13-career-economy-and-progression) and [§14](../bible.md#14-crew-hiring-shares-and-fatigue). Proposed UI treatments and portrait prompts below remain proposals, not standing instructions or approved canon.

Prepared 2026-09-19. This is an investigation and production brief only. No portrait images were generated, and the fishing-bed control was not removed or redesigned.

## Fishing sub-area control

### What it does

The departure-menu action in `src/expedition-actions.js` cycles the currently viewed sector's saved bed preference through `a → b → c`. Pressing it does not depart or move the boat. The selected ID is passed into the working day when the player chooses **Begin working day**.

The generic fallback names are Bed A/B/C, but the current departure UI resolves them to sector-specific names:

| Sector | A | B | C |
| --- | --- | --- | --- |
| Near | Harbour Flats | Kelp Bowl | North Shelf |
| Middle | Lee Channel | Tidal Saddle | Split Narrows |
| Far | Outer Bowl | Long Shoulder | Needle Edge |

The choice has real economic and ecological consequences. It changes the bed's harvest multiplier, catch price/quality profile, and the separate player/NPC pressure ledger used for depletion and recovery. The chart also describes each bed with a difficulty and hazard summary. Those descriptions help the player choose; they should not be represented as proof that the button itself relocates simulation hazards.

### Why it exists

The control makes each broad sector three persistent biological/economic grounds instead of one static catch pool. It supports learning local ground, choosing risk and earning potential, and distributing fishing pressure. This aligns with the Bible's loop of choosing ground, reading conditions, building knowledge, and deciding whether extra production is worth the risk.

A literal **Fishing sub area: Bed A** label is fallback/stale presentation, not evidence of a dead button. Current source normally shows the sector-specific name, for example **Fishing sub-area: Harbour Flats**.

### Viable player-facing treatments

1. **Recommended low-risk treatment:** keep the cycling action and persistent per-sector preference; label it **Fishing bed: Harbour Flats** (or the corresponding real name). Show its difficulty and hazard summary in the existing chart detail.
2. Replace the cycle with a three-row **Choose fishing bed** panel. Each row can show name, qualitative difficulty, and hazards. Keep exact yield/value numbers behind the appropriate information assists so Realistic play is not omniscient.
3. Make the three beds directly selectable on the chart while retaining the same saved preference and simulation IDs. This is clearest spatially but requires authored bed positions and a larger UI change.

Do not remove the control unless another selector takes ownership of `career.preferences.subAreas[sector]`; otherwise the player loses a meaningful ground choice while the simulation silently falls back to bed A.

## Current portrait inventory and replacement scope

- `public/assets/harbour/frank-v1.png` is the only bitmap person portrait. It belongs to Frank, not the diver roster, and is a quality/lighting reference rather than a replacement target.
- `src/crew-portrait.js` produces one generic inline SVG face. Colour, name, and the DFO badge are its only meaningful variations.
- That SVG is used by authored and seed-generated divers in the harbour Crew cards/detail panel and the in-water portrait-only selector. The DFO skipper uses its officer variant.
- There are currently no diver-specific bitmap assets and no predeclared replacement filenames.
- The first replacement set should cover the eight authored divers below. Seed-generated rival/hireable divers need a reusable, deterministic portrait bank or modular portrait system; assigning one canonical face to every generated name would break seed variability. The DFO officer should remain a separate uniformed target.
- Proposed authored target directory: `public/assets/harbour/divers/`. Proposed files: `ada-chen-v1.png`, `milo-ward-v1.png`, `nell-fraser-v1.png`, `roy-bell-v1.png`, `inez-brooks-v1.png`, `r-robinson-v1.png`, `pat-murphy-v1.png`, and `dave-kaimana-v1.png`.

### Future integration location

After approved assets exist, add a trusted `portraitSrc` field to each authored entry in `src/career-data.js`. Update `portrait(p)` in `src/crew-portrait.js` to render a square image when that field is present and preserve the SVG fallback for old saves, generated divers, and the DFO. Update the SVG-specific selectors in `src/style.css` (notably `.crew-profile svg` and `.crew-card svg`) to address a shared portrait class. Keep the current accessible name and the in-water identity-only test.

## Portrait art direction

These are draft prompts, not established canon. The Bible fixes the cold working-harbour tone, readable presentation, concise personalities, and profile-image purpose, but it does not fix faces, ethnicity, clothing, or most ages. Casting details below are provisional art direction and should be approved before generation.

Use this shared direction for every portrait:

> Square 1:1, chest-up realistic editorial portrait of a working commercial diver in a cold British Columbia/Pacific Northwest harbour. Frank-level facial and material detail; the approved harbour scene's blue-green water, dark timber, evergreen mountains and restrained warm dock light. Authentic worn waterproof workwear and dive gear, natural skin texture, practical grooming, quiet confidence, softly focused working dock background, eye-level 85 mm portrait feel, strong silhouette readable at 64–108 px. No glamour pose, fantasy gear, scuba-resort styling, text, logo, watermark, duplicated equipment, distorted hands, or face-obscuring mask.

### Ada Chen — `ada-chen-v1.png`

> Shared direction. Lean, composed adult diver; rust/copper watch cap and tidy weatherproof layers keyed to #b46e46. Calm evaluating gaze, one glove cuff being checked, equipment neatly secured, squared posture, clean deck habits visible without looking pristine. The portrait should communicate caution, judgement, reliability, and economical movement rather than timidity.

Ability hint: “Checks the ground before committing, keeps the deck tidy, and rarely wastes air. A steady choice when judgement matters.”

### Milo Ward — `milo-ward-v1.png`

> Shared direction. Wiry, energetic younger adult diver; sea-blue bib or drysuit accents keyed to #648c9c, wind-tossed practical hair, regulator hose over one shoulder, forward-leaning posture and an impatient half-smile. Suggest fast bottom movement and eagerness, with well-used gear and a hint that pace sometimes outruns judgement.

Ability hint: “Fast across the bottom and quick to bag, but burns air and may chase a thin patch too long. Best when speed matters more than patience.”

### Nell Fraser — `nell-fraser-v1.png`

> Shared direction. Mature adult diver with a still, observant expression; muted sage cap and workwear keyed to #879262, damp gloves, subtle kelp and sorted urchin crates in the soft background. Patient posture, eyes reading something off-camera near the water. Communicate exceptional awareness, clean product handling, and knowing when to move.

Ability hint: “Patient reef reader with sharp awareness and clean picking. Slow to rush, quick to notice when the good product has moved.”

### Roy Bell — `roy-bell-v1.png`

> Shared direction. Strong, restless adult diver in scuffed ochre workwear keyed to #b48650, broad quick grin, wet gloves, hearing protection hanging at the neck and a compressor softly implied behind. More kinetic framing than the others. Communicate extremely fast bagging, love of dense nearby ground, high air use, and confidence that can become recklessness.

Ability hint: “The fastest bags in harbour and the loudest compressor. Thrives on dense ground near the drop, but gives dive tables an optimistic reading.”

### Inez Brooks — `inez-brooks-v1.png`

> Shared direction. Strong, balanced adult diver in teal-green gear keyed to #609386, one hand controlling a taut dock line, deliberate gaze and planted shoulders despite wind. Damp, authentic channel-work equipment. Communicate current tolerance, route discipline, high awareness, and excellent judgement without making the pose heroic.

Ability hint: “Built for channels: holds position in strong current, keeps a deliberate route, and brings excellent judgement when the water starts moving.”

### R. Robinson — `r-robinson-v1.png`

> Shared direction. Lean, unhurried adult diver in muted mustard layers keyed to #bba260, composed face, carefully coiled regulator and pressure gauge, relaxed shoulders, watching the water rather than the camera. Communicate patience, exceptional air economy and awareness; keep the full first name and gender presentation intentionally unresolved.

Ability hint: “Never hurries and somehow makes the last breath last longer. Exceptional awareness, judgement, and air economy reward patient work.”

### Pat Murphy — `pat-murphy-v1.png`

> Shared direction. Capable adult diver in slate-violet accents keyed to #887da4, wry expression, picker gear close at hand. Three identical, correctly constructed regulator bags sit neatly in the background as a subtle eccentric detail. Communicate very fast picking and strong all-round water skills, with a small suggestion of private superstition.

Ability hint: “An excellent, very fast picker with strong all-round water skills. Carries three identical regulator bags and will not explain why.”

### Dave Kaimana — `dave-kaimana-v1.png`

> Shared direction. Broad-shouldered veteran in his fifties, salt-and-pepper working-harbour appearance, weathered teal-blue bib keyed to #578fa2, calm direct gaze, exceptionally well-maintained but well-used dive gear. A clean premium product crate is softly visible behind. Communicate speed, air efficiency, hard-current confidence, near-flawless judgement, and the dry assurance of someone who once supplied a demanding small restaurant.

Ability hint: “Broad-shouldered veteran in his fifties; quick, air-efficient, calm in hard current, and almost never wrong. A tiny restaurant still asks after him.”

## Blurb implementation

The eight ability hints above are now the authored `bio` strings in `src/career-data.js`. The existing Crew detail UI already displays that field and the strings are static repository content with no markup, so this is safe in the current renderer. They intentionally do not appear in the portrait-only in-water selector.
