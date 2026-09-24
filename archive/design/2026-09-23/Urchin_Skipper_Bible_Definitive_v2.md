<!--
Agent-readable retrieval mirror of Urchin_Skipper_Bible_Definitive_v2.docx.
The DOCX remains the sole authoritative design document.
-->

# URCHIN SKIPPER BIBLE

**Definitive full-game vision — Phaser 4 / Matter.js — Steam Deck-targeted 2D browser game**

## 1. Purpose and Authority

Give the coding AI an immutable core description of the game. This document exists to prevent unrequested changes to decided systems. It is the authoritative full-game vision.

Current-build bugs and playtest findings belong in a separate implementation list. If requested feedback implementation contravenes this guide, do not make the change; report the conflict so this document or the request can be changed.

Treat this document as the authoritative player-facing vision, not as a demand to implement every system simultaneously.

Checkpoints are no longer saved as they were ballooning in size exponentially. The export folder of temp and itch.io ready versions serves as the sole backup of previous versions.

The pdf version of this document is in archive as an historical reference, this docx is now the living source of truth.

## 2. Core Vision and Intended Experience

The player is the skipper of a small commercial sea-urchin dive boat. The player controls the boat and gives high-level instructions; solo SCUBA divers operate autonomously underwater. The game is about skipper skill, not manually controlling divers.

**Core loop:** Prepare at harbour → inspect forecast/tides/current → choose boat, crew, equipment and ground → travel → search using chart, depth sounder and knowledge → deploy divers → read bubbles/floats → maneuver and recover → accumulate catch → decide whether to move, continue or return → meet the offload deadline → sell/offload → pay costs and crew → compare results → repair, hire, upgrade and plan the next day.

The intended feel is a chaotic but believable working-boat operation, not an urchin-collecting arcade game. A good day should generate stories from interacting systems rather than scripted missions. The goal is a game where becoming better means genuinely learning to skipper the operation: reading ground and conditions, handling different boats, knowing crew, managing risk, building useful knowledge and deciding when the extra bag is worth it.

## 3. Camera, Presentation, Art and Audio

Gameplay uses a rigid orthographic bird's-eye/top-down camera. The camera follows the boat and can zoom from a close view where the boat fills the screen to a large-area view. There is no normal free-pan strategy camera.

Visuals should become attractive and atmospheric while preserving readability of boats, floats, bubbles, kelp, reefs, wake, weather and deck load. The working deck and accumulating bags remain visually important. Kelp, wind, wake, waves, spray, rain and other environmental effects should also serve as usable information about current, boat movement and wind speed.

A diver is a simple black figure on deck and next to the float on the surface. Underwater, the diver is not visible; only bubbles show location. Navigational, tidal and weather charts are accessible through menus.

Provide proper title, launcher and Steam artwork. Audio communicates engine state, throttle/jet behavior, wind, waves, recoveries, impacts, radio/crew cues and environmental danger without overwhelming the player.

## 4. World, Coastline, Bathymetry and Grounding

Use deterministic authoritative world data shared by rendering, the depth sounder, diver AI, current and grounding. Ideally, include some real locations.

Coastlines need varied bathymetry: beaches/gentle shelves, normal slopes, steep slopes, reefs, rocks and occasional cliff-like shores where several metres of water can exist immediately beside land. A meaningful coastal/archipelago area can be of a size that will be defined through testing. Roughly 0–10 m depth gets a visible shallow-water/terrain gradient; deeper water may look similar.

The depth sounder reports only depth directly beneath the boat; it does not magically reveal surrounding terrain. For the rudder boat, grounding begins at about 2 m depth, tunable. 1m for jet boats. Grounding severely constrains movement rather than causing damage. If deeper water is astern, the boat can reverse off at about 0.5 m/s. Full tidal stranding/refloating is future work.

Persistent chart knowledge is part of the full game: explored reefs, depths, useful ground and player marks can persist, with better charting/scanning equipment improving what can be recorded.

## 5. Fishing Grounds and Hidden Productivity

Good urchin ground emerges from believable terrain and hidden productivity fields/patches rather than individual simulated urchins. Good red-urchin patches should favor flat bottoms and gentle slopes, low-current areas or channels between islands, and shoreline-adjacent ground. They should not be deeper than 70 ft, should avoid very high current, and should avoid dead zones unless they are at the end of a current die-off.

