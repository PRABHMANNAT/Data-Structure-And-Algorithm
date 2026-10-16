import unittest

from plagiarism_detector.fingerprints import winnow


class WinnowingTests(unittest.TestCase):
    def test_selects_rightmost_minimum(self):
        self.assertEqual([(f.digest, f.position) for f in winnow([5, 2, 2, 4], 3)],
                         [(2, 2)])

    def test_short_input_uses_one_window(self):
        self.assertEqual(winnow([7], 4)[0].position, 0)
