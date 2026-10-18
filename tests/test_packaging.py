import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / (name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


class PackagingTests(unittest.TestCase):
    def test_zip_is_self_contained_and_runnable(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = module("package_skill").package(Path(directory) / "skill.zip")
            with zipfile.ZipFile(archive) as bundle:
                names = bundle.namelist()
                self.assertTrue(all(n.startswith("zhifou-oracle/") and ".." not in Path(n).parts for n in names))
                self.assertEqual(79, sum(n.endswith(".jpg") for n in names))
                self.assertIn("zhifou-oracle/LICENSE", names)
                self.assertIn("zhifou-oracle/NOTICE.md", names)
                self.assertFalse(any("__pycache__" in n for n in names))
                bundle.extractall(directory)
            result = subprocess.run([sys.executable, str(Path(directory) / "zhifou-oracle/scripts/oracle.py"),
                                     "lookup", "--hexagram", "1"], check=True, capture_output=True, text=True,
                                    cwd=directory)
            self.assertIn("乾", result.stdout)

    def test_packaging_is_reproducible(self):
        tool = module("package_skill")
        with tempfile.TemporaryDirectory() as directory:
            first = tool.package(Path(directory) / "first.zip")
            second = tool.package(Path(directory) / "second.zip")
            self.assertEqual(hashlib.sha256(first.read_bytes()).digest(), hashlib.sha256(second.read_bytes()).digest())

    def test_project_install_and_no_overwrite(self):
        installer = module("install_skill")
        with tempfile.TemporaryDirectory() as directory:
            for host, folder in (("codex", ".agents"), ("claude", ".claude")):
                destination = installer.install(host, directory)
                self.assertEqual(Path(directory).resolve() / folder / "skills/zhifou-oracle", destination)
                self.assertTrue((destination / "SKILL.md").exists())
                with self.assertRaises(FileExistsError):
                    installer.install(host, directory)

    def test_android_export_escapes_kotlin_literals_and_routes_methods(self):
        source = module("export_android").render()
        self.assertIn('"铜钱卦" -> COIN', source)
        self.assertIn('"韦特塔罗" -> TAROT', source)
        self.assertIn('"答案之书" -> ANSWER', source)
        self.assertIn("untrusted task data", source)
        self.assertIn("\\n", source)


if __name__ == "__main__":
    unittest.main()