Urchin patches should not simply be circles dotted on the map. Prefer long curved edge-rectangles or sausage-like shapes that follow adjacent shoreline. Ground data can contain density, quality, depth, terrain, patch direction and patch size. Patchs might hold roughly 1,000–4,000 lb.

The player should learn which grounds are productive without receiving omniscient information. For testing, the authoritative patch/grid/field should include deliberately obvious good, mediocre/poor and empty patches. Easy/debug can reveal them; Realistic cannot show magical productivity. Use Phaser Tilemaps only if they actually simplify implementation.

## 6. Boats and Boat Handling

~~***Working commercial dive-boat hulls vary in size. Hull size affects weather capability, fuel use, deck capacity and wind effect.***~~

~~***Variable propulsion can include prop with rudder, outboard, leg, jet, one or two engines, and bow thruster. These affect minimum depth, maneuverability, speed and fuel use.***~~

~~***Boats are upgradeable, including upgrades that affect information provided or gameplay.***~~

~~***Keep major boat properties configurable: mass, acceleration, max speed, reverse speed, steering response, rudder effectiveness, bow-thruster strength, draft, wave tolerance, windage and fuel behavior.***~~

The boat has momentum. Steering is not instant. Wind, waves and current move it, so approaching a diver requires anticipation.

Hydrodynamic behavior should use velocity through water = boat world velocity minus local current velocity. Resolve this into longitudinal and lateral components, with much stronger lateral resistance. Prefer Matter forces/corrections over blindly overwriting velocity every tick. Expose coefficients for tuning.

Preserve the current controller as a good base and improve it conservatively. Widen the high-speed turning circle. The rudder boat should require thrust to steer, but also have reduced steering at the top end and in reverse. Twin engine steers better than single. Leg and outboard and jet steer very well. Jet can also, controls fantastically in reverse and can spin in a very small circle if twin engine or a small circle if dual. Bow thrusters add great maneuverability.

## 7. Wind, Current, Waves and Weather

Wind, current and waves are separate authoritative variables and may have different directions. Wind pushes the boat, with the cabin most affected, so model the push point accordingly by hull. Surface current pushes both the boat and surfaced diver/float. Waves affect pitch/roll and handling. The boat produces a visible wake. Rough water affects handling and visibility and makes bubbles smaller. Use low-cost believable approximations, not fluid dynamics.

Strong channels should reach roughly 3–5 knots where appropriate. A boat that does 10 knots full ahead should do 14 knots with a 5-knot current and 6 knots against it. Divers can effectively hold position in modest current, roughly up to 2 knots as an initial feel target. As an initial calibration, 3 knots of current might produce about 1 knot of net diver drift.

Strong current can sweep a diver off a small patch before a bag is filled. Once useful ground is lost, normal search/surface/air logic determines the outcome. A diver might enter at slack and later be swept away as current builds.

Weather includes calm periods, rain, squalls, storms, fog, wind shifts, rough seas, lightning and rare rogue-wave events. Conditions should affect decisions, visibility and handling rather than being cosmetic. Forecasting tools provide imperfect but useful information. Better equipment/experience can improve detail or confidence without perfect foreknowledge.

Current must be obvious enough to matter during pickup. Boat and surfaced diver/float read the same authoritative current. Environmental cues can include kelp direction, drifting material or flow around fixed objects. Easy/debug also gets a toggleable current/tide overlay with arrows. Full tide-cycle simulation is not required yet.

## 8. Divers: Core Rules, AI and Instructions

Divers are autonomous solo SCUBA agents; there is no underwater player control. This is a permanent design decision, not a placeholder for a tender/hookah model. Two divers start on deck. They are selectable and receive high-level instructions through a preset menu rather than free text.

Instructions can include minimum allowed quality, compass search direction, maximum scouting time and maximum bag time. Minimum acceptable quality presets are Any / 60% / 70% / 80% / 90%.

Searching and harvesting are separate states. Approximate diver awareness begins around 30 ft / 9 m, tunable. Search direction biases movement but does not override worthwhile nearby ground. As an acceptance target, a patch about 25 ft behind the instructed direction can be seen and chosen; a patch about 50 ft behind is unseen and should be missed. Bag-fill timing begins only when worthwhile ground is reached and harvesting starts. Do not add A\* unless real obstacle/pathfinding needs emerge.

