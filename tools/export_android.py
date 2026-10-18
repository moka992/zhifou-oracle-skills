#!/usr/bin/env python3
"""Generate Kotlin prompt constants. Run explicitly; no app configuration is changed."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "skills" / "zhifou-oracle" / "prompts"


def render():
    names = ("core", "coin", "tarot", "answer", "dialogue", "daily")
    fields = []
    for name in names:
        value = (PROMPTS / (name + ".md")).read_text(encoding="utf-8").strip()
        literal = json.dumps(value, ensure_ascii=False).replace("$", "\\$")
        fields.append(f"    const val {name.upper()} = {literal}")
    return """// Generated from zhifou-oracle-skills prompts; MIT. Do not edit individual constants.
package com.zhifou.fortune

internal object OraclePrompts {
""" + "\n".join(fields) + """

    fun forReading(kind: String): String = CORE + "\\n\\n" + when (kind) {
        "铜钱卦" -> COIN
        "韦特塔罗" -> TAROT
        "答案之书" -> ANSWER
        else -> ""
    } + "\\n\\nRespond in Simplified Chinese unless the user explicitly requests another language."
}
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(), encoding="utf-8")
    print("Generated " + args.output.name)
