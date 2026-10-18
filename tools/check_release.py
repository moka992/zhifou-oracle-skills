#!/usr/bin/env python3
"""Validate public files, local links, source integrity, and obvious secret patterns."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/zhifou-oracle"
SENSITIVE = [
    re.compile(r"/Users/[A-Za-z\u4e00-\u9fff]"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_" + r"[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bsk-" + r"[A-Za-z0-9_-]{24,}\b"),
]


def check():
    errors = []
    for path in ROOT.rglob("*"):
        if any(p in (".git", "__pycache__", "dist", ".venv") for p in path.relative_to(ROOT).parts):
            continue
        if path.is_symlink():
            errors.append("Symlink: " + path.relative_to(ROOT).as_posix())
            continue
        if not path.is_file():
            continue
        if path.name.startswith(".env") or path.suffix in (".keystore", ".jks", ".apk"):
            errors.append("Private/binary application file: " + path.name)
        if path.suffix not in (".md", ".py", ".json", ".yml", ".yaml", ".txt"):
            continue
        text = path.read_text(encoding="utf-8")
        if any(pattern.search(text) for pattern in SENSITIVE):
            errors.append("Potential secret/personal path: " + path.relative_to(ROOT).as_posix())
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                target = target.split("#")[0]
                if target and not (path.parent / target).exists():
                    errors.append("Broken local link: " + path.relative_to(ROOT).as_posix() + " -> " + target)
    manifest = json.loads((SKILL / "data/manifest.json").read_text(encoding="utf-8"))
    for filename, expected in manifest["sha256"].items():
        actual = hashlib.sha256((SKILL / "data" / filename).read_bytes()).hexdigest()
        if actual != expected:
            errors.append("Dataset checksum: " + filename)
    frontmatter = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
    if "name: zhifou-oracle" not in frontmatter or "description:" not in frontmatter:
        errors.append("Invalid skill frontmatter")
    if not (SKILL / "LICENSE").exists():
        errors.append("Packaged MIT license missing")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Release checks passed: links, data integrity, skill layout, and obvious-secret scan")


if __name__ == "__main__":
    check()
