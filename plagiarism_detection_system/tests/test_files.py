import tempfile
import unittest
from pathlib import Path

from plagiarism_detector.files import discover


class FileDiscoveryTests(unittest.TestCase):
    def test_source_and_plain_text_files_are_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "a.py").write_text("print(1)", encoding="utf-8")
            (root / "note.txt").write_text("ignore", encoding="utf-8")
            self.assertEqual([Path(doc.path).name for doc in discover(root)], ["a.py", "note.txt"])
