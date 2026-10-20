import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("demo", ROOT / "tools/demo.py")
demo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(demo)


class DemoTests(unittest.TestCase):
    def test_demo_is_reproducible_and_never_requests_a_random_draw(self):
        with patch.object(demo.oracle.RNG, "sample", side_effect=AssertionError("must not redraw")), \
             patch.object(demo.oracle.RNG, "choice", side_effect=AssertionError("must not cast")):
            first = demo.run_demo()
            self.assertEqual(first, demo.run_demo())
        self.assertEqual([1, 4], first["coin"]["moving_lines"])
        self.assertFalse(first["model_called"])
        self.assertTrue(first["tarot"]["changed_orientation_rejected"])

    def test_cards_and_orientations_match_the_published_case(self):
        cards = demo.run_demo()["tarot"]["cards"]
        self.assertEqual(["major_08", "cups_02", "major_14"], [row["card_id"] for row in cards])
        self.assertEqual([False, True, False], [row["reversed"] for row in cards])
        self.assertEqual(["situation", "challenge", "next_step"], [row["position"] for row in cards])

    def test_human_output_identifies_fixed_imports_and_no_model_call(self):
        text = demo.format_demo(demo.run_demo())
        self.assertIn("Fixed imports", text)
        self.assertIn("No model called", text)
        self.assertIn("reversed", text)
        self.assertIn("固定导入", demo.format_demo(demo.run_demo(), "zh"))

    def test_demo_runs_from_another_directory_and_outputs_valid_json(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/demo.py"), "--json"],
                                cwd=ROOT.parent, check=True, capture_output=True, text=True)
        data = json.loads(result.stdout)
        self.assertTrue(data["coin"]["receipt_verified"])
        self.assertNotIn(str(ROOT), result.stdout)
