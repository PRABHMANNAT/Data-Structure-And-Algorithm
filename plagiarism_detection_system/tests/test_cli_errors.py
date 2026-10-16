import contextlib
import io
import unittest

from plagiarism_detector.cli import main


class CliErrorTests(unittest.TestCase):
    def test_missing_path_exits_with_error(self):
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            code = main(["definitely-missing-directory"])
        self.assertEqual(code, 2)
        self.assertIn("error:", error.getvalue())

    def test_bad_threshold_exits_with_error(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main([".", "--threshold", "2"]), 2)
