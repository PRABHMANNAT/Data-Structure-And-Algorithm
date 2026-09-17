import unittest
from advanced_delivery_network.delivery_network.trie import Trie
class TrieTests(unittest.TestCase):
    def test_suggests_values_by_prefix(self):
        trie = Trie(); trie.add("airport", "A"); trie.add("apex", "X")
        self.assertEqual(trie.suggest("ap"), ["X"]); self.assertEqual(trie.suggest("a"), ["A", "X"])
if __name__ == "__main__": unittest.main()
