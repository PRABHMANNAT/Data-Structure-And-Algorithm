import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from plagiarism_detector.cli import main


class CliTests(unittest.TestCase):
    def test_json_scan_of_two_files(self):
        with tempfile.TemporaryDirectory() as folder:
            for name in ("a.py", "b.py"):
                (Path(folder) / name).write_text("def f(x): return x + 1", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = main([folder, "--format", "json"])
            self.assertEqual(result, 0)
            self.assertIn('"matches"', output.getvalue())
