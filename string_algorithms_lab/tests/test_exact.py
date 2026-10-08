import random
import unittest

from stringlab.api import ALGORITHMS


class ExactSearchTests(unittest.TestCase):
    def test_overlaps_empty_and_unicode(self):
        cases = [("banana", "ana", [1, 3]), ("aaaa", "aa", [0, 1, 2]),
                 ("abc", "", [0, 1, 2, 3]), ("é🙂é🙂", "é🙂", [0, 2]),
                 ("abc", "abcd", []), ("", "a", [])]
        for text, pattern, expected in cases:
            for name, matcher in ALGORITHMS.items():
                with self.subTest(algorithm=name, text=text, pattern=pattern):
                    self.assertEqual(matcher(text, pattern), expected)

    def test_random_cross_check(self):
        randomizer = random.Random(42)
        for _ in range(300):
            text = "".join(randomizer.choices("ab🙂", k=randomizer.randrange(20)))
            pattern = "".join(randomizer.choices("ab🙂", k=randomizer.randrange(6)))
            expected = ALGORITHMS["naive"](text, pattern)
            for matcher in ALGORITHMS.values():
                self.assertEqual(matcher(text, pattern), expected, (text, pattern))


if __name__ == "__main__":
    unittest.main()
