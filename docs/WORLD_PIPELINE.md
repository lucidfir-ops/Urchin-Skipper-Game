# Game-ready sectors and future world data

## Current boundary

`world-source/sectors.js` is the source recipe for three **invented** 600 m sectors. `scripts/generate-sectors.js` runs offline and writes `src/generated/sectors.json`. The original 500 m basin remains in `src/world-data.json` for focused regression/practice fixtures. Gameplay loads saved data; Phaser never runs a GIS parser or regenerates terrain.

Run `node scripts/generate-sectors.js` after editing recipes. `tests/sectors.test.js` independently regenerates and hashes all exports, checks complete stock/rate/quality matrices, wet drops and field dimensions. New sessions clone mutable stock; revisiting a sector retains its own depletion.

## Export schema v2

- Sector identity: stable ID, display name, travel minutes, schematic chart position, harbour-facing boundary and safe entry.
- Terrain: square extent in metres, grid spacing, row-major finite depth values. Positive depths are **below datum**; negative values are drying/land elevation. Current grids have their own resolution.
- Coordinates: x east, y south, local metre units, origin and vertical-datum description. Synthetic data has no real-world origin. Future data must supply explicit projection/EPSG, geographic bounds, origin and datum conversion metadata.
- Provenance: source recipe and seed, source list, synthetic/imported classification, `notForNavigation: true`. Future source entries need publisher, dataset/version/date, URL, licence/attribution, raw filename and SHA-256. Do not silently combine unknown vertical datums.
- Patches: stable ID, synthetic origin, polygon outline, bounding radius, starting stock, independent picking rate and quality, drop position, derived features and suitability. The diagnostic matrix is intentionally authored test content; habitat patches are seeded from terrain suitability. No real fishery locations. Each stocked region exports nine locally depleting clumps with their own IDs, positions, radii and conserved stock. Runtime harvest updates clump and region totals together; the larger outline is a chart marking.
- Current field: interleaved flood x/y, ebb x/y, residual x/y, and local lag minutes. Runtime bilinear sampling blends separate time curves. Flood and ebb geography need not be exact negatives.
- Environment: independent tide-height and signed-current curves. Both can use harmonic components or timestamped samples. Their phases are independent. Wind/waves remain lightweight existing influences.

## Future offline processing

Raw immutable GIS/bathymetry → crop → normalize projection/local coordinates → validate vertical datum → mask/clean/interpolate gaps → resample → derive slope/curvature/shelves/bowls/reef shoulders → substrate/current/lee/bend features → habitat suitability → seeded synthetic patches → current basis fields → validate/compress/export.

Interpolation must retain a source/coverage/confidence mask. Do not turn missing bathymetry into zero depth or pretend coarse NONNA cells are high-resolution multibeam. Keep raw observations, processing recipes and derived products separate. Large rasters/meshes belong offline; a later compressed/binary export can replace today's JSON behind the same sector loader and sampling API.

The provisional habitat module accepts depth, slope, curvature, shelf, bowl, shoulder, hardness (including unknown), shelter, current, channel-edge and inside-bend features. Existing coefficients are synthetic placeholders awaiting the designer's ecological knowledge. Authored channel/shelter hints can later be replaced by GIS-derived geometry and calibrated observations.

## Runtime authorities

`terrain.js` owns bilinear bed depth, gradient and depth = bed + authoritative sea-level offset. Sounder, hull constraints, diver deployment/search, surface drift, kelp, charts and reef/coast drawing use it. The raster renderer refreshes after roughly 5 cm of tide change to avoid rebuilding its texture each tick; physical depth queries remain continuous.

`environment.js` updates height/current state from the day clock and samples local currents. No moving entity should read a global vector directly except explicit uniform test fixtures. Boat propulsion is water-relative; divers/floats/foam sample their own positions. Foam stops at shore; it does not disappear and respawn to fake a convergence.

`simulation.js` is fixed-step, has no DOM or hardware reads and accepts abstract helm/diver actions. The presentation resolves displayed action hints using the same nearest-eligible target resolver and saved input labels. Explicit entity IDs can pin a queued command; selection is retained for orders. Future touchscreen controls should emit these same commands, then add large targets, throttle/rudder affordances, compass orders and pinch zoom in a separate view. Ship a local/offline web bundle later; this pass does not claim a finished Doogee/PWA package.

Future NPCs should own independent kinematic/Matter bodies and sample the same terrain/current/time services. AIS may inform aggregate route/density priors, not identifiable vessel playback. Water taxi behavior, diver collisions, horn responses and flag visibility remain future design work. There is no NPC or networking runtime yet. Stable sector/entity IDs, seeded content, explicit commands and simulation time form a useful base for later authority/snapshots; do not promise lockstep determinism across Matter/browser versions.

## Future geography-to-art direction (designer, September 10 overnight pass)

Investigate real coastal geography plus appropriately licensed aerial/satellite/map references as the physical skeleton and visual guide for detailed overhead 2D sector artwork. Crop/projection/datum cleanup belongs offline. Derive game terrain and synthetic habitat from the authoritative data; produce layered textures or tiles that align with that terrain rather than a huge scene whose painted shoreline secretly defines physics. Coastlines and drying reefs must still respond to the authoritative tide. Keep imagery/data provenance and licence permissions alongside raw sources, retain originals, and verify derivative-use rights before ingestion. No real imagery or GIS was ingested during this pass; current sectors remain entirely synthetic.
