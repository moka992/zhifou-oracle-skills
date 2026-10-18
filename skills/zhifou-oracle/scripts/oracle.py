#!/usr/bin/env python3
"""Local draws and source lookup. Python standard library only; no network access."""

import argparse
import hashlib
import json
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = 1
RNG = random.SystemRandom()
ZHOUYI_SOURCE = {
    "work": "Zhou Yi received Chinese text, Kanseki KR1a0001",
    "url": "https://github.com/kanripo/KR1a0001",
    "revision": "8284adbf9e3435d713180e24f05bf75f8b7d1d96",
    "license": "CC-BY-SA-4.0",
}
TAROT_SOURCE = {
    "historical_reference": "A. E. Waite, The Pictorial Key to the Tarot (1910)",
    "url": "https://en.wikisource.org/wiki/The_Pictorial_Key_to_the_Tarot",
    "meaning_text": "Original modern Chinese summaries, not a verbatim Waite translation",
    "summary_license": "MIT",
    "artwork": "Pamela Colman Smith, Rider, 1909; see NOTICE.md for source notices",
}
SAFE_ALMANAC = frozenset([
    "开市", "开工", "赴任", "上任", "求职", "交易", "立券", "入学", "求学", "习艺",
    "修造", "扫舍", "会亲友", "嫁娶", "纳采", "订盟", "出行", "纳财", "开仓", "置产",
])
SPREADS = {
    "single": [("focus", "关注点")],
    "three-card": [("situation", "当前状况"), ("challenge", "主要挑战"), ("next_step", "下一步")],
    "celtic-cross": [
        ("present", "核心现状"), ("crossing", "交叉阻力"), ("crown", "意识目标"),
        ("foundation", "深层基础"), ("past", "近期过去"), ("near_future", "近期发展"),
        ("self", "自我立场"), ("environment", "外部环境"), ("hopes_fears", "希望与担忧"),
        ("outlook", "综合趋向"),
    ],
}


def load_data(name):
    return json.loads((ROOT / "data" / (name + ".json")).read_text(encoding="utf-8"))


def require_int(value, minimum, maximum, label):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{label} must be an integer in {minimum}..{maximum}")
    return value


