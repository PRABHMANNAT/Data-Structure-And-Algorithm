import tempfile
import unittest
from pathlib import Path

from plagiarism_detector.files import discover


class FileLimitTests(unittest.TestCase):
    def test_oversized_file_is_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "large.py"
            path.write_text("a" * 10, encoding="utf-8")
            self.assertEqual(discover(folder, max_bytes=5), [])

    def test_invalid_limit_rejected(self):
        with self.assertRaises(ValueError):
            discover(".", max_bytes=0)
