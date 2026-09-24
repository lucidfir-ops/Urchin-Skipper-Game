import { engineState } from './operating-state.js';
import { recallStatus } from './diver-recall.js';
import { pickupTolerance } from './assists.js';
import { C } from './config.js';
import {
  recoveryStatus,
  recoveryDuration,
  deploymentStatus,
  nearestRecoveryTarget,
  actionTarget,
  rediveStatus,
} from './simulation.js';
import { selectedDiver } from './world.js';
export function interactionDiver(w, realistic = false) {
  const tolerance = pickupTolerance(w, realistic);
  // Follow ongoing progress for information; each action still resolves its own
  // eligible physical target, independently of this display or diver selection.
  const working = w.divers.find((d) => d.state === 'surface' && d.hooking);
  if (working) return working;
  const eligible = nearestRecoveryTarget(w, 'recoverDiver', tolerance);
  if (eligible) return eligible;
  if (!realistic) return selectedDiver(w);
  const nearby = w.divers
    .filter(
      (d) =>
        d.state === 'surface' &&
        recoveryStatus(w, C.recovery.tolerance, d).distance <= C.recovery.tolerance + 3,
    )
    .sort(
      (a, b) =>
        Math.hypot(a.x - w.boat.x, a.y - w.boat.y) - Math.hypot(b.x - w.boat.x, b.y - w.boat.y),
    );
  return nearby[0] || selectedDiver(w);
}
export const throttleText = (value) =>
  `${Math.round(Math.abs(value) * 100)}% ${value > 0 ? 'AHEAD' : value < 0 ? 'REVERSE' : 'NEUTRAL'}`;
export const rudderText = (value) =>
  `${Math.round((Math.abs(value) / C.boat.rudderLimit) * 100)}% ${value > 0 ? 'STARBOARD' : value < 0 ? 'PORT' : 'CENTER'}`;
