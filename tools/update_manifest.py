#!/usr/bin/env python3
"""Refresh checksums after an intentional, reviewed reference-pack change."""
import hashlib
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "skills/zhifou-oracle/data"
manifest = {
    "version": "0.1.0",
    "source_pack": "Zhifou Fortune offline reference pack, separated 2026-10-19",
    "zhouyi_source": "https://github.com/kanripo/KR1a0001",
    "zhouyi_revision": "8284adbf9e3435d713180e24f05bf75f8b7d1d96",
    "zhouyi_license": "CC-BY-SA-4.0",
    "modern_summaries_and_answers_license": "MIT",
    "sha256": {name: hashlib.sha256((DATA / name).read_bytes()).hexdigest()
               for name in ("zhouyi.json", "tarot.json", "answers.json")},
}
(DATA / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print("Updated reference-pack manifest")
