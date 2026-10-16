import tempfile
import unittest
from pathlib import Path

from plagiarism_detector.files import discover


class FileExcludeTests(unittest.TestCase):
    def test_excluded_directory_is_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "generated").mkdir()
            (root / "generated" / "copy.py").write_text("x=1", encoding="utf-8")
            (root / "original.py").write_text("x=1", encoding="utf-8")
            names = [Path(doc.path).name for doc in discover(root, excludes={"generated"})]
            self.assertEqual(names, ["original.py"])
