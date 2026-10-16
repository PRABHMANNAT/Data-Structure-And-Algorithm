import unittest

from plagiarism_detector import Detector, SourceDocument


class ExactMatchTests(unittest.TestCase):
    def test_identical_files_match(self):
        code = "def square(x):\n    return x * x\n"
        docs = [SourceDocument("a.py", code, "python"), SourceDocument("b.py", code, "python")]
        matches = Detector().compare(docs)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].score, 1.0)
