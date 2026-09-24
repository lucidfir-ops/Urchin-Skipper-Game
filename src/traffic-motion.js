import { clearVesselPose } from './vessel-contact.js';
import { C } from './config.js';
import { clamp, angleDelta } from './math.js';
import { boatSpec } from './boats.js';
import { clearWater, waterSegment } from './water-route.js';
import { checkDiverSafety } from './diver-safety.js';
import { hullDistance, fromHull } from './collision-geometry.js';
import { surfacedWildlifePoints } from './wildlife.js';

export function moveTraffic(w, actor, dt) {
  const target = actor.route[actor.waypoint];
  // Transiting boats leave at the final edge waypoint, before water bounds can
  // strand an overshooting turn. They fade over the final approach in the view.
  if (
    target &&
    actor.waypoint === actor.route.length - 1 &&
    (['taxi', 'tourist'].includes(actor.kind) || actor.phase === 'leaving')
  ) {
    const edge = Math.min(target.x, target.y, w.terrain.size - target.x, w.terrain.size - target.y);
    if (edge <= 10 && Math.hypot(actor.x - target.x, actor.y - target.y) <= 12) return true;
  }
  if (!target) {
    actor.vx = actor.vy = actor.speed = 0;
    return true;
  }
  let dx = target.x - actor.x,
    dy = target.y - actor.y;
  if (
    Math.hypot(dx, dy) <
    (actor.docking ? 0.7 : Math.max(3, (actor.knots / C.knotsPerMps) * dt * 1.5))
  ) {
    actor.waypoint++;
    return false;
  }
  const length = Math.max(0.001, Math.hypot(dx, dy));
  dx /= length;
  dy /= length;
  const player = boatSpec(w),
    avoid = [
      ...(!actor.docking || actor.target !== 'player'
        ? [{ ...w.boat, radius: player.length / 2 + actor.length / 2 + 4 }]
        : []),
      ...(w.traffic?.actors || [])
        .filter((a) => a !== actor)
        .map((a) => ({ ...a, radius: (a.length + actor.length) / 2 + 3 })),
      ...(actor.kind === 'taxi' ? surfacedWildlifePoints(w) : []),
    ];
  if (actor.kind !== 'taxi')
    for (const d of [...w.divers, ...(w.traffic?.actors || []).flatMap((a) => a.divers || [])])
      if (
        typeof d.underwater === 'boolean' ||
        ['deploying', 'searching', 'harvesting', 'surfacing', 'surface'].includes(d.state)
      )
        avoid.push({ ...d, radius: 17 });
  for (const obstacle of avoid) {
    const x = actor.x - obstacle.x,
      y = actor.y - obstacle.y,
      d = Math.hypot(x, y),
      range = obstacle.radius + (actor.knots / C.knotsPerMps) * 2;
    if (d >= range || d < 0.001) continue;
    const force = ((range - d) / Math.max(1, range - obstacle.radius)) * 2.5;
    const side = actor.id.charCodeAt(actor.id.length - 1) % 2 ? 1 : -1;
    dx += (x / d) * force - (y / d) * force * 0.8 * side;
    dy += (y / d) * force + (x / d) * force * 0.8 * side;
  }
  const desired = Math.atan2(dx, -dy),
    delta = angleDelta(desired, actor.heading),
    heading = actor.heading + clamp(delta, -actor.turnRate * dt, actor.turnRate * dt),
    speed = (actor.knots / C.knotsPerMps) * Math.max(0.12, Math.cos(delta)),
    next = {
      x: actor.x + Math.sin(heading) * speed * dt,
      y: actor.y - Math.cos(heading) * speed * dt,
    },
    spec = { draft: actor.draft, radius: Math.max(actor.width / 2, 3) };
  const previous = { x: actor.x, y: actor.y, heading: actor.heading };
  const safe = clearVesselPose(w, actor, previous, { ...next, heading });
  actor.heading = safe.heading;
  if (
    safe.blocked ||
    !clearWater(w.terrain, w.environment.seaLevel || 0, next, spec) ||
    !waterSegment(w.terrain, w.environment.seaLevel || 0, actor, next, spec) ||
    (actor.docking &&
      actor.target === 'player' &&
      [-1, 1].some((side) =>
        [-1, 1].some((fore) => {
          const corner = fromHull(
            { ...next, heading },
            (side * actor.width) / 2,
            (fore * actor.length) / 2,
          );
          return hullDistance(w.boat, corner.x, corner.y, player) < 0.25;
        }),
      )) ||
    avoid.some(
      (o) =>
        Math.hypot(next.x - o.x, next.y - o.y) < o.radius &&
        Math.hypot(next.x - o.x, next.y - o.y) < Math.hypot(actor.x - o.x, actor.y - o.y),
    )
  ) {
    if (safe.blocked) {
      actor.x = safe.x;
      actor.y = safe.y;
    }
    actor.vx = actor.vy = actor.speed = 0;
    actor.stuckSeconds = (actor.stuckSeconds || 0) + dt;
    const edge = Math.min(actor.x, actor.y, w.terrain.size - actor.x, w.terrain.size - actor.y);
    if (['taxi', 'tourist'].includes(actor.kind) && edge < 22 && actor.stuckSeconds >= 3)
      return true;
    return false;
  }
  actor.stuckSeconds = 0;
  actor.vx = (next.x - actor.x) / dt;
  actor.vy = (next.y - actor.y) / dt;
  actor.speed = speed;
  actor.x = next.x;
  actor.y = next.y;
  checkDiverSafety(w, previous, {
    boat: actor,
    spec: { length: actor.length, width: actor.width },
    exposed: true,
  });
  return false;
}
