import unittest

from plagiarism_detector import Detector, SourceDocument


class CommonCodeTests(unittest.TestCase):
    def test_three_identical_submissions_are_still_reported(self):
        docs = [SourceDocument(f"{n}.py", "def f(x): return x + 1", "python")
                for n in range(3)]
        self.assertEqual(len(Detector().compare(docs)), 3)

    def test_code_shared_by_entire_large_corpus_is_ignored(self):
        docs = [SourceDocument(f"{n}.py", "def f(x): return x + 1", "python")
                for n in range(5)]
        self.assertEqual(Detector().compare(docs), [])
