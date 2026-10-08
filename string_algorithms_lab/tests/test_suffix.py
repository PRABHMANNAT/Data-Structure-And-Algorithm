import random
import unittest

from stringlab.lcp import lcp_array
from stringlab.repeated_substring import longest_repeated_substring
from stringlab.suffix_array import suffix_array
from stringlab.suffix_search import SuffixIndex


class SuffixTests(unittest.TestCase):
    def test_banana(self):
        self.assertEqual(suffix_array("banana"), [5, 3, 1, 0, 4, 2])
        self.assertEqual(lcp_array("banana"), [0, 1, 3, 0, 0, 2])
        self.assertEqual(SuffixIndex("banana").find_all("ana"), [1, 3])
        self.assertEqual(longest_repeated_substring("banana"), "ana")

    def test_random_order_and_queries(self):
        randomizer = random.Random(19)
        for _ in range(100):
            text = "".join(randomizer.choices("abc", k=randomizer.randrange(12)))
            self.assertEqual(suffix_array(text), sorted(range(len(text)), key=lambda i: text[i:]))
            index = SuffixIndex(text)
            for pattern in ("", "a", "ab", "bc", "cccc"):
                expected = [i for i in range(len(text) - len(pattern) + 1) if text.startswith(pattern, i)]
                self.assertEqual(index.find_all(pattern), expected)

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            lcp_array("abc", [0, 0, 1])


if __name__ == "__main__":
    unittest.main()
