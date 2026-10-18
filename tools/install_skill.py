#!/usr/bin/env python3
"""Install into one explicit project's skill folder, refusing to overwrite existing files."""
import argparse
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().parents[1] / "skills/zhifou-oracle"


def install(host, project):
    if host not in ("codex", "claude"):
        raise ValueError("Unknown host")
    project = Path(project).expanduser().resolve(strict=True)
    if not project.is_dir():
        raise ValueError("Project must be a directory")
    parent = project / (".agents" if host == "codex" else ".claude") / "skills"
    if any(p.is_symlink() for p in (parent.parent, parent)):
        raise ValueError("Skill directory must not be a symlink")
    destination = parent / "zhifou-oracle"
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Existing skill was not changed; review it before updating")
    shutil.copytree(SOURCE, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("codex", "claude"), required=True)
    parser.add_argument("--project", type=Path, required=True)
    args = parser.parse_args()
    install(args.host, args.project)
    print("Installed zhifou-oracle in the selected project's skill directory")
