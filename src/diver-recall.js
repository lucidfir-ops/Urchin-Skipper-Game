import { C } from './config.js';
import { seededRandom } from './math.js';

export function recallStatus(w, id) {
  const candidates = w.divers.filter(
    (d) => ['searching', 'harvesting'].includes(d.state) && (id === undefined || d.id === id),
  );
  candidates.sort(
    (a, b) =>
      Math.hypot(a.x - w.boat.x, a.y - w.boat.y) - Math.hypot(b.x - w.boat.x, b.y - w.boat.y) ||
      a.id - b.id,
  );
  const diver = candidates[0],
    distance = diver ? Math.hypot(diver.x - w.boat.x, diver.y - w.boat.y) : Infinity;
  return { diver, distance, available: distance <= 5 && diver.recallAt == null };
}
export function recallDiver(w, id) {
  const status = recallStatus(w, id);
  if (!status.available) return false;
  const d = status.diver,
    random = seededRandom((w.career?.seed || C.seed) ^ ((d.diveCount || 0) * 1973 + d.id * 9277));
  d.recallAt = w.time + 2 + random() * 3;
  w.events.push('CLANGING THE HULL — CALLING NEARBY DIVER UP');
  w.effects.push({ type: 'recall', diverId: d.id, x: d.x, y: d.y });
  return true;
}
