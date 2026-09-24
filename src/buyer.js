import { roll } from './career-data.js';
function buyerDemand(c, day) {
  return {
    day,
    minQuality: [0.6, 0.7, 0.8][Math.floor(roll(c.seed, day + 4701) * 3)],
    premium: 0.2,
  };
}
export function prepareBuyer(c) {
  // Never spring a new requirement on an already saved working day.
  c.buyerNext ??= buyerDemand(c, c.day + 1);
}
export function advanceBuyer(c) {
  c.buyerToday = c.buyerNext?.day === c.day ? c.buyerNext : null;
  c.buyerNext = buyerDemand(c, c.day + 1);
}
export function buyerNotice(c) {
  prepareBuyer(c);
  const offer = (d) =>
    `${Math.round(d.minQuality * 100)}% landed quality · +${Math.round(d.premium * 100)}% price`;
  return `Today: ${c.buyerToday ? offer(c.buyerToday) : 'standard market'}. Tomorrow (day ${c.buyerNext.day}): ${offer(c.buyerNext)}. Lower quality still sells at the standard market price. Catch age can reduce landed quality.`;
}
