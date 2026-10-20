#!/usr/bin/env python3
"""Run a reproducible, offline product demo. Fixed imports, no LLM and no saved user data."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("zhifou_demo_oracle", ROOT / "skills/zhifou-oracle/scripts/oracle.py")
oracle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(oracle)


def run_demo():
    coin = oracle.coin_reading(values=[6, 7, 8, 9, 7, 8])
    cards = [{"card_id": "major_08", "reversed": False},
             {"card_id": "cups_02", "reversed": True},
             {"card_id": "major_14", "reversed": False}]
    tarot = oracle.tarot_reading("three-card", cards=cards)
    assert oracle.verify_receipt(coin)
    assert oracle.verify_receipt(tarot)
    tampered = copy.deepcopy(tarot)
    tampered["outcome"]["cards"][0]["reversed"] = True
    try:
        oracle.verify_receipt(tampered)
    except ValueError:
        tamper_rejected = True
    else:
        raise AssertionError("The modified reading was not rejected")
    return {
        "origin": "fixed demonstration imports, not new random draws",
        "coin": {
            "values_bottom_to_top": coin["outcome"]["values"],
            "primary": {"number": coin["primary"]["number"], "name": coin["primary"]["name"]},
            "moving_lines": coin["outcome"]["moving_positions"],
            "transformed": {"number": coin["transformed"]["number"], "name": coin["transformed"]["name"]},
            "selected_passages": [{key: row[key] for key in ("hexagram", "type", "position", "text") if key in row}
                                  for row in coin["selected_passages"]],
            "receipt_verified": True,
        },
        "tarot": {
            "spread": "three-card",
            "cards": [{"position": position["position"], "name": position["card"]["name_en"],
                       "card_id": position["card"]["id"], "reversed": position["reversed"]}
                      for position in tarot["positions"]],
            "receipt_verified": True,
            "changed_orientation_rejected": tamper_rejected,
        },
        "model_called": False,
        "sources": {"iching": oracle.ZHOUYI_SOURCE["url"], "tarot": oracle.TAROT_SOURCE["url"]},
    }


def format_demo(result, lang="en"):
    zh = lang == "zh"
    coin, tarot = result["coin"], result["tarot"]
    lines = ["ZHIFOU ORACLE / OFFLINE DEMO",
             "固定导入示例，不是一次新的随机抽取。" if zh else "Fixed imports. No new random draw. No API key.", "",
             "铜钱卦 / I CHING", "  6  7  8  9  7  8  (bottom -> top)",
             f"  #{coin['primary']['number']} {coin['primary']['name']} -> #{coin['transformed']['number']} {coin['transformed']['name']}",
             ("  动爻：" if zh else "  Moving lines: ") + ", ".join(map(str, coin["moving_lines"])),
             "  结果一致性校验：PASS" if zh else "  Receipt consistency: PASS", "", "韦特塔罗 / THREE-CARD TAROT"]
    for card in tarot["cards"]:
        orientation = ("逆位" if card["reversed"] else "正位") if zh else ("reversed" if card["reversed"] else "upright")
        lines.append(f"  {card['position']}: {card['name']} / {orientation}")
    lines.extend(["  正逆位修改被拒绝：PASS" if zh else "  Modified orientation rejected: PASS", "",
                  "未调用模型；结果与出处由本地程序提供。" if zh else "No model called. Local tools supply outcomes and sources.",
                  "一致性校验不证明占卜的预测能力。" if zh else "Consistency checks do not establish predictive validity."])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print a compact demonstration summary, not a full reading receipt")
    parser.add_argument("--lang", choices=("en", "zh"), default="en")
    args = parser.parse_args()
    result = run_demo()
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else format_demo(result, args.lang))
