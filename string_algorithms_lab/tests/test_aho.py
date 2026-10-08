import unittest

from stringlab.aho_corasick import AhoCorasick


class AhoTests(unittest.TestCase):
    def test_suffix_outputs(self):
        engine = AhoCorasick(["he", "she", "his", "hers"])
        self.assertEqual(engine.find_all("ushers"),
                         {"he": [2], "she": [1], "his": [], "hers": [2]})

    def test_duplicates_and_overlaps(self):
        engine = AhoCorasick(["a", "aa", "a"])
        self.assertEqual(engine.find_all("aaa"), {"a": [0, 1, 2], "aa": [0, 1]})

    def test_reject_empty_patterns(self):
        for patterns in ([], [""], ["ok", ""]):
            with self.assertRaises(ValueError):
                AhoCorasick(patterns)


if __name__ == "__main__":
    unittest.main()
