// Screen-space defaults based on the designer's tablet and Deck arrangements.
// User layouts take precedence; these adapt without rewriting saved positions.
function baselineHudRect(id, width, height, touch, tutorial = false) {
  const r = (left, top, w, h) => ({ left, top, width: w, height: h });
  if (id === 'almanacPanel') return r(width / 2 - 95, 155, 190, 36);
  if (touch) {
    const short = height < 500,
      map = short ? 126 : Math.min(240, width * 0.21),
      start = map + 14,
      available = width - start - 244,
      cell = Math.max(64, available / 5),
      gaugeH = short ? 76 : 104;
    const strip = [
      'timepiecePanel',
      'speedPanel',
      'throttlePanel',
      'fuelPanel',
      'depthInstrumentPanel',
    ];
    if (strip.includes(id)) return r(start + strip.indexOf(id) * cell, 6, cell - 4, gaugeH);
    return {
      minimapPanel: r(6, 6, map, short ? 160 : map + 44),
      clock: r(start, gaugeH + 16, 145, 76),
      sounderPanel: r(start + 152, gaugeH + 16, 145, 76),
      electronics: r(width - 236, 52, 144, short ? 64 : 94),
      currentReadout: r(width - 86, 52, 80, short ? 74 : 100),
      helmPanel: r(width * 0.6, height - 48, width * 0.4 - 6, 44),
      diverPanel: r(6, height - 48, width * 0.6 - 12, 44),
      frankAboard: r(
        start,
        gaugeH + 14,
        short ? Math.min(365, width - start - 250) : width * 0.4,
        short ? 98 : 186,
      ),
      message: r(width * 0.25, height - (short ? 205 : 222), width * 0.37, short ? 46 : 72),
      help: r(
        short && tutorial ? width - 236 : width * 0.25,
        short && tutorial ? 134 : height - (short ? 256 : 294),
        short && tutorial ? 230 : width * 0.4,
        short ? 62 : 64,
      ),
      groundLegend: r(
        short && tutorial ? 6 : width - 170,
        short && tutorial ? 172 : short ? 134 : 164,
        short && tutorial ? 126 : 164,
        short && tutorial ? 38 : 64,
      ),
      navigation: r(start, gaugeH + 14, 214, 64),
      actionFeedback: r(width * 0.58, height * 0.45, 180, 70),
      compassPanel: r(start, height * 0.38, 120, 112),
      hullPanel: r(
        short ? 6 : start + 128,
        short ? 144 : height * 0.38,
        short ? 65 : 120,
        short ? 58 : 112,
      ),
      loadPanel: r(
        short ? 73 : start + 256,
        short ? 144 : height * 0.38,
        short ? 65 : 120,
        short ? 58 : 112,
      ),
    }[id];
  }
  const left = Math.min(320, width * 0.26),
    gap = 10,
    top = Math.max(90, height * 0.14),
    gauge = Math.min(150, width * 0.12),
    right = width - gauge - 8;
  return {
    helmPanel: r(8, 8, left, height * 0.28),
    diverPanel: r(8, height * 0.3, left, height * 0.21),
    timepiecePanel: r(left + 18, 6, gauge * 1.15, top),
    clock: r(left + 18, top + 14, gauge * 1.15, 84),
    depthInstrumentPanel: r(left + gauge * 1.15 + 26, 6, gauge, top),
    sounderPanel: r(left + gauge * 1.15 + 26, top + 14, gauge, 84),
    throttlePanel: r(left + gauge * 2.15 + 34, 6, gauge, top),
    electronics: r(width - gauge * 1.7 - 8, 6, gauge * 1.7, top - 12),
    speedPanel: r(right, top + gap, gauge, 115),
    fuelPanel: r(right, top + 135, gauge, 115),
    currentReadout: r(right, top + 260, gauge, 94),
    minimapPanel: r(
      width - Math.min(240, height * 0.3) - 8,
      height - Math.min(240, height * 0.3) - 44,
      Math.min(240, height * 0.3),
      Math.min(240, height * 0.3) + 36,
    ),
    frankAboard: r(left + 18, top + 18, width - left - gauge - 40, height * 0.27),
    message: r(8, height - 92, Math.min(410, width * 0.34), 84),
    help: r(width * 0.35, height - 92, width * 0.35, 84),
    navigation: r(left + 18, tutorial ? top + height * 0.3 : top + 18, 220, 64),
    groundLegend: r(width * 0.59, height - 175, 155, 72),
    actionFeedback: r(width * 0.66, height * 0.4, 160, 72),
    compassPanel: r(left + 18, height * 0.48, 130, 115),
    hullPanel: r(8, height * 0.54, 130, 115),
    loadPanel: r(150, height * 0.54, 130, 115),
  }[id];
}

export function defaultHudRect(id, width, height, touch, tutorial = false, controlsTop) {
  let rect;
  if (touch && width < height) {
    const cell = (width - 20) / 5,
      controls =
        controlsTop === undefined
          ? 64 + ((width <= 700 ? 225 : 170) * touchScale()) / 100
          : height - controlsTop + 10;
    const top = [
      'timepiecePanel',
      'speedPanel',
      'throttlePanel',
      'fuelPanel',
      'depthInstrumentPanel',
    ];
    if (top.includes(id))
      rect = { left: 4 + top.indexOf(id) * (cell + 3), top: 50, width: cell, height: 65 };
    else
      rect = {
        minimapPanel: { left: 4, top: 122, width: 100, height: 110 },
        clock: { left: 110, top: 122, width: 134, height: 68 },
        sounderPanel: { left: 250, top: 122, width: width - 254, height: 68 },
        diverPanel: { left: 4, top: height - 52, width: width - 8, height: 48 },
        helmPanel: { left: 110, top: 198, width: width - 114, height: 45 },
        hullPanel: { left: 4, top: 240, width: 74, height: 68 },
        loadPanel: { left: 110, top: 122, width: 74, height: 68 },
        currentReadout: { left: width - 78, top: 122, width: 74, height: 68 },
        electronics: { left: 110, top: 250, width: width - 114, height: 58 },
        frankAboard: {
          left: 6,
          top: 312,
          width: width - 12,
          height: Math.min(160, height - 312 - controls),
        },
        message: { left: 6, top: height - controls - 65, width: width - 12, height: 60 },
        navigation: { left: 110, top: 315, width: width - 114, height: 60 },
        groundLegend: { left: 4, top: 315, width: 100, height: 60 },
        help: { left: 6, top: height - controls - 125, width: width - 12, height: 54 },
      }[id];
  }
  rect ||= baselineHudRect(id, width, height, touch, tutorial);
  return rect;
}
import { touchScale } from './touch-scale.js';
