import unittest

from plagiarism_detector.models import Match
from plagiarism_detector.report import to_text


class TextReportTests(unittest.TestCase):
    def test_empty_report_has_clear_message(self):
        self.assertIn("No matches", to_text([]))

    def test_score_and_paths_are_visible(self):
        output = to_text([Match("a", "b", 0.75, 0.8, 0.7, 0.5, 3, ())])
        self.assertIn("75.0%", output)
        self.assertIn("a", output)
