#!/usr/bin/env python3
"""Create an additive, verified project checkpoint or validate an existing one.

Source, assets, documents, raw data and dist are included. Rebuildable caches and
browser profiles are excluded. No old archive is ever removed or overwritten.
"""
import argparse
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {"node_modules", ".browser-cache", ".npm-cache", ".runtime", "checkpoints", "test-results", ".git", "__pycache__"}
REQUIRED = ["package.json", "package-lock.json", "index.html", "src/main.js", "src/world-data.json", "src/generated/sectors.json", "world-source/sectors.js", "scripts/generate-sectors.js", "scripts/launch-deck.sh"]
DESIGN_LOCATIONS = ("DESIGN_DOCUMENT.txt", "archive/DESIGN_DOCUMENT.txt")
PREFIX = "UrchinSkipper/"
MANIFEST = PREFIX + ".backup-manifest.json"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def files():
    for directory, dirs, names in os.walk(ROOT):
        # Portable launches also create live profiles inside their export folder.
        # Preserve them in place, just like the root .runtime browser profile.
        skip = EXCLUDE if Path(directory) == ROOT else {"__pycache__", ".player-data"}
        dirs[:] = sorted(d for d in dirs if d not in skip)
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_symlink():
                raise ValueError(f"Review source symlink before archiving: {path.relative_to(ROOT)}")
            if path.is_file():
                yield path

def verify(archive, restore=False):
    with tarfile.open(archive, "r:gz") as tf:
        manifest = json.load(tf.extractfile(MANIFEST))
        for rel, expected in manifest["files"].items():
            member = tf.extractfile(PREFIX + rel)
            if member is None or digest(member.read()) != expected:
                raise ValueError(f"Archive hash mismatch: {rel}")
        for rel in REQUIRED:
            if rel not in manifest["files"]:
                raise ValueError(f"Missing restore input: {rel}")
        if not any(rel in manifest["files"] for rel in DESIGN_LOCATIONS):
            raise ValueError("Missing restore input: DESIGN_DOCUMENT.txt (root or archive)")
        if restore:
            with tempfile.TemporaryDirectory(prefix="urchin-restore-check-") as temp:
                tf.extractall(temp, filter="data")
                restored = Path(temp) / "UrchinSkipper"
                for rel, expected in manifest["files"].items():
                    if digest((restored / rel).read_bytes()) != expected:
                        raise ValueError(f"Restoration hash mismatch: {rel}")
                package = json.loads((restored / "package.json").read_text())
                assert package["name"] == "urchin-skipper"
    return len(manifest["files"])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", default="checkpoint")
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--restore-check", action="store_true")
    args = parser.parse_args()
    if args.verify:
        count = verify(args.verify.resolve(), args.restore_check)
        print(f"Verified {count} files: {args.verify}")
        return
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", args.label):
        parser.error("label must contain only letters, digits, underscores or hyphens")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive = ROOT / "checkpoints" / f"{args.label}-{stamp}.tar.gz"
    archive.parent.mkdir(exist_ok=True)
    paths = list(files())
    manifest = {"created_utc": stamp, "excluded_directories": sorted(EXCLUDE), "files": {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in paths}}
    # Exclusive creation protects an existing known-good archive even on rerun.
    with archive.open("xb") as out, tarfile.open(fileobj=out, mode="w:gz") as tf:
        for path in paths:
            tf.add(path, arcname=PREFIX + str(path.relative_to(ROOT)), recursive=False)
        data = (json.dumps(manifest, indent=2) + "\n").encode()
        info = tarfile.TarInfo(MANIFEST)
        info.size = len(data)
        tf.addfile(info, io.BytesIO(data))
    count = verify(archive, args.restore_check)
    # A concurrent edit must not be silently labelled a verified checkpoint.
    for rel, expected in manifest["files"].items():
        if digest((ROOT / rel).read_bytes()) != expected:
            raise ValueError(f"Project changed during backup; make another archive: {rel}")
    archive.with_suffix(archive.suffix + ".sha256").write_text(digest(archive.read_bytes()) + "  " + archive.name + "\n")
    print(json.dumps({"archive": str(archive.relative_to(ROOT)), "files_verified": count, "restore_checked": args.restore_check, "bytes": archive.stat().st_size}, indent=2))

if __name__ == "__main__":
    main()
