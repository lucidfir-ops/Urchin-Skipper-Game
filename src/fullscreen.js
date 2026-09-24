export const fullscreenLabel = () =>
  globalThis.document?.fullscreenElement || globalThis.document?.webkitFullscreenElement
    ? 'Exit fullscreen'
    : 'Fullscreen';
export function toggleFullscreen() {
  document.querySelector('#touchFullscreen')?.click();
}
export function allowRotation() {
  try {
    globalThis.screen?.orientation?.unlock?.();
    return true;
  } catch (error) {
    // Some embedded views let only the host manage orientation. Layout still
    // responds to every viewport change and fullscreen supplies a full viewport.
    logEvent('orientation', { result: error.name });
    return false;
  }
}
export function installRotationRecovery(input) {
  let settle;
  const refresh = (event) => {
    if (document.hidden) return;
    allowRotation();
    applyScreenFit();
    clearTimeout(settle);
    // Hosts can enter fullscreen and apply their orientation after iframe load.
    // Recheck once after that transition, never in a per-frame polling loop.
    settle = setTimeout(() => {
      allowRotation();
      applyScreenFit();
      logEvent('viewport', {
        event: event?.type || 'install',
        width: innerWidth,
        height: innerHeight,
        screen: screen.orientation?.type,
        fullscreen: !!(document.fullscreenElement || document.webkitFullscreenElement),
        embedded: window !== window.top,
      });
    }, 250);
  };
  for (const name of ['pageshow', 'focus', 'resize', 'orientationchange'])
    window.addEventListener(name, refresh);
  for (const name of ['visibilitychange', 'fullscreenchange', 'webkitfullscreenchange'])
    document.addEventListener(name, refresh);
  screen.orientation?.addEventListener?.('change', refresh);
  window.visualViewport?.addEventListener('resize', refresh);
  // A child need not receive a parent's fullscreenchange. Its next touch also
  // releases the host's late orientation lock, without requiring Fullscreen.
  window.addEventListener(
    'pointerdown',
    (event) => {
      if (event.pointerType === 'touch' || input.touchEnabled) allowRotation();
    },
    { capture: true, passive: true },
  );
  refresh();
}
export function installFullscreen(input) {
  installRotationRecovery(input);
  const button = document.createElement('button'),
    notice = document.createElement('div');
  button.id = 'touchFullscreen';
  button.hidden = true;
  button.textContent = 'Fullscreen';
  notice.id = 'fullscreenNotice';
  notice.hidden = true;
  notice.setAttribute('role', 'status');
  document.body.append(button, notice);
  const active = () => document.fullscreenElement || document.webkitFullscreenElement;
  const label = () => {
    allowRotation();
    button.textContent = active() ? 'Exit fullscreen' : 'Fullscreen';
    document.querySelectorAll('[data-fullscreen]').forEach((el) => {
      el.textContent = `⛶ ${fullscreenLabel()}`;
    });
  };
  document.addEventListener('fullscreenchange', label);
  document.addEventListener('webkitfullscreenchange', label);
  button.onclick = async () => {
    input.suppress();
    try {
      if (active()) {
        const exit = document.exitFullscreen || document.webkitExitFullscreen;
        await exit.call(document);
      } else {
        const root = document.documentElement,
          request = root.requestFullscreen || root.webkitRequestFullscreen;
        if (!request) throw new Error('unsupported');
        try {
          await request.call(root, { keyboardLock: 'browser' });
        } catch (error) {
          if (error.name !== 'NotSupportedError') throw error;
          await request.call(root);
        }
        // Chromium's separate API accepts only Escape here. Modified browser
        // and desktop shortcuts continue through the ordinary event handler.
        try {
          await navigator.keyboard?.lock?.(['Escape']);
        } catch {
          /* Fullscreen still works if keyboard capture is unavailable. */
        }
      }
      notice.hidden = true;
    } catch {
      notice.textContent =
        'Fullscreen is unavailable in this browser view. On itch.io use Launch game / fullscreen; on iPhone or iPad use Share → Add to Home Screen.';
      notice.hidden = false;
      notice.onclick = () => {
        notice.hidden = true;
      };
    }
    label();
  };
}
import { applyScreenFit } from './screen-fit.js';
import { logEvent } from './troubleshooting-log.js';
