import unittest

from plagiarism_detector.similarity import longest_common_run


class RunLimitTests(unittest.TestCase):
    def test_limit_caps_work(self):
        self.assertEqual(longest_common_run(["a", "b"], ["a", "b"], 1), 1)

    def test_invalid_limit_rejected(self):
        with self.assertRaises(ValueError):
            longest_common_run([], [], 0)
