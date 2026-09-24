"""Preserve selected release evidence; never replace an older acceptance set."""
from pathlib import Path
import hashlib
import json
import shutil
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
out = root / 'docs/history/2026-09-20-device-feedback/acceptance'
out.mkdir(exist_ok=False)
reports = ['verification-unit.json', 'verification-device-feedback.json',
           'verification-device-feedback-firefox.json', 'verification-device-embed.json',
           'verification-performance.json', 'verification-shore-hazards.json',
           'sep20-device-feedback.json', 'sep20-embed.json', 'performance-chromium.json',
           'september20-unit-verify.log', 'september20-browser.log', 'september20-firefox.log',
           'september20-embed.log', 'september20-performance-final.log',
           'september20-hazards.log', 'september20-package.log',
           'september20-lint.log', 'september20-format-check.log', 'september20-final-build.log']
shots = [f'sep20-{device}-{screen}.png' for device in ['tablet','s22','deck']
         for screen in ['frank','crew','conditions','fleetboard','settings','layout','harbour-fit','water','tutorial']]
shots += ['sep20-embedded-title.png', 'shore-chromium-deep-shallow-exposed-bands.png',
          'shore-chromium-calm.png', 'shore-chromium-night-fog.png', 'performance-chromium-traffic.png']
for name in reports + shots:
    shutil.copy2(root / 'test-results' / name, out / name)
release = root / 'exports/2026-09-20-device-feedback'
digest = lambda data: hashlib.sha256(data).hexdigest()
verification = {}
for name in ['UrchinSkipper-TEMP-ITCHIO.zip', 'Urchin Skipper TEMP.zip']:
    path = release / name
    with ZipFile(path) as z:
        assert z.testzip() is None
        prefix = '' if 'ITCHIO' in name else 'Urchin Skipper TEMP/dist/'
        for file in (root/'dist').rglob('*'):
            if file.is_file():
                assert z.read(prefix+file.relative_to(root/'dist').as_posix()) == file.read_bytes()
        assert not any('firefox-profile' in p or 'urchin-career-day-' in p for p in z.namelist())
    verification[name] = {'bytes':path.stat().st_size,'sha256':digest(path.read_bytes()),'all_dist_bytes_match':True,'zip_integrity':True,'profile_free':True}
(out/'release-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
print(json.dumps(verification,indent=2))
