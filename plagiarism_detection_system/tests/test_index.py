import unittest

from plagiarism_detector.index import FingerprintIndex
from plagiarism_detector.models import Fingerprint


class IndexTests(unittest.TestCase):
    def test_candidates_and_frequency(self):
        index = FingerprintIndex()
        index.add("one", (Fingerprint(7, 0), Fingerprint(7, 1)))
        index.add("two", (Fingerprint(7, 2),))
        self.assertEqual(index.candidates((Fingerprint(7, 9),)), {"one", "two"})
        self.assertEqual(index.frequency(7), 2)
