import { clamp } from './math.js';

// Game-scale hydrodynamic loads, in hull axes (metres, seconds). A stern
// appendage stabilizes a shaft boat; a leg has less area and a jet has none.
// Forces use water-relative motion, so a boat carried with uniform water has
// no perpetual rudder force. Wind is applied independently by boat.js.
export function waterLoads(spec, forward, lateral, turn, rudder) {
  const appendage = spec.jetCount ? 0 : spec.vectorDrive ? 0.18 : 1;
  const exposure = spec.environmentResponse ?? 1;
  const bow = spec.length * 0.3;
  const stern = -spec.length * 0.43;
  const bowSide =
    -lateral *
    (0.8 + Math.abs(forward) * 0.55) *
    exposure *
    (spec.jetCount ? 1.6 : spec.vectorDrive ? 1.2 : 1);
  return [
    { fore: bow, side: bowSide },
    // Redistribute the existing lateral hull resistance rather than counting
    // it twice. Rudder lift and rotational appendage drag remain additional.
    { fore: 0, side: -bowSide + lateral * 0.65 * appendage },
    {
      fore: stern,
      side:
        (-lateral - turn * stern) * 0.65 * appendage -
        clamp(forward * Math.abs(forward), -9, 9) *
          Math.sin(rudder * 0.65) *
          0.6 *
          appendage *
          exposure,
    },
  ];
}
