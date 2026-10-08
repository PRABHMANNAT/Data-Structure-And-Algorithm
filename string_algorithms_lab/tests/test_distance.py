import unittest

from stringlab.edit_distance import edit_distance


class DistanceTests(unittest.TestCase):
    def test_insert_delete_substitute(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("abc", "abc"), 0)
        self.assertEqual(edit_distance("🙂a", "🙂b"), 1)

    def test_symmetry(self):
        for a, b in [("abc", "bca"), ("", "xyz"), ("frog", "fog")]:
            self.assertEqual(edit_distance(a, b), edit_distance(b, a))


if __name__ == "__main__":
    unittest.main()
