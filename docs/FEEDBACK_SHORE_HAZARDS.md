# Shoreline hazards — September 17 designer amendment

The designer requested more logs and hittable shoreline rocks, a massive increase in logs at night and in fog, fixed features across 1–5 m depths, and selective chart coverage with clearly visible uncharted hazards. The designer explicitly clarified that **1–5 m means surrounding seabed depths, with rocks rising near the surface**.

This extends the definitive DOCX §§3/17 world and visibility rules: obvious uncharted crowns are an explicit visibility amendment. It supersedes the earlier once-only doubling of night logs in [itch feedback](FEEDBACK_ITCH_TEMP.md). Plain shallow-bottom grounding remains harmless; rock/timber strikes use the existing impact-damage system. The orthographic camera and original bathymetry, decorative coastline, fishing patches, stock and day-zero lesson remain intact.

## Implemented decisions

- Each 600 m working sector has 40 deterministic fixed features: eight in each rounded 1–5 m seabed band, all in the actual 1–5 m range and within 50 m of exposed datum shoreline. Rocks and elongated outcrops share geometry between simulation, water presentation and charts. Their positions remain the same across days, sector visits and reloads.
- Thirty features appear as pink crosses on local working/departure/tidal charts. Labels show **clearance over the top at chart datum**, with “dries” for exposed tops; add the current tide to obtain clearance. Selecting a charted rock reports its surrounding seabed depth too. Ten uncharted features have larger, brighter crowns and stronger pale wash, retained in Easy/Realistic/All Off within the existing weather/light visibility range. Floating logs remain uncharted.
- Every sector starts with 72 logs, at least three quarters deliberately coastal. Night adds 360 (432 total); fog adds 288 (360 total); encountering both gives 720. These independent cohorts spawn only once per sector visit and survive save/reload. They remain and drift when visibility improves, rather than disappearing beside the player. The existing occasional runoff/event logs may add further timber.
- New timber spawns at least 45 m from the boat and 20 m from deployed divers, in water with space between logs. Legacy logs remain where saved; one safe coastal addition upgrades old visits. World-edge drift is bounded. Existing careers gain fixed features deterministically; a rock overlapping a legacy boat gets clearance grace until the boat has left it.
- Rocks block swept hull/drive motion and remain fixed. Bow impacts affect the hull; exposed stern impacts can also damage propulsion. Gentle contact and sufficient tidal clearance cause no damage, and backing away is allowed. Continuous contact does not repeatedly roll damage. Local sounder/scanner measurements detect a top only beneath their sample footprint. Other-boat water routes account for fixed rocks.
- The known-good USB Xbox mapping is untouched. Browser fixtures stage positions/weather and exercise real menu and renderer paths; they do not establish physical controller behavior.

## Verification and export recipe

Focused and complete simulation regressions cover all sectors/depth bands, preservation, selective charts, visibility, huge but bounded weather cohorts, spawn safety, old/new saves, impacts, escape, tidal clearance, soundings and traffic clearance. Run `npm run verify -- --unit-only`; rendered acceptance uses `npm run verify -- --browsers-only --suite=shore-hazards` and `--suite=shore-hazards-firefox`. Existing phone and controller journeys remain available.

Build recipe: `npm run build`, then `python3 scripts/package-temp.py --output exports/2026-09-17-shoreline-hazards`. The packager adds a new folder and verifies every build byte in both ZIPs, retaining older exports and excluding careers/profiles. Title: “TEMP · SEP 17 · SHORELINE HAZARDS”. Final screenshots, checks and fingerprints: [acceptance record](history/2026-09-17-shoreline-hazards/acceptance/README.md).
