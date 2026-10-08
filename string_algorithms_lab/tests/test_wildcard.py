import unittest

from stringlab.wildcard import glob_match


class WildcardTests(unittest.TestCase):
    def test_anchored_glob(self):
        cases = [("adceb", "*a*b", True), ("acdcb", "a*c?b", False),
                 ("", "*", True), ("", "?", False), ("abc", "a?c", True),
                 ("abc", "a*d", False), ("abc", "***", True)]
        for text, pattern, expected in cases:
            with self.subTest(text=text, pattern=pattern):
                self.assertEqual(glob_match(text, pattern), expected)


if __name__ == "__main__":
    unittest.main()