When a diver's current patch is exhausted, the diver surfaces immediately whether the bag is full, partial or empty, rather than autonomously moving to a new patch. “Surface when patch exhausted” is inherent behavior, not a separate instruction. If productive ground remains after a normal bag turnaround, issue a fresh bag and let the diver continue/re-descend. Never blindly return them to exhausted ground.

A partially filled bag slows underwater movement/search; the exact penalty is tunable. Divers can be hit without consequence at slow speeds, defined elsewhere, and can be injured or killed above those speeds. Divers have stats that improve with experience, including swim speed, boarding speed, maximum workable current and scouting visibility.

Divers work according to US Navy tables. This means they can dive nearly the whole day at 20ft, but will require breaks if diving at 70ft. This can be modelled accurately at first and altered if not fun. Divers can have hidden behaviour like more or less conservative adherence to tables, and will have increasing risk of injury: the bends, increasing with number of days dived consecutively where bottom time was maxed out or surpassed, and one or two divers might randomly have the hidden quality to totally ignore the tables, massively increasing their bends risk if dived in deep locations a lot.

## 9. Bag Timing, Air and Surface Behavior

Time advances continuously but is accelerated. Initial calibration: 30 seconds of game time represents about 15 minutes of real-world bag time. Exceptional ~10-minute real bag: ~20 game seconds; great ~15-minute bag: ~30 seconds; acceptable ~20-minute bag: ~40 seconds; poor ~30-minute bag: ~60 seconds. All timing values are configurable. Fishing time and pickup/recovery time are separate; the bag-time clock stops when the diver surfaces.

Normal full-bag target is approximately 300 lb. Partial bags arise naturally from air, patch exhaustion, current displacement or other legitimate interruptions. A roughly 150 lb bag is valid only as a legitimate partial bag.

Each deployment carries a simple air-time budget. It is a forced-surface trigger, not a survival or injury mechanic. Initial calibration is 100 units of air. A diver may continue searching/fishing until 20 units remain, then must surface automatically regardless of bag state; this overrides normal patch-exhaustion behavior. No death, injury or emergency state is attached to running low on air; it simply forces a surface. Air values are configurable/tunable.

Divers must also surface after a definable scouting period if they do not find a patch, so they do not use a whole tank searching. The default is 70 seconds. Better hireable divers can default to 15 seconds. If the player changes scouting time, remember the new default for that specific diver.

Down diver: bubbles only, very visible close to the boat and progressively fainter at distance. Ascent: sparse → dense bubbles → orange float appears, with roughly 5 seconds of pre-surface warning. Surface diver: orange float always stays attached to/with the diver while waiting. Distance-opacity falloff is not a priority; zoom already reduces apparent bubble size at distance.

## 10. Recovery and Deck Work

Recovery is a boat-handling task. Position the working side close enough to the diver/float/bag. Prefer a realistic working-side recovery sector of approximately 120° on the port side where appropriate, rather than a full interaction circle. Initial pickup distance target is about 5 m in Easy and 3 m in Realistic; values are tunable.

Bag turnaround and ending a diver's operation are distinct actions. Bag-only recovery can keep a productive diver working; diver+bag recovery ends or moves that operation. Recovery requires low relative speed; an earlier calibration is less than 1.5 knots relative to the diver.

Keep a short bag hook/preparation phase of roughly 3 seconds. Earlier recovery timing is 2 seconds ±1 second for a bag and 1 second ±0.5 seconds for a diver. Catch appears physically on deck and affects exact load. Assists may widen tolerances or clarify valid actions; realistic settings demand accurate maneuvering. If the diver gets on the boat, their state resets so they can be redeployed with a fresh bag.

## 11. Deck and Loading

Urchin bags are visibly stacked on the working deck and accumulate as catch is recovered. The simulation has an exact load value even when the UI hides it. Easy shows exact load, remaining capacity and detailed loading UI. Realistic has no exact weight readout; the physical deck is the primary load information. Visual bag placement and numerical loading must be separate systems so one can be tuned without breaking the other.

## 12. Day, Travel, Chart and Offload

The player chooses a ground/drop location. Manual travel to it is abstracted, but travel distance determines the fishing time available that day. The offload deadline is 7:00 PM. Example calibration: grounds about 3 hours away require departure by 4:00 PM; grounds about 1 hour away allow fishing until 6:00 PM. The full travel-time-to-deadline mapping is configurable/tunable rather than hard-coded to these examples.

