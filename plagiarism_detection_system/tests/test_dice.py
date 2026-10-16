import unittest

from plagiarism_detector.similarity import multiset_dice


class DiceTests(unittest.TestCase):
    def test_repeated_tokens_count(self):
        self.assertAlmostEqual(multiset_dice(["a", "a", "b"], ["a", "b"]), 4 / 5)

    def test_empty(self):
        self.assertEqual(multiset_dice([], ["a"]), 0.0)
