import unittest

from plagiarism_detector.similarity import jaccard


class JaccardTests(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(jaccard({1, 2}, {1, 2}), 1.0)

    def test_partial(self):
        self.assertAlmostEqual(jaccard({1, 2}, {2, 3}), 1 / 3)

    def test_empty(self):
        self.assertEqual(jaccard(set(), set()), 0.0)
