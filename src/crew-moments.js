// Surface reports refer only to this diver's actual work. No live hidden-bed
// lookup: an opinion is a sample, not a promise about the whole ground.
const LINES = {
  ada: {
    good: 'Good colour. Mark that drift.',
    poor: 'Thin pick. Worth another drop?',
    tired: 'A breather before the next one.',
  },
  milo: {
    good: 'Now that’s a bag!',
    poor: 'Swam more than I picked.',
    tired: 'Even I could use a rest.',
  },
  nell: {
    good: 'There’s a useful mark for tomorrow.',
    poor: 'Let’s remember this sample.',
    tired: 'Give the next dive a little time.',
  },
  roy: {
    good: 'Compressor’s earning its keep!',
    poor: 'Plenty of swimming, little picking.',
    tired: 'Time for a warm drink.',
  },
};
export function surfaceMoment(w, d) {
  const quality = d.bag ? d.qualitySum / d.bag : null;
  const mood =
    d.fatigue > 0.55 || /break|interval/i.test(d.reason)
      ? 'tired'
      : d.bag === 0 || (quality !== null && quality < 0.65)
        ? 'poor'
        : 'good';
  const lines = LINES[d.crewId] || {
    good: 'That’s this drift’s sample.',
    poor: 'Not much in this bag.',
    tired: 'A rest before we go again.',
  };
  const speak = w.time >= (d.nextBanterAt || 0);
  d.speech = {
    icon: mood === 'tired' ? '…' : mood === 'poor' ? '👎' : '👍',
    text: speak ? lines[mood] : '',
    until: w.time + 8,
  };
  if (speak) d.nextBanterAt = w.time + 65;
}