def reading_receipt(method, origin, outcome):
    canonical = json.dumps({"method": method, "origin": origin, "outcome": outcome},
                           ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {"schema_version": SCHEMA_VERSION, "method": method, "origin": origin,
            "outcome": outcome, "receipt_sha256": hashlib.sha256(canonical.encode()).hexdigest()}


def select_passages(primary, transformed, moving):
    """One declared Zhu Xi-style policy; not a universal rule for all I Ching schools."""
    def judgment(h, role="primary"):
        return {"hexagram": h["number"], "name": h["name"], "type": "judgment",
                "role": role, "text": h["judgment"]}

    def line(h, position, role="primary"):
        return {"hexagram": h["number"], "name": h["name"], "type": "line",
                "position": position, "role": role, "text": h["lines"][position - 1],
                "commentary": h["line_commentaries"][position - 1]}

    n = len(moving)
    if n == 0:
        return [judgment(primary)]
    if n == 1:
        return [line(primary, moving[0])]
    if n == 2:
        return [line(primary, moving[1]), line(primary, moving[0], "supporting")]
    if n == 3:
        return [judgment(primary), judgment(transformed, "supporting")]
    unchanged = [p for p in range(1, 7) if p not in moving]
    if n == 4:
        return [line(transformed, unchanged[0]), line(transformed, unchanged[1], "supporting")]
    if n == 5:
        return [line(transformed, unchanged[0])]
    if primary["number"] in (1, 2) and primary.get("use_text"):
        return [{"hexagram": primary["number"], "name": primary["name"],
                 "type": "use_nine" if primary["number"] == 1 else "use_six",
                 "role": "primary", "text": primary["use_text"],
                 "commentary": primary.get("use_commentary", "")}]
    return [judgment(transformed)]


def coin_reading(values=None, coins=None, rng=None):
    rng = rng or RNG
    if values is not None and coins is not None:
        raise ValueError("Supply values or coin faces, not both")
    origin = "generated" if values is None and coins is None else "imported"
    if coins is None and values is None:
        coins = [[rng.choice((2, 3)) for _ in range(3)] for _ in range(6)]
    if coins is not None:
        if not isinstance(coins, list) or len(coins) != 6:
            raise ValueError("A cast needs six three-coin rows, bottom to top")
        for row in coins:
            if not isinstance(row, list) or len(row) != 3:
                raise ValueError("Each line needs exactly three coin faces")
            for face in row:
                require_int(face, 2, 3, "Coin face")
        values = [sum(row) for row in coins]
    if not isinstance(values, list) or len(values) != 6:
        raise ValueError("A cast needs six values, bottom to top")
    for value in values:
        require_int(value, 6, 9, "Line value")
    primary_pattern = "".join("1" if v in (7, 9) else "0" for v in values)
    changed_pattern = "".join("1" if v in (6, 7) else "0" for v in values)
    by_pattern = {h["pattern"]: h for h in load_data("zhouyi")}
    primary, transformed = by_pattern[primary_pattern], by_pattern[changed_pattern]
    moving = [i + 1 for i, value in enumerate(values) if value in (6, 9)]
    outcome = {"line_order": "bottom-to-top", "values": values,
               "moving_positions": moving, "primary_number": primary["number"],
               "transformed_number": transformed["number"],
               "primary_pattern": primary_pattern, "transformed_pattern": changed_pattern}
    if coins is not None:
        outcome["coins"] = coins
    result = reading_receipt("iching-three-coins", origin, outcome)
    result.update({"selection_policy": "zhu-xi-changing-lines-v1", "primary": primary,
                   "transformed": transformed if moving else None,
                   "selected_passages": select_passages(primary, transformed, moving),
                   "source": dict(ZHOUYI_SOURCE)})
    return result


def tarot_reading(spread="celtic-cross", cards=None, rng=None):
    rng = rng or RNG
    if spread not in SPREADS:
        raise ValueError("Unknown spread")
    deck = {card["id"]: card for card in load_data("tarot")}
    positions = SPREADS[spread]
    origin = "generated" if cards is None else "imported"
    if cards is None:
        ids = rng.sample(list(deck), len(positions))
        cards = [{"card_id": cid, "reversed": bool(rng.getrandbits(1))} for cid in ids]
    if not isinstance(cards, list) or len(cards) != len(positions):
        raise ValueError(f"{spread} requires {len(positions)} cards")
    ids = []
    for card in cards:
        if not isinstance(card, dict) or card.get("card_id") not in deck:
            raise ValueError("Unknown card ID")
        if type(card.get("reversed")) is not bool:
            raise ValueError("Each card needs an explicit boolean reversed value")
        ids.append(card["card_id"])
    if len(set(ids)) != len(ids):
        raise ValueError("A spread cannot contain duplicate cards")
    outcome = {"spread": spread, "significator": None,
               "cards": [{"card_id": card["card_id"], "reversed": card["reversed"]} for card in cards]}
    result = reading_receipt("rider-waite-smith", origin, outcome)
    result["positions"] = [
        {"number": i + 1, "position": pos[0], "position_zh": pos[1],
         "reversed": card["reversed"], "card": deck[card["card_id"]]}
        for i, (pos, card) in enumerate(zip(positions, cards))
    ]
    result["tradition"] = "Waite Celtic method, ten drawn positions, no separate significator" if spread == "celtic-cross" else "Modern reflection spread; not attributed to Waite's Celtic method"
    result["source"] = dict(TAROT_SOURCE)
    return result


def answer_reading(page=None, rng=None):
    entries = load_data("answers")
    if page is None:
        entry = (rng or RNG).choice(entries)
    else:
        require_int(page, 1, len(entries), "Page")
        entry = entries[page - 1]
    result = reading_receipt("original-reflection", "generated" if page is None else "imported", entry)
    result["source"] = "Original Zhifou reflection entries; not a commercial Book of Answers"
    return result


def verify_receipt(record):
    if not isinstance(record, dict) or record.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Unsupported reading schema")
    outcome, method, origin = record.get("outcome"), record.get("method"), record.get("origin")
    if origin not in ("generated", "imported") or not isinstance(outcome, dict):
        raise ValueError("Invalid receipt origin or outcome")
    expected = reading_receipt(method, origin, outcome)["receipt_sha256"]
    if record.get("receipt_sha256") != expected:
        raise ValueError("Receipt checksum does not match")
    if method == "iching-three-coins":
        if not isinstance(outcome.get("values"), list):
            raise ValueError("Receipt needs explicit line values")
        rebuilt = coin_reading(coins=outcome["coins"]) if "coins" in outcome else coin_reading(values=outcome.get("values"))
        for key in ("selection_policy", "primary", "transformed", "selected_passages", "source"):
            if record.get(key) != rebuilt.get(key):
                raise ValueError("Reading metadata disagrees with the cast: " + key)
    elif method == "rider-waite-smith":
        if not isinstance(outcome.get("cards"), list):
            raise ValueError("Receipt needs explicit cards")
        rebuilt = tarot_reading(outcome.get("spread"), outcome.get("cards"))
        for key in ("positions", "tradition", "source"):
            if record.get(key) != rebuilt.get(key):
                raise ValueError("Reading metadata disagrees with the spread: " + key)
    elif method == "original-reflection":
        require_int(outcome.get("page"), 1, 100, "Page")
        rebuilt = answer_reading(outcome.get("page"))
        if outcome != rebuilt["outcome"] or record.get("source") != rebuilt.get("source"):
            raise ValueError("Unknown or modified reflection entry")
    else:
        raise ValueError("Unsupported reading method")
    if outcome != rebuilt["outcome"]:
        raise ValueError("Outcome fields disagree with their derived values")
    return True


def read_json(path):
    p = Path(path)
    if p.stat().st_size > 2_000_000:
        raise ValueError("Input JSON exceeds 2 MB")
    return json.loads(p.read_text(encoding="utf-8"))


def clean_context(raw):
    if not isinstance(raw, dict):
        raise ValueError("Context must be a JSON object")
    allowed = {"date", "lunar_date", "day_ganzhi", "solar_term", "focus_keywords", "almanac_yi", "almanac_ji"}
    if set(raw) - allowed:
        raise ValueError("Unexpected context fields; include only relevant nonsecret calendar and focus data")
    result = {"provenance": "caller-provided; not independently calculated or verified"}
    for key, value in raw.items():
        if key in ("almanac_yi", "almanac_ji", "focus_keywords"):
            if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
                raise ValueError(key + " must be a string list")
            value = [v.strip() for v in value]
            if key != "focus_keywords":
                value = [v for v in value if v in SAFE_ALMANAC]
            result[key] = list(dict.fromkeys(v[:80] for v in value))[:8]
        else:
            if not isinstance(value, str):
                raise ValueError(key + " must be a string")
            result[key] = value[:120]
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    coin = commands.add_parser("coin", help="Cast or import six lines, bottom to top")
    imported = coin.add_mutually_exclusive_group()
    imported.add_argument("--lines", help="Six comma-separated integers in 6..9")
    imported.add_argument("--coins", help="JSON containing six arrays of three 2/3 faces")
    tarot = commands.add_parser("tarot", help="Draw or import unique cards")
    tarot.add_argument("--spread", choices=SPREADS, default="celtic-cross")
    tarot.add_argument("--cards", help="JSON list of card_id and boolean reversed objects")
    answer = commands.add_parser("answer", help="Draw an original reflection entry")
    answer.add_argument("--page", type=int)
    for cmd in (coin, tarot, answer):
        questions = cmd.add_mutually_exclusive_group()
        questions.add_argument("--question")
        questions.add_argument("--question-stdin", action="store_true")
        cmd.add_argument("--context", type=Path, help="Optional caller-provided context JSON")
    lookup = commands.add_parser("lookup", help="Look up source text without drawing")
    target = lookup.add_mutually_exclusive_group(required=True)
    target.add_argument("--hexagram", type=int)
    target.add_argument("--card")
    verify = commands.add_parser("verify", help="Validate an existing receipt without drawing")
    verify.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "coin":
            values = [int(v.strip()) for v in args.lines.split(",")] if args.lines else None
            result = coin_reading(values=values, coins=json.loads(args.coins) if args.coins else None)
        elif args.command == "tarot":
            result = tarot_reading(args.spread, json.loads(args.cards) if args.cards else None)
        elif args.command == "answer":
            result = answer_reading(args.page)
        elif args.command == "verify":
            verify_receipt(read_json(args.file))
            result = {"valid": True, "note": "Consistency check, not cryptographic authentication of a physical draw"}
        elif args.hexagram is not None:
            require_int(args.hexagram, 1, 64, "Hexagram")
            result = dict(load_data("zhouyi")[args.hexagram - 1], source=dict(ZHOUYI_SOURCE))
        else:
            cards = {card["id"]: card for card in load_data("tarot")}
            if args.card not in cards:
                raise ValueError("Unknown card ID")
            result = dict(cards[args.card], source=dict(TAROT_SOURCE))
        if args.command in ("coin", "tarot", "answer"):
            question = sys.stdin.read(2001) if args.question_stdin else (args.question or "")
            if len(question) > 2000:
                raise ValueError("Question exceeds 2000 characters")
            result["question"] = question.strip()
            if args.context:
                result["context"] = clean_context(read_json(args.context))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        # Do not echo private questions, imported text, paths, or provider credentials on error.
        print(json.dumps({"error": "Invalid reading input", "category": type(exc).__name__}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
