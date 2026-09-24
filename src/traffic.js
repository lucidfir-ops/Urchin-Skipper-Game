import { seededRandom } from './math.js';
import { boatDefinition } from './boats.js';
import { TAXI_ART, DFO_ART, NINE_ART } from './vessel-catalog.js';
import { crewProfile } from './crew-roster.js';
import { takeCatch } from './harvest-ground.js';
import { waterEntries, waterRoute } from './water-route.js';
import { moveTraffic } from './traffic-motion.js';
import { TRAFFIC, trafficSettings } from './traffic-settings.js';
import { stepPatrol } from './patrol.js';
import { inspectionDue } from './inspection-schedule.js';
import { recordFishingPressure, subAreaYield } from './quota-areas.js';

const pick = (values, random) => values[Math.floor(random() * values.length)];
export function prepareTraffic(w) {
  if (!w.career || w.day.phase !== 'working') return null;
  if (w.traffic?.area === w.day.groundId) return w.traffic;
  const random = seededRandom(w.career.seed ^ (w.career.day * 6373));
  return (w.traffic = {
    area: w.day.groundId,
    actors: [],
    serial: 0,
    accumulator: 0,
    next: Object.fromEntries(
      ['taxi', 'tourist', 'dfo', 'rival'].map((kind) => [
        kind,
        w.time + (kind === 'dfo' ? 8 : TRAFFIC[kind][0]) * (0.6 + random() * 0.4),
      ]),
    ),
  });
}
function outsideView(w, p) {
  const view = w.trafficView || { x: w.boat.x, y: w.boat.y, rangeX: 100, rangeY: 70 };
  return Math.abs(p.x - view.x) > view.rangeX + 20 || Math.abs(p.y - view.y) > view.rangeY + 20;
}
const spawnJobs = new WeakMap();
export function spawnTraffic(w, kind, options = {}) {
  const search = planTraffic(w, kind, options);
  let result;
  do {
    result = search.next();
  } while (!result.done);
  return result.value;
}
function* planTraffic(w, kind, { start, patchId, art, fleetId } = {}) {
  const traffic = prepareTraffic(w);
  if (!traffic || traffic.actors.length >= TRAFFIC.maxActors) return null;
  const random = seededRandom(
    Math.imul(w.career.seed, 2654435761) ^ (w.career.day * 193 + ++traffic.serial * 9277),
  );
  const mystery = w.career.opponents.find((t) => t.hidden);
  let fleet;
  if (kind === 'rival') {
    const candidates = w.career.todayFleet.filter(
      (r) =>
        r.area === w.day.groundId &&
        !r.shipDone &&
        r.begin <= w.day.minute &&
        w.day.minute < r.end &&
        !traffic.actors.some((a) => a.fleetId === r.id),
    );
    fleet = fleetId
      ? candidates.find((r) => r.id === fleetId)
      : pick(
          candidates.filter((r) => !r.hidden || random() < 0.08),
          random,
        );
    if (!fleet) return null;
  }
  const id = `traffic-${w.career.day}-${traffic.area}-${traffic.serial}`,
    actor = {
      id,
      kind,
      forPlayer: kind === 'dfo',
      art:
        art ||
        (kind === 'taxi'
          ? pick(TAXI_ART, random)
          : kind === 'dfo'
            ? pick(DFO_ART, random)
            : kind === 'rival'
              ? fleet.art
              : pick(
                  NINE_ART.filter((id) => id !== mystery.art),
                  random,
                )),
      knots: kind === 'taxi' ? 30 : kind === 'dfo' ? 25 : kind === 'tourist' ? 5 : fleet.speed,
      length: kind === 'rival' ? 11 : 9,
      width: kind === 'rival' ? 4 : 3.2,
      draft: kind === 'rival' ? boatDefinition(fleet.hull).spec.draft || 2 : 2,
      turnRate: kind === 'rival' ? fleet.turnRate : 1.1,
      route: [],
      waypoint: 0,
      heading: 0,
      vx: 0,
      vy: 0,
      turn: 0,
      throttle: 1,
      speed: 0,
      phase: 'transit',
      born: w.time,
      checked: [],
      fleetId: fleet?.id || null,
      hidden: !!fleet?.hidden,
      subAreaId: fleet?.subAreaId || null,
      wildlifeCurious: kind === 'tourist' && random() < 0.65,
    };
  const spec = { draft: actor.draft, radius: 5 },
    entries = waterEntries(w, spec),
    starts = start ? [start] : kind === 'dfo' ? entries : entries.filter((p) => outsideView(w, p));
  if (!starts.length) return null;
  const desiredPatch = patchId || trafficSettings(w).patchId;
  const patches = w.patches.filter(
    (p) =>
      p.remaining > 0 &&
      (kind !== 'rival' || p.quality >= 0.6) &&
      (!desiredPatch || p.id === desiredPatch),
  );
  for (let attempt = 0; attempt < 12; attempt++) {
    const entry = pick(starts, random),
      patch = pick(patches, random),
      end = pick(
        entries.filter((p) => Math.hypot(p.x - entry.x, p.y - entry.y) > w.terrain.size * 0.6),
        random,
      );
    if (!entry || !end || !patch) {
      yield;
      continue;
    }
    const working = { x: patch.x, y: patch.y },
      route = waterRoute(w, entry, kind === 'dfo' && !desiredPatch ? end : working, spec);
    if (!route.length) {
      yield;
      continue;
    }
    if (kind === 'taxi' || kind === 'tourist' || (kind === 'dfo' && desiredPatch)) {
      const exit = waterRoute(w, working, end, spec);
      if (!exit.length) {
        yield;
        continue;
      }
      route.push(...exit);
    }
    Object.assign(actor, entry, {
      route,
      patchId: patch.id,
      heading: Math.atan2(route[0].x - entry.x, entry.y - route[0].y),
    });
    if (
      traffic.actors.length >= TRAFFIC.maxActors ||
      (fleet &&
        (fleet.shipDone ||
          w.day.minute >= fleet.end ||
          traffic.actors.some((a) => a.fleetId === fleet.id)))
    )
      return null;
    traffic.actors.push(actor);
    return actor;
  }
  return null;
}
function setRoute(w, actor, target) {
  if (!target) return false;
  const route = waterRoute(w, actor, target, { draft: actor.draft, radius: 5 });
  if (!route.length) return false;
  actor.route = route;
  actor.waypoint = 0;
  return true;
}
function fish(w, actor, dt) {
  const fleet = w.career.todayFleet.find((r) => r.id === actor.fleetId),
    patch = w.patches.find((p) => p.id === actor.patchId);
  if (!fleet || !patch) {
    actor.done = true;
    return;
  }
  if (actor.phase === 'transit' && w.day.minute >= fleet.end) {
    actor.phase = 'leaving';
    fleet.shipDone = true;
    if (!waterEntries(w, { draft: actor.draft, radius: 5 }).some((p) => setRoute(w, actor, p)))
      actor.done = true;
  }
  if (actor.phase === 'transit') {
    if (moveTraffic(w, actor, dt)) {
      actor.phase = 'fishing';
      actor.workSeconds = 0;
    }
    return;
  }
  if (actor.phase === 'leaving') {
    if (moveTraffic(w, actor, dt)) actor.done = true;
    return;
  }
  if (actor.inspectedBy) return;
  actor.workSeconds += dt;
  actor.divers = [];
  const crew = w.career.opponents.find((r) => r.id === (fleet.teamId || fleet.id))?.crew || [];
  for (const [i, id] of crew.entries()) {
    const profile = crewProfile(w.career, id),
      record = w.career.people[id];
    if (!profile || record?.condition !== 'fit' || record.availableDay > w.career.day) continue;
    const clumps = (patch.clumps || [])
        .filter((c) => c.remaining > 0)
        .sort(
          (a, b) =>
            Math.hypot(a.x - actor.x, a.y - actor.y) - Math.hypot(b.x - actor.x, b.y - actor.y),
        ),
      clump = clumps[Math.min(i, clumps.length - 1)];
    if (!clump) continue;
    const underwater = (actor.workSeconds + i * 7) % 55 < 45;
    actor.divers.push({ x: clump.x, y: clump.y, underwater });
    if (!underwater) continue;
    record.experience = (record.experience || 0) + dt * 10;
    const requested = Math.min(
        fleet.goal - fleet.gross,
        patch.rate *
          profile.harvestRate *
          (fleet.catchSpeed || 1) *
          (30 / 45) *
          (1 + (record.experience || 0) / 200000) *
          subAreaYield(w.career, fleet.area, fleet.subAreaId) *
          dt,
      ),
      amount = takeCatch(patch, clump, Math.max(0, requested));
    fleet.gross += amount;
    fleet.qualitySum += amount * (clump.quality ?? patch.quality);
    recordFishingPressure(w.career, fleet.area, fleet.subAreaId, 'npc', amount);
  }
  actor.deckBags = Math.floor(fleet.gross / 300);
  // Patrol between safe pickup positions alongside the bubble patches.
  if (actor.workSeconds >= (actor.nextPickupMove || 0)) {
    actor.nextPickupMove = actor.workSeconds + 25;
    actor.pickupSide = -(actor.pickupSide || 1);
    const target = { x: patch.drop.x + actor.pickupSide * 12, y: patch.drop.y + 18 };
    setRoute(w, actor, target);
  }
  const passageSpeed = actor.knots;
  actor.knots = 1.8;
  moveTraffic(w, actor, dt);
  actor.knots = passageSpeed;
  fleet.minute = Math.max(fleet.minute, w.day.minute);
  if (fleet.gross >= fleet.goal - 0.01 || patch.remaining <= 0.01 || w.day.minute >= fleet.end) {
    actor.divers = [];
    fleet.shipDone = true;
    actor.phase = 'leaving';
    const exits = waterEntries(w, { draft: actor.draft, radius: 5 }).sort(
      (a, b) => Math.hypot(a.x - actor.x, a.y - actor.y) - Math.hypot(b.x - actor.x, b.y - actor.y),
    );
    if (!exits.some((p) => setRoute(w, actor, p))) actor.done = true;
  }
}
export function stepTraffic(w, dt) {
  const traffic = prepareTraffic(w);
  if (!traffic) return;
  const settings = trafficSettings(w);
  if (settings.rate <= 0) spawnJobs.delete(traffic);
  else {
    let job = spawnJobs.get(traffic);
    if (!job) {
      const kind = ['taxi', 'tourist', 'dfo', 'rival'].find(
        (kind) => w.time >= traffic.next[kind] && (kind !== 'dfo' || inspectionDue(w)),
      );
      if (kind) {
        const available =
          traffic.actors.filter((a) => a.kind === kind).length < (kind === 'dfo' ? 1 : 2);
        job = { kind, search: available ? planTraffic(w, kind) : null };
        spawnJobs.set(traffic, job);
      }
    }
    if (job) {
      // One attempted itinerary per tick; failed searches keep their RNG and
      // candidates across ticks instead of running twelve searches in one frame.
      const result = job.search?.next();
      if (!result || result.done) {
        spawnJobs.delete(traffic);
        const random = seededRandom(w.career.seed ^ (traffic.serial * 9173 + Math.floor(w.time)));
        traffic.next[job.kind] =
          w.time +
          (TRAFFIC[job.kind][0] + random() * (TRAFFIC[job.kind][1] - TRAFFIC[job.kind][0])) /
            settings.rate;
      }
    }
  }
  traffic.accumulator += dt;
  while (traffic.accumulator >= TRAFFIC.tickSeconds) {
    traffic.accumulator -= TRAFFIC.tickSeconds;
    for (const actor of traffic.actors) {
      actor.renderFrom = { x: actor.x, y: actor.y, heading: actor.heading };
      if (actor.kind === 'dfo') stepPatrol(w, actor, TRAFFIC.tickSeconds);
      else if (actor.kind === 'rival') fish(w, actor, TRAFFIC.tickSeconds);
      else if (moveTraffic(w, actor, TRAFFIC.tickSeconds)) actor.done = true;
      if (w.emergency?.mandatoryRescue) return;
      if (w.time - actor.born > 1200 && actor.kind !== 'dfo') actor.done = true;
    }
    traffic.actors = traffic.actors.filter((a) => !a.done);
  }
}
