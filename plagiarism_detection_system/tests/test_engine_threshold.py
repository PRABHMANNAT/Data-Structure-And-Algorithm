import unittest

from plagiarism_detector import Detector, DetectorConfig, SourceDocument


class ThresholdTests(unittest.TestCase):
    def test_threshold_can_suppress_a_match(self):
        docs = [SourceDocument("a.py", "def f(x): return x + 1", "python"),
                SourceDocument("b.py", "def g(y): return y + 2", "python")]
        self.assertEqual(Detector(DetectorConfig(min_score=1.0)).compare(docs)[0].score, 1.0)

    def test_invalid_threshold_rejected(self):
        with self.assertRaises(ValueError):
            DetectorConfig(min_score=1.1)
