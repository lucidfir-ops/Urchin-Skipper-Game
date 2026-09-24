"""Read-only full project inventory; player files are counted, never opened or changed."""
from pathlib import Path
from collections import defaultdict
import os
import json

root = Path(__file__).resolve().parents[1]
totals = defaultdict(lambda: {'files': 0, 'bytes': 0})
links = 0
for parent, folders, files in os.walk(root, followlinks=False):
    for name in files:
        path = Path(parent) / name
        if path.is_symlink():
            links += 1
            continue
        relative = path.relative_to(root)
        category = relative.parts[0] if len(relative.parts) > 1 else '[root files]'
        stat = path.stat()
        totals[category]['files'] += 1
        totals[category]['bytes'] += stat.st_size
result = {'scope': 'Entire UrchinSkipper workspace, symlinks not followed',
          'groups': dict(sorted(totals.items(), key=lambda item: -item[1]['bytes'])),
          'symlinks_skipped': links,
          'cleanup': 'Removed only .npm-cache/_cacache (~314 MiB) and .runtime/whisper/pip-cache/http-v2 (~126 MiB). Redownloadable package caches; models, installed dependencies, player profiles, original assets/feedback/documents and older exports preserved.'}
target = root / 'docs/history/2026-09-20-device-feedback/storage-audit.json'
target.write_text(json.dumps(result, indent=2) + '\n')
print(target)
