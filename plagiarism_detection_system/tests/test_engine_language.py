import unittest

from plagiarism_detector import Detector, SourceDocument


class LanguageIsolationTests(unittest.TestCase):
    def test_different_languages_are_not_compared(self):
        docs = [SourceDocument("a.py", "return value + 1", "python"),
                SourceDocument("b.js", "return value + 1", "javascript")]
        self.assertEqual(Detector().compare(docs), [])
