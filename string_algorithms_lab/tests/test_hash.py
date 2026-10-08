import unittest

from stringlab.rabin_karp import find_all
from stringlab.rolling_hash import RollingHash


class HashTests(unittest.TestCase):
    def test_equal_windows(self):
        rolling = RollingHash("abcabc")
        self.assertEqual(rolling.digest(0, 3), rolling.digest(3, 6))
        self.assertNotEqual(rolling.digest(0, 2), rolling.digest(1, 3))

    def test_invalid_ranges(self):
        rolling = RollingHash("abc")
        for start, end in [(-1, 1), (2, 1), (0, 4)]:
            with self.assertRaises(IndexError):
                rolling.digest(start, end)

    def test_verified_matches(self):
        self.assertEqual(find_all("ababa", "aba"), [0, 2])
        self.assertEqual(find_all("abc", "xyz"), [])


if __name__ == "__main__":
    unittest.main()
