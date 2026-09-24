import { boatDefinition, boatSpec } from './boats.js';
import { C } from './config.js';
import { boatFamily } from './vessel-catalog.js';

const HANDLING = {
  basic:
    'Your shaft boat likes a little ahead power over the rudder. Centre the rudder before a long straight run; reverse has less steering authority. Leave room for the turn.',
  thruster:
    'Use the bow thruster in short bursts at low speed to swing the bow. It fades as speed rises. The main rudder still needs flow; settle alongside before handling a bag.',
  sterndrive:
    'That steerable leg turns the thrust itself. Small ahead or reverse inputs give good control, but keep the exposed leg away from rocks and floating timber.',
  outboard:
    'The Tender turns neatly under thrust and gets home quickly. Its small deck fills first. Give rocks and timber a wide berth: that exposed outboard is vulnerable.',
  jet: 'The single jet can work in shallower water, but still needs thrust to steer. Neutral coasts. It is a working boat at ten knots, so budget the passage time.',
  twinjet:
    'Select neutral, then hold right stick up to pivot port or down to pivot starboard. Release to coast. Left stick sideways operates a fitted bow thruster independently.',
};
export function frankAdvice(w, bind) {
  const boat = boatDefinition(w.boat.configuration),
    family = boatFamily(boat.id),
    spec = boatSpec(w);
  return `Meet the boat: ${boat.name}.
${HANDLING[family]}${family === 'basic' && spec.bowThrusterStrength ? ' Your fitted bow thruster adds low-speed sideways bow control; hold left stick left or right.' : ''}
${boat.controls}
${Math.round(spec.maxSpeed * C.knotsPerMps)} knots at this load · ${spec.capacity.toLocaleString()} lb deck · ${spec.travelBurn} L/h passage. Keep fuel for the return and a reserve.

Drop on promising bottom. The sounder shows depth; kelp and the chart help you find a reef edge. ${bind('recoverDiver')} deploys the selected diver. ${bind('cycleDiver')} selects the other berth. ${bind('instructions')} / ${bind('quickOrders')} changes the search direction and minimum quality. ${bind('recall')} recalls bubbles within 5 m; listen for the clang and allow 2–5 seconds for a response.

Bring the float to port and match its drift. Pickup speed is relative to the float: drifting together at two knots is fine. Keep the float outside the hull and away from powered propellers.

${bind('work')} takes the bag and leaves the diver waiting with the same tank. Press it again to send down with an empty bag if there is air and useful ground. ${bind('recoverDiver')} brings diver and any catch aboard, supplies an empty bag and a fresh tank. Partial bags stay safely on deck. The next deployment starts a new search.

When diver readouts are enabled, check the surfacing reason: full bag, air reserve, exhausted ground, a table break or the quality order. Fresh tanks do not clear accumulated dive exposure; heed requests for surface intervals. Repeated deep days can lead to suspected decompression sickness and a medical return. These are fictional game tables, never real dive guidance. Reports are written to the chart as the catch comes aboard.

Sometimes your divers pick undersize and there’s nothing you can do.

An early departure before 07:00 adds 6% fatigue once; darkness also makes unlit work harder. Rest ashore or warm up the crew at sea. Experience builds over worked trips; check each diver's level in Meet the crew.

${bind('debug')} cycles the permitted information presets: Easy / Realistic / All Off in Easy careers, Realistic / All Off in Realistic careers. ${bind('assists')} opens the assists menu. For identity and selection only, disable Diver indicators and enable the portrait-only selector. ${bind('chart')} opens your current area's chart. ${bind('almanac')} opens tides, or use the Tide & current almanac button. Bring both divers home across the marked harbour edge for 19:00 offload. Injuries need medical help; sinking or a fatality needs radio assistance.`;
}
