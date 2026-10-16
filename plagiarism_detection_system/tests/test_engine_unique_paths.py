import unittest

from plagiarism_detector import Detector, SourceDocument


class UniquePathTests(unittest.TestCase):
    def test_duplicate_paths_are_rejected(self):
        docs = [SourceDocument("same.py", "x = 1", "python"),
                SourceDocument("same.py", "y = 2", "python")]
        with self.assertRaises(ValueError):
            Detector().compare(docs)
