#!/usr/bin/env python3
"""Build a portable skill ZIP with reproducible paths and no user data."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/zhifou-oracle"


def package(output=None):
    output = output or ROOT / "dist/zhifou-oracle-0.1.0.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_symlink():
                raise ValueError("Skill bundles must not contain symlinks")
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            name = "zhifou-oracle/" + path.relative_to(SKILL).as_posix()
            entry = zipfile.ZipInfo(name, (2026, 10, 19, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(".zip.sha256").write_text(digest + "  " + output.name + "\n", encoding="utf-8")
    print(output.name + " SHA256 " + digest)
    return output


if __name__ == "__main__":
    package()