Skippers must manually drive to the map edge to leave the area and are penalised on a sliding scale for late offloads.

## 13. Career, Economy and Progression

The career is driven primarily by money, assets, reputation/experience and access rather than an abstract arcade score. Revenue comes from landed catch and market conditions. Costs can include fuel, crew shares/wages, maintenance, repairs, equipment, boat purchases and useful simplified fees/insurance.

Economic failure is the principal long-term fail state. There need not be an arbitrary Game Over after a bad day, but the player can make themselves unable to continue—for example by destroying a newly purchased boat and absorbing a severe loss.

Avoid tedious accounting. Financial detail belongs where it creates decisions: risk an expensive boat, hire a better diver, repair now or work, choose a distant ground, upgrade electronics, etc. Prices, costs and progression pacing are tunable balance data. Track useful career records such as best load, best revenue day, average catch, boat history, days worked and incidents.

## 14. Crew, Hiring and Shares

Divers become hireable individuals with differing ability, share/wage expectations, reliability, experience and traits. Better divers become available once certain goals are reached.

Hireable divers should differ through understandable behavior: search judgement, harvest rate, air efficiency, current tolerance/resistance, reliability, experience, fatigue/injury recovery, personality, swim speed and bag speed. Prefer visible behavioral differences over opaque percentage bonuses. It would be nice to have stat sheets with profile images.

Crew economics should evoke commercial fishing. Astra may design a clear first-pass share/wage model rather than asking the user to specify every percentage. Great crew should create attachment and difficult choices. Availability can be affected by injury, other work, conflict or personal events without becoming a soap-opera simulator.

Crew events may include fatigue, disputes, requests, exceptional performance, mistakes, sickness/injury recovery, scheduling conflicts and rare memorable incidents. Personality should mostly emerge through concise bios, radio/harbour dialogue and events rather than long cutscenes.

## 15. Injury, Safety and Consequences

The game includes diver injury and serious consequences. Safety creates decisions, not gore or arbitrary punishment. Risk can rise with poor weather, dangerous recoveries, exhaustion, collisions, inadequate equipment, bad judgement or exceptional events.

Injuries can reduce/remove crew availability and create financial or operational consequences. Catastrophic outcomes should be rare, legible and connected to meaningful risk. Boat damage ranges from inconvenience and repair to catastrophic loss according to impact and circumstances.

## 16. Other Boats, Rivals and Inspections

Other skippers/boats occasionally spawn on grounds and fish a random area. Their fishing activity directly impacts the grounds they use. Daily offload/results can show rival catches, giving context for whether the player's day was poor, average or exceptional.

Rivals can develop recognizable tendencies, boats, favorite areas and reputations. Rival boats are unique assets labelled rival1, rival2, etc., assigned at random to competition fleets. Boats receive random maneuverability/speed profiles; divers receive random ability/experience. Divers can be poached, and the player's divers may leave for rival boats. Track boats, performance and diver access. Some boats/divers are loyal and never change crew; others are interchangeable.

Create Shai hull wood as a mystery boat and crew hidden from player-facing information, with locked-in loyal and hidden divers Paul and Worm and skipper Jessy Bean.

Taxi boats spawn randomly off screen, choose a route and drive it. Routes should go through an urchin patch. If the player is working that patch they can attempt to block the taxi; it moves to avoid the player's boat but does not avoid diver bubbles. If a diver surfaces and is hit, injury/death follows existing calculations. Spawn frequency, routes and encounter frequency must be adjustable. Taxi sprites are labelled taxi1, taxi2, etc. and travel at 30 knots.

DFO is another random spawn that circles the map. If it sees player or AI fishing boats, it approaches and stays 100 m away. The player cannot deploy a diver until both divers are up, then DFO boards. For now this is simply a time cost. Asset: dfoboat1. Stop time, spawn frequency and routes must be adjustable. DFO uses a 25-knot boat.

## 17. Events, Easter Eggs and Rare Weirdness

Natural and operational events include storms, squalls, fog, rogue waves, debris, equipment/engine problems, wildlife, other vessels, inspections and crew events. Events should intersect with current plans. Avoid event spam; ordinary productive work must remain satisfying so unusual days stay memorable.

