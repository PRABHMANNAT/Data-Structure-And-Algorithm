import unittest

from plagiarism_detector.fingerprints import kgram_hashes
from plagiarism_detector.models import Token


class KGramHashTests(unittest.TestCase):
    def test_stable_and_sensitive_to_order(self):
        a = [Token(v, 1, 0) for v in ["a", "b", "c"]]
        b = [Token(v, 1, 0) for v in ["b", "a", "c"]]
        self.assertEqual(kgram_hashes(a, 2), kgram_hashes(a, 2))
        self.assertNotEqual(kgram_hashes(a, 2), kgram_hashes(b, 2))

    def test_short_stream_has_no_kgrams(self):
        self.assertEqual(kgram_hashes([Token("a", 1, 0)], 2), [])
