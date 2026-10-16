import unittest

from plagiarism_detector.similarity import longest_common_run


class CommonRunTests(unittest.TestCase):
    def test_consecutive_run(self):
        self.assertEqual(longest_common_run(["a", "b", "c"], ["x", "b", "c"]), 2)

    def test_subsequence_is_not_run(self):
        self.assertEqual(longest_common_run(["a", "b", "c"], ["a", "x", "c"]), 1)