Include restrained references to maritime games, diving culture, science fiction and project history without directly reproducing copyrighted characters or assets. References may appear as subtly referential crew/boat names, props, radio lines, achievements and extremely rare unexplained events.

Canonical internal joke: a vessel named Shy Hull Wood whose skipper may speak reverently of “urchin sign the likes of which God has never seen.” Very rare unexplained events may include enormous transient sonar returns, distant lights, strange radio calls, abandoned objects or impossible one-frame readings. Not everything should be explained. Easter eggs are seasoning; Urchin Skipper must not become a collage of references.

## 18. Easy, Realistic and HUD Information

RB toggles information overlay options; options can be checked on/off individually. Easy preset is all on. Environment and diver-underwater options are not selectable in Realistic mode.

Easy/high-information visual cues on grounds can include current direction/speed arrows, delineated areas with dots representing urchins, line colour showing speed, and solid/dashed line spacing showing quality. UI groups can include environmental information (wind/current speed and direction, wave height), boat information (speed, heading, throttle, steering), and diver information (names, fatigue, current bag fill, on boat/in water, searching/picking).

The UI must be modular and compartmentalised into relevant information clusters rather than several large text boxes. These clusters must fluidly change according to the toggle list. UI must not drive simulation.

Easy can identify diver positions/states, cycle/select across the two divers with a clear current-target highlight, and show a directional arrow after roughly 15 seconds when a relevant diver is off-screen. Realistic requires the player to remember deployment locations and visually find bubbles/floats; there is no arrow or selection aid.

Easy can show exact load and clearer underwater/hazard visibility. Realistic uses the physical deck as primary load information, much darker underwater visibility, and hazardous reefs barely visible within roughly 100 ft. Simulation remains identical in both modes.

Easy HUD can show time/day and offload countdown, wind, current, waves, visibility, boat speed/heading/fuel, loading/capacity, deck/catch, selected-ground information, diver locations/states, depth sounder, chart/minimap and quick actions. Realistic removes information a skipper could not reasonably know. Do not turn the game into an omniscient dashboard.

## 19. Default Controls

~~***RB: toggle UI options.***~~

~~***LB: next diver.***~~

~~***RT / LT: zoom in / zoom out.***~~

~~***Diver on boat: Y deploy diver.***~~

~~***Diver on surface with bag: Y ***~~recover diver and bag.

~~***Diver on surface with bag: X take bag.***~~

~~***Diver on surface with no bag***~~: X give bag.

~~***Diver on boat: B open instructions menu.***~~

~~***Diver underwater: ***~~press ~~***A to tell diver to surface; must be within 5 m of bubbles, takes 2–5 seconds to begin surfacing, accompanied by loud clanging sounds.***~~

~~***Right analogue: steering left/right.***~~

~~***Left analogue: throttle up/down, bow thruster left/right. Do not engage one while engaging the other.***~~

~~***D-pad up: full ahead. D-pad down: full reverse. D-pad left or right: neutral / 0% throttle.***~~

UI must always show the currently valid action. Always double-check that updates have not affected this default control scheme.

## 20. Technical Architecture and Rendering Rules

Use a modular Phaser 4 project targeting Phaser 4.2.1, with Matter.js where appropriate. Do not make a giant monolithic file, but do not build an elaborate framework for its own sake.

Modules include application/bootstrap; scene/camera; input mapper; boat simulation/controller; water/environment; wind/current/waves; diver simulation/AI; fishing-ground data/search; catch/bag/loading; recovery interaction; depth sounder; chart/ground selection; day-timer/session; UI/HUD; Easy/Realistic information layer; audio/effects; config/debug tools.

Keyboard and gamepad resolve to the same abstract game commands. A single authoritative world-state module holds depth/terrain, reefs and wind/current; seabed renderer, depth sounder and diver AI read from this one source. Keep content/tuning data separate from simulation logic. Easy/Realistic are information/presentation layers over the same world state. UI must not drive simulation.

Standard Phaser game objects/primitives and basic/canvas textures are acceptable for boats, deck, terrain and prototype visuals. Simple particle systems are acceptable for bubbles and wake. No complex custom GLSL/shader pipeline or premium rendering asset/shader packages are required or expected for the prototype.

