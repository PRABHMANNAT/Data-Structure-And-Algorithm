import unittest

from plagiarism_detector.similarity import containment


class ContainmentTests(unittest.TestCase):
    def test_shorter_is_fully_contained(self):
        self.assertEqual(containment({1, 2}, {1, 2, 3}), 1.0)

    def test_disjoint(self):
        self.assertEqual(containment({1}, {2}), 0.0)