export function feedbackText(text, realistic = false) {
  if (!realistic) return text;
  // Automatic underwater/surface transitions are observed through bubbles and floats.
  if (/DIVER SURFACING|DIVER SURFACED|DIVER UNDERWATER|FRESH BAG PROVIDED/.test(text)) return null;
  return text
    .replace(/\d+ lb EXCESS CATCH/, 'EXCESS CATCH')
    .replace(/BAG RECOVERED — \d+ lb/, 'BAG RECOVERED');
}
export function diverVisual(d) {
  return {
    bubbles: ['deploying', 'searching', 'harvesting', 'surfacing'].includes(d.state),
    surface: d.state === 'surface',
    aboard: d.state === 'ready',
  };
}
export function deckMarkers(bags) {
  const columns = Math.max(3, Math.ceil(Math.sqrt(bags.length))),
    rows = Math.max(4, Math.ceil(bags.length / columns));
  return bags.map((_, i) => ({
    x: -1.4 + ((i % columns) * 2.8) / Math.max(1, columns - 1),
    y: 1 + (Math.floor(i / columns) * 3) / Math.max(1, rows - 1),
    radius: Math.min(0.55, 1.6 / columns, 1.8 / rows),
  }));
}
export function playState(
  w,
  lockReason = '',
  tolerance = C.recovery.tolerance,
  d = selectedDiver(w),
  realistic = false,
) {
  const r = recoveryStatus(w, tolerance, d),
    waiting = diverVisual(d).surface,
    duration = recoveryDuration(d);
  const operation = d.recoveryAction === 'recoverDiver' ? 'DIVER + BAG RECOVERY' : 'BAG TURNAROUND';
  let status;
  if (waiting) {
    if (d.hooking && r.available)
      status = `${operation} — ${Math.max(0, duration - d.hook).toFixed(1)}s`;
    else if (d.hooking || d.recoveryPause || d.hook > 0)
      status = `RECOVERY PAUSED — ${r.reason || d.recoveryPause || 'PLAYER PAUSED'}`;
    else
      status = r.available
        ? d.condition === 'injured'
          ? 'INJURED DIVER — BRING ABOARD'
          : d.bagHandled
            ? 'BAG ABOARD — SEND DOWN AGAIN OR BOARD'
            : 'RECOVERY AVAILABLE'
        : `RECOVERY UNAVAILABLE — ${r.reason}`;
  } else
    status = {
      ready:
        d.condition === 'injured'
          ? 'INJURED DIVER ABOARD — RETURN TO HARBOUR'
          : 'DIVER ABOARD — CHOOSE A DROP',
      fatality: 'DIVER FATALITY — RADIO FOR EMERGENCY ASSISTANCE',
      deploying: `DIVER DEPLOYING — ${Math.max(0, d.timer).toFixed(1)}s`,
      searching: 'DIVER UNDERWATER — BUBBLES ONLY',
      harvesting: 'DIVER UNDERWATER — BUBBLES ONLY',
      surfacing: `DIVER SURFACING — ${Math.max(0, d.timer).toFixed(1)}s`,
    }[d.state];
  if (!realistic && ['surface', 'surfacing'].includes(d.state) && d.reason && !d.hooking)
    status += ` · ${d.reason}${d.bagHandled ? ' · empty bag' : ` · ${Math.round(d.bag)} lb in bag`}`;
  if (d.state === 'ready' && w.day.inspection?.status === 'boarding')
    status = 'INSPECTION UNDERWAY — HOLD A SAFE POSITION';
  else if (d.state === 'ready' && w.day.crewRest > 0) status = 'CREW WARMING UP';
  const actions = [];
  if (!lockReason) {
    for (const action of ['work', 'recoverDiver']) {
      const target = actionTarget(w, action, tolerance),
        status = recoveryStatus(w, tolerance, target),
        operation = action === 'work' ? 'recoverBag' : 'recoverDiver';
      let text = '';
      if (target.state === 'surface' && target.hooking && target.recoveryAction === operation)
        text = w.career ? 'Recovery in progress' : 'Pause recovery';
      else if (
        status.available &&
        action === 'work' &&
        target.bagHandled &&
        rediveStatus(w, target).available
      )
        text = 'Fresh bag → Send diver down';
      else if (status.available && (action !== 'work' || status.bagAvailable))
        text =
          action === 'work'
            ? 'Recover Bag · diver waits'
            : target.bagHandled
              ? 'Board Diver · fresh tank'
              : 'Recover Diver + Bag';
      else if (action === 'recoverDiver' && deploymentStatus(w, target).available)
        text = 'Deploy Diver';
      if (text) actions.push({ action, text, diverId: target.id });
    }
    const recall = recallStatus(w);
    if (recall.available)
      actions.push({
        action: 'recall',
        text: 'Clang hull · summon diver',
        diverId: recall.diver.id,
      });
  }
  const observable =
    !realistic || d.state === 'ready' || (waiting && r.distance <= C.recovery.tolerance + 3);
  if (!observable) status = 'WATCH BUBBLES / MANEUVER ALONGSIDE';
  return {
    status,
    operation,
    available: r.available && observable,
    observable,
    distance: r.distance,
    waterSpeed: r.waterSpeed,
    overflow: r.overflow,
    actions,
    reason: observable && waiting && d.bagHandled ? rediveStatus(w, d).reason : '',
    diverId: d.id,
    progress: !observable
      ? null
      : waiting && d.hook > 0
        ? Math.min(1, d.hook / duration)
        : d.state === 'deploying'
          ? 1 - d.timer / C.diver.deploySeconds
          : null,
    controls: lockReason
      ? `CONTROLS LOCKED: ${lockReason}`
      : engineState(w).powered
        ? 'BOAT CONTROLS AVAILABLE'
        : `HELM RESPONDING · ${engineState(w).label}`,
    locked: !!lockReason,
  };
}
// Surface color only reveals the shallow 0–10 m band. Sounder never modifies it.
export function terrainColor(depth) {
  if (depth <= 0) return depth > -1 ? [173, 164, 125] : [83, 104, 75];
  const t = Math.min(1, depth / 10),
    shallow = [109, 154, 138],
    deep = [22, 76, 96];
  return shallow.map((v, i) => Math.round(v + (deep[i] - v) * t));
}
