import random
import unittest

from stringlab.palindrome import longest_palindrome


class PalindromeTests(unittest.TestCase):
    def test_examples_and_ties(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome(""), "")
        self.assertEqual(longest_palindrome("a#a"), "a#a")

    def test_against_brute_force(self):
        randomizer = random.Random(81)
        for _ in range(100):
            text = "".join(randomizer.choices("ab#", k=randomizer.randrange(12)))
            candidates = [(text[i:j], i) for i in range(len(text) + 1)
                          for j in range(i, len(text) + 1) if text[i:j] == text[i:j][::-1]]
            expected = min(candidates, key=lambda pair: (-len(pair[0]), pair[1]))[0]
            self.assertEqual(longest_palindrome(text), expected)


if __name__ == "__main__":
    unittest.main()
