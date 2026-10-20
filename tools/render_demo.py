#!/usr/bin/env python3
"""Render the real reproducible CLI output as a code-native SVG, without model-generated artwork."""
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

from demo import format_demo, run_demo


def render(output):
    lines = ["$ python3 tools/demo.py", ""] + format_demo(run_demo()).splitlines()
    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    def element(name, **attributes):
        return ET.SubElement(root, "{" + namespace + "}" + name, {k.replace("_", "-"): str(v) for k, v in attributes.items()})
    height = 108 + len(lines) * 29
    root = ET.Element("{" + namespace + "}svg", {"viewBox": f"0 0 1120 {height}", "width": "1120", "height": str(height), "role": "img"})
    element("title").text = "Reproducible offline I Ching and tarot tool output; no model was called"
    element("rect", width=1120, height=height, rx=8, fill="#171B23")
    element("text", x=38, y=43, fill="#AEBBD0", font_family="system-ui, sans-serif", font_size=16).text = "ZHIFOU ORACLE SKILLS  /  REPRODUCIBLE LOCAL DEMO"
    element("line", x1=38, y1=65, x2=1082, y2=65, stroke="#384354")
    for index, text in enumerate(lines):
        color = "#7FE1B1" if "PASS" in text or text.startswith("$") else "#F1F5FA"
        if text.startswith("Fixed") or text.startswith("Consistency"):
            color = "#BCC8D9"
        element("text", x=38, y=103 + index * 29, fill=color,
                font_family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace", font_size=19).text = text
    output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(output, encoding="utf-8", xml_declaration=True)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "docs/assets/offline-demo.svg")
    print("Rendered " + render(parser.parse_args().output).name)