Before writing generic systems, check Phaser/Matter built-ins and official examples first for input/gamepad, camera/zoom, particles, Clock/timers, tweens, scenes, audio and sensors. Keep dependencies few. Reuse external code only under a compatible license with required notices preserved; prefer permissive MIT/BSD/Apache sources, do not copy unlicensed code, and avoid GPL/AGPL unless those obligations are deliberately accepted.

Boat-physics conceptual references: Aaron Vanderpoel, “Simple Top-Down 2D Boat Physics for Games” (directional/keel drag and tracking), and Habrador/Unity-Boat-physics-Tutorial (MIT) for hydrodynamic force concepts. These references guide behavior; they do not mandate copying code or architecture.

## 21. Developer and Training Tools

The arcade machine on dock allows access to this mode.

Provide developer tools to toggle Easy/Realistic, spawn/reposition divers, force surface/underwater/surfacing states, set bag weight/fullness, set remaining air, set ground productivity/quality, set wind/current/waves, reveal hidden seabed information for testing, pause/single-step if practical, show hidden physics markers, reset the prototype, change time scale/day timer, and expose major tuning values.

Also allow adding/removing money, buying any boat and upgrade, and unlocking/levelling/delevelling any diver. This should be accessible to future players through a training arcade cabinet image on the dock labelled “training mode”.

Add an in-play Easy/Realistic/debug-information toggle so hidden grounds, current and other simulation truth can be inspected without restarting. Debug reveal is for validation and does not automatically define the final Easy-mode UI.

## 22. Design and Development Rules for Astra

~~***The ocean should create difficulty naturally; avoid arbitrary +20% difficulty modifiers.***~~

~~***Player upgrades should preferably change perception or physical capability rather than invisible percentage bonuses.***~~

~~***Realistic mode should reward learning and observation. Do not give the player information they could not reasonably know.***~~

~~***Do not simulate detail just because it is realistic; simulate it when it creates an interesting decision.***~~

~~***Keep major gameplay values configurable.***~~

~~***One world state, multiple systems reading it.***~~

~~***Use artistic licence. Make ordinary game-design, UX, tuning and engineering decisions autonomously. Do not escalate minor numerical choices to the user.***~~

~~***Build interconnected systems rather than isolated feature boxes. Economy, crew, weather, rivals, equipment, injuries and information should create compound decisions.***~~

~~***Choose a sensible dependency order, build in playable vertical slices, integrate and test each slice, then continue autonomously.***~~

~~***Preserve working systems and avoid gratuitous rewrites. Reuse existing architecture where practical.***~~

~~***Test what you build and fix reasonable errors before reporting. If one feature is blocked, continue useful independent work.***~~

~~***Keep simulation truth separate from presentation. Easy/Realistic/Custom are information/assistance layers over the same world wherever practical.***~~

~~***When uncertain, favor fun, legibility, believable commercial-boat behavior and meaningful decisions over maximal simulation detail.***~~

~~***Treat this document as the north star for iterative development and use playtesting to refine implementation.***~~

~~***Prioritize actually building, testing and improving the game over explaining what you are doing. Keep responses concise and do not narrate routine steps or internal reasoning.***~~

~~***Do not repeatedly ask for confirmation when the design document already provides enough information. When a detail is unspecified, make the simplest robust implementation decision consistent with this document and record the assumption.***~~

~~***Batch related implementation work. Prefer simple, robust implementations over unnecessary architectural complexity. Diagnose and attempt reasonable fixes before asking for direction.***~~

~~***Maintain consistent architecture and preserve agreed design decisions unless explicitly changed. Do not spend tokens explaining code unless explanation is requested.***~~

~~***Build in playable vertical slices where practical: establish a working core loop early, then expand it. Adjust implementation order when doing so clearly reduces rework or enables testing.***~~

~~***When reporting progress, summarize only completed work, tests performed, blockers/assumptions and the next useful step. If the next step is obvious and does not require user input, proceed without asking permission.***~~

~~***Maximize useful development work per token while keeping the implementation complete, testable and maintainable.***~~

## 23. Finalised image references

Where the author of this document feels that a part of the game is in good status and should be maintained as is, without alteration, screenshots will be stored here.

Harbour Screen. When it looked like this, the buttons were the most functional, and the buttons were in the most relevant places for the image. Settings should be top right, talk to frank should be bottom left, and chandlery should be centre left.

![Embedded document reference](Urchin_Skipper_Bible_Definitive_v2.assets/image1.png)

...
