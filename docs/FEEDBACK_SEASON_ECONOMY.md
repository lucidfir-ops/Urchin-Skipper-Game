# Nine-day season and coastal progression

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

This note records the September 19, 2026 designer amendment for season/economy progression. The Definitive v2 Bible remains authoritative for the general fishery, stock, rival, injury and career systems; it does not assign numeric season, area-access or diver-contact values. The explicit request therefore supplies the nine-day structure, and the values below are reversible balance tuning.

## Player-facing progression

- A1 resolves the hierarchy as **three coasts, each with three physical subareas**. The earlier three-map/nine-accounting-bed implementation is superseded. All nine destinations have separate exported depth grids, current fields, terrain, stock and chart knowledge.

| Coast / access | Day 1 subarea | Day 3 subarea | Day 5 subarea |
| --- | --- | --- | --- |
| Home Coast / included | Sheltered Kelp (`near`) | South Reef (`middle`) | Outer Ledge (`far`) |
| Stormbreak Coast / $12,000 / hard | Stormbreak Channel | Gale Sound | Broken Cape |
| Frontier Coast / $30,000 / extremely hard | Blackwater Reach | Wreck Teeth | Last Light Bank |

- A season lasts nine days. The original 1/3/5 opening schedule applies within each coast, independently of the permanent coast permit. This is the explicit implementation interpretation of A1/A2; no additional waiting season or boat ownership gate is introduced.
- Sail shows all nine destinations and clearly says **Area not open**, with the opening day and/or permit price. Accounts sells one permanent permit for all three maps on the selected coast; Cancel and repeat purchase cannot charge. Both later permits total $42,000.
- Existing `near`/`middle`/`far` physical map IDs, bathymetry, stock, chart observations and active trips remain in Home Coast. Legacy paid middle/far access becomes Stormbreak/Frontier access respectively. Saves from before permits retain both later coasts. Migration never charges, refunds or replenishes stock.
- Both starter boats cost $15,000 and leave $5,000 working cash.
- The old **Fishing sub-area: Bed A** button only selected accounting/price/pressure records on the same map. It now opens the real coast/subarea chooser. Legacy accounting slots and their saved preferences remain readable to preserve old catches and pressure history; they are not additional playable places.
- New physical maps have 65 career patches each, with 30% / 60% more initial stock than their own unscaled recipe, and +0.03 / +0.06 raw quality. Standard price multipliers are 1.32 / 1.64, reflecting lower competition; inherited Home Coast catch profiles stay compatible. These are tunable fictional multipliers.
- New current fields have stronger channels, local shelter/eddies and an additional 210-minute component (amplitude 0.12 / 0.22). The existing 5-kn current cap stays in force; difficulty also comes from more extensive races and variation. Wind is 1.32× / 1.64× with stronger gusts and changing bearing. Swell increases independently; rain is not forced by wind. Each new map retains navigable sheltered working pockets.
- Fixed rocks increase from 40 to 55 / 70; uncharted rocks increase from 10 to 35 / 50. New entrances and a route to working ground are tested at -0.4 m tide for a 2 m draft and 5 m clearance radius. Original maps are unchanged.

## Earnings verification and tuning decision

The original claim that two opening trips would reliably fund the next area was only an assumption. A2 now has a repeatable three-season economic assessment in `scripts/progression-balance.js`: three seeds, both starters, and cautious/competent/aggressive strategies, plus clean expert, repeated-home-ground, boat-first and credit scenarios (22 runs / 594 career days).

Assumed target catches are 1,500 / 3,300 / 7,000 lb, limited by boat capacity, available working time and actual clump stock. Search skill is an explicit scenario input. Work is limited by the real weather-sensitive travel/return window; 25% working throttle estimates fuel. Crew work/fatigue, stock removal, rival catch, market/quality/age losses, 40% crew shares, insurance, licensing, interest, repair purchases, medical absence and rollover use production functions. Every trip saves/reloads and checks settlement and permit idempotence. Setback runs include quarter-catch days, 6% hull / 10% drive damage, and recorded diver injuries with subsequent absence/premium increases. They retain a cash reserve and rest for fatigue/availability. These runs do **not** operate the helm, model search success, or prove survivable diving in extreme water; the assumed 55% bottom-time duty cycle is not a validated dive schedule.

| Scenario | Coast two purchase day | Coast three purchase day |
| --- | --- | --- |
| Cautious, either starter, setbacks | 7–10 in four runs; not reached in two | Not reached within three seasons |
| Competent, either starter, setbacks | 4–10 | 12–18 |
| Aggressive Workhorse, setbacks | 2–3 | 6–8 |
| Aggressive Island Tender, setbacks | 4 | 13–15 |
| Baseline expert Workhorse, no scripted setbacks | 3 | 7 |
| Baseline aggressive, Coastal Workhorse before Frontier | 3 | 15 (boat purchased day 11 for $52,000) |
| Baseline competent, $5,000 borrowed | 3 | 11 (debt retained; interest charged) |

Retain the $12,000 / $30,000 costs: competent results support earning coast two, while Frontier competes with equipment and boats. Larger Workhorse capacity enables the modeled first-season push; it is an expert possibility, not a guaranteed winning route. The Tender's faster travel does not erase its 3,000 lb deck limit. Rank-one contacts became available on days 3–9 in the baseline scenarios; rank-two contacts remain gated by combined records and are not guaranteed by a permit. The rank-two daily-load gate is reduced from 3,200 to 2,800 lb: the former exceeded the Tender's capacity and unintentionally made a boat upgrade compulsory. All other combined requirements remain unchanged.

The fixed-ground sensitivity case fell from 9,717 lb in season one to 102 lb in season two and 2,201 lb in season three. This deliberately severe result measures repeating the same five patches, not exhausting an entire coast. Cautious runs that stalled below their permit-plus-reserve target can scout the other 60 patches per map, lower their reserve, work ashore, or use financing. Wider patch rotation and enjoyable long-term recovery rates still need human playtesting. All baseline scenarios stayed solvent; this does not promise recovery from arbitrary catastrophic play.

## Stock and rivals

The shorter season no longer doubles survivors every boundary. Survivor growth is 1.35 plus 0.4% recolonization per nine-day rollover. Logical sustainable pressure is 5,500 / 8,000 / 11,000 weighted pounds per bed for near / middle / far. Player pressure weights fall from 1.0 to 0.8 to 0.6; rival weights fall from 0.30 to 0.24 to 0.18, so exposed grounds have slower long-term attrition.

Existing rival rosters and identities remain. In fair weather some experienced teams venture to Stormbreak and only an occasional offshore team to Frontier; rough weather brings those teams back to Home Coast. A 90-day deterministic check verifies decreasing visits across the three coasts. New maps use middle/far pressure weights and sustainable rates above; ambient presence is 55% / 40%, below Home Coast's 70%. Only physical rivals remove stock in the player's map; aggregate rivals work elsewhere without replaying catch after reload.

## Diver contacts

Rank-one and rank-two contacts now require a combined operating record: average crew return, total pounds, best daily load, best net day, total sales, safe days, a sufficiently long working day, and controlled fatigue on that long day. Rank-one goals are 5,000 lb total, 1,400 lb best load, $2,500 best net, $8,000 sales, three safe days and a six-hour day at no more than 72% fatigue. Rank two requires 15,000 lb, 2,800 lb, $6,500, $30,000, six safe days and an eight-hour day at no more than 62% fatigue.

## Safety report

The end-of-day report now names every safety incident, cause, time, injury/fatality outcome, expected availability, and the insurance consequence. A clean day explicitly reports no injury or direct safety charge.
