import unittest

from plagiarism_detector.evidence import matching_spans
from plagiarism_detector.models import Token


class EvidenceTests(unittest.TestCase):
    def test_reports_source_lines(self):
        left = [Token(v, i + 2, 0) for i, v in enumerate("a b c d".split())]
        right = [Token(v, i + 9, 0) for i, v in enumerate("x b c d".split())]
        span = matching_spans(left, right, 3)[0]
        self.assertEqual((span.length, span.left_line, span.right_line), (3, 3, 10))
