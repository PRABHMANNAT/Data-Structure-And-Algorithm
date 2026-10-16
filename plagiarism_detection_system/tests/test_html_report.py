import unittest

from plagiarism_detector.models import Match
from plagiarism_detector.report import to_html


class HtmlReportTests(unittest.TestCase):
    def test_paths_are_escaped(self):
        html = to_html([Match("<bad>", "other", 0.5, 0.5, 0.5, 0.5, 1, ())])
        self.assertIn("&lt;bad&gt;", html)
        self.assertNotIn("<bad>", html)
