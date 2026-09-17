import unittest
from intermediate_data_structures.intermediate_ds.trie import Trie
class TrieTests(unittest.TestCase):
    def test_words_and_prefixes(self):
        trie = Trie(); trie.add("tree")
        self.assertTrue(trie.contains("tree")); self.assertFalse(trie.contains("tre"))
        self.assertTrue(trie.starts_with("tr"))
if __name__ == "__main__": unittest.main()
