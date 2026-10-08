import unittest

from stringlab.horspool import find_all


class HorspoolTests(unittest.TestCase):
    def test_shifts_and_overlaps(self):
        self.assertEqual(find_all("here is a simple example", "example"), [17])
        self.assertEqual(find_all("aaaaa", "aaa"), [0, 1, 2])
        self.assertEqual(find_all("a", "aa"), [])
        self.assertEqual(find_all("aaa", "a"), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
