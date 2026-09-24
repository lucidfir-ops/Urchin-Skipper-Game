export const TRAFFIC = {
  maxActors: 7,
  tickSeconds: 0.1,
  inspectionMinutes: 6,
  sightMeters: 250,
  taxi: [90, 210],
  tourist: [140, 280],
  dfo: [240, 420],
  rival: [45, 120],
};
export function trafficSettings(w) {
  const saved = w.career?.trafficSettings || {};
  return {
    rate: Math.max(0, Math.min(3, saved.rate ?? 1)),
    patchId: saved.patchId || null,
    inspectionMinutes: Math.max(
      1,
      Math.min(60, saved.inspectionMinutes ?? TRAFFIC.inspectionMinutes),
    ),
  };
}
