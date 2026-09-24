# Selective design directions and inspiration

Historical notes from the designer's September 10, 2026 playtest. These are not active design instructions, a fallback specification or an implementation queue. See the [current design authority](../PROJECT_STATUS.md#design-authority); retrieve these notes only for relevant history.

## The physical experience

**Physically fight wind/current and maneuver the boat to recover divers.** Boat position, drift matching, exposure, obstacles and crew safety are the central gameplay problem. Do not replace that with a haul button, minigame and abstract result. Keep the confirmed difference between through-water speed and speed over ground, useful low ahead power, and working port-side recovery.

## Future modular boats

Eventually hull size, engines, outboards, sterndrives, single/twin jets, bow/stern thrusters and unusual combinations should produce discernible handling, performance, operating-cost and repair differences. A vessel relying heavily on thrusters rather than conventional main propulsion is a valid future experiment. Physical/visual customization should correspond to those mechanical differences.

The six prototype packages were considered sufficient at the time. Data-defined hull/drive properties and abstract commands provided a modest foundation for the v1.7 career/economy expansion; see [historical implementation decisions](V17_DEVELOPMENT.md). A full construction editor or replacement propulsion engine was not a prerequisite. Major jet drive replacement/repair was provisionally about 72 hours. Packages could be changed before departure; mid-day fitting was considered unnecessary.

## Future presentation strategy

Continue the **rigid orthographic 2D prototype** as the gameplay laboratory. Once gameplay/system design is substantially mature and proven, investigate rebuilding or presenting it in 3D or an angled 3D perspective. Keep simulation state and geometry independent of decorative assets. Do not implement two renderers/engines or sacrifice the current prototype for that possibility.

Real geography → detailed overhead coastal artwork is a separate future experiment. Prefer lawful open geographic sources, retain physical data authority and keep synthetic fishing resources separate. The offline import/export direction is recorded in [world architecture](WORLD_PIPELINE.md).

## Inspiration, not cloning or immediate tasks

| Reference | Designer's interest |
| --- | --- |
| DREDGE | Strong presentation and atmosphere. |
| In the Same Boat | Relevant boat/game presentation ideas. |
| Ship Shaper | Modular construction ideas, at a complexity well beyond this game's needs. |
| NavalArt / Warship Craft | Modular vessel construction concepts. |
| Professional Ship Simulator | Impressive vessel presentation and accuracy. |
| Seafarer: The Ship Sim | Vessel/game presentation reference. |
| Ship Simulator Extremes | Vessel/game presentation reference. |
| Ships at Sea | Vessel/game presentation reference. |
| SeaOrama | Vessel/game presentation reference. |
| Sailwind | Especially wind behavior. |
| Windrose | Visual beauty. |
| Fishing Inc | Fishing/boat visual inspiration. |
| Fishing: Barents Sea | Potentially useful reference; avoid making Urchin Skipper predominantly a management abstraction. |

These are the designer's reference notes, not independently researched evaluations. No assets, code or protected maps are sourced from them.
