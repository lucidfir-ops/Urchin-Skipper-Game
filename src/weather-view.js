import { rainMotion } from './wind-motion.js';
import { C } from './config.js';
import { gear, visibilityRange } from './assists.js';
import { lightningState } from './weather-effects.js';
// A screen veil changes what can be seen; it never changes the sea bed.
export class WeatherView {
  constructor() {
    this.canvas = document.createElement('canvas');
    this.canvas.id = 'weatherVeil';
    document.querySelector('#game').after(this.canvas);
  }
  draw(w, width, height, zoom) {
    const canvas = this.canvas;
    canvas.hidden = !w.career;
    if (!w.career) return;
    if (canvas.width !== width || canvas.height !== height) {
      canvas.width = width;
      canvas.height = height;
    }
    const ctx = canvas.getContext('2d'),
      weather = w.weather;
    if (!weather) return;
    ctx.clearRect(0, 0, width, height);
    const cx = width / 2,
      cy = height / 2,
      r = visibilityRange(w) * C.pixelsPerMeter * zoom;
    if (weather.darkness) {
      const light = ctx.createRadialGradient(cx, cy, Math.min(20, r * 0.2), cx, cy, r);
      light.addColorStop(0, `rgba(3,15,26,${weather.darkness * 0.18})`);
      light.addColorStop(1, `rgba(3,15,26,${weather.darkness})`);
      ctx.fillStyle = light;
      ctx.fillRect(0, 0, width, height);
      if (gear(w, 'lights')) {
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(w.boat.heading);
        ctx.fillStyle = '#f8dfa416';
        ctx.beginPath();
        ctx.moveTo(-8, -10);
        ctx.lineTo(-r * 0.6, -r * 0.4);
        ctx.lineTo(-r * 0.7, r * 0.5);
        ctx.closePath();
        ctx.fill();
        // Clear part of the darkness in the forward beam, then tint it warmly.
        const beam = ctx.createRadialGradient(0, -10, 0, 0, -10, r);
        beam.addColorStop(0, 'rgba(255,255,255,0.78)');
        beam.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = beam;
        ctx.beginPath();
        ctx.moveTo(0, -10);
        ctx.arc(0, -10, r, -Math.PI / 2 - 0.48, -Math.PI / 2 + 0.48);
        ctx.closePath();
        ctx.fill();
        ctx.globalCompositeOperation = 'source-over';
        ctx.fillStyle = '#ffe6a014';
        ctx.fill();
        ctx.restore();
      }
    }
    if (weather.visibility < 200) {
      const fog = ctx.createRadialGradient(cx, cy, r * 0.15, cx, cy, r * 1.6);
      fog.addColorStop(0, '#c0d0c500');
      fog.addColorStop(1, `rgba(142,165,163,${weather.kind === 'fog' ? 0.87 : 0.25})`);
      ctx.fillStyle = fog;
      ctx.fillRect(0, 0, width, height);
    }
    const lightning = lightningState(weather, w.time);
    if (lightning.flash) {
      ctx.fillStyle = `rgba(218,235,255,${lightning.flash * 0.58})`;
      ctx.fillRect(0, 0, width, height);
    }
    const motion = rainMotion(w.environment.wind);
    const dt =
      this.lastWorld === w ? Math.max(0, Math.min(0.1, w.time - (this.lastTime ?? w.time))) : 0;
    this.lastWorld = w;
    this.lastTime = w.time;
    this.rainX = (this.rainX || 0) + motion.x * dt;
    this.rainY = (this.rainY || 0) + motion.y * dt;
    const speed = Math.max(1, Math.hypot(motion.x, motion.y));
    const wrap = (n, span) => ((n % span) + span) % span;
    for (const layer of [0, 1]) {
      const factor = layer ? 1.25 : 0.7;
      ctx.strokeStyle = `rgba(215,235,236,${weather.rain * (layer ? 0.58 : 0.3)})`;
      ctx.lineWidth = layer ? 1.45 : 0.9;
      ctx.beginPath();
      const count = Math.min(260, Math.floor((weather.rain * width * height) / 4700));
      const length = (9 + Math.min(24, speed * 0.05)) * factor;
      for (let i = 0; i < count; i++) {
        const x = wrap(i * 173.7 + layer * 79 + this.rainX * factor, width + 60) - 30;
        const y = wrap(i * 91.3 + layer * 173 + this.rainY * factor, height + 60) - 30;
        ctx.moveTo(x, y);
        ctx.lineTo(x + (motion.x / speed) * length, y + (motion.y / speed) * length);
      }
      ctx.stroke();
    }
  }
}
