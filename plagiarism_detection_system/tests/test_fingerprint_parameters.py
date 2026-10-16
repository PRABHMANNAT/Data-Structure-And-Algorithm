import unittest

from plagiarism_detector.fingerprints import kgram_hashes, winnow


class FingerprintParameterTests(unittest.TestCase):
    def test_invalid_k_rejected(self):
        with self.assertRaises(ValueError):
            kgram_hashes([], 0)

    def test_invalid_window_rejected(self):
        with self.assertRaises(ValueError):
            winnow([], 0)
