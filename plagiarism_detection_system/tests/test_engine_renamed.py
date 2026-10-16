import unittest

from plagiarism_detector import Detector, SourceDocument


class RenamedMatchTests(unittest.TestCase):
    def test_identifier_renaming_and_literal_changes_match(self):
        docs = [SourceDocument("a.py", "def f(x): return x + 1", "python"),
                SourceDocument("b.py", "def g(y): return y + 2", "python")]
        self.assertEqual(len(Detector().compare(docs)), 1)
