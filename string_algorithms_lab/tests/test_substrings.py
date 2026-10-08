import unittest

from stringlab.common_substring import longest_common_substring
from stringlab.lcs import longest_common_subsequence
from stringlab.rotation import minimal_rotation


class SequenceTests(unittest.TestCase):
    def test_subsequence(self):
        self.assertEqual(longest_common_subsequence("ABCBDAB", "BDCABA"), "BDAB")
        self.assertEqual(longest_common_subsequence("abc", "xyz"), "")

    def test_common_substring(self):
        self.assertEqual(longest_common_substring("xabcdz", "yabcde"), "abcd")
        self.assertEqual(longest_common_substring("abc", "xyz"), "")

    def test_minimal_rotation(self):
        self.assertEqual(minimal_rotation("baca"), "abac")
        self.assertEqual(minimal_rotation("aaaa"), "aaaa")
        self.assertEqual(minimal_rotation(""), "")


if __name__ == "__main__":
    unittest.main()
