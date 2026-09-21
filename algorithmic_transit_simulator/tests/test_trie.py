import unittest
from transit_simulator.trie import PrefixTrie

class TrieTests(unittest.TestCase):
    def test_returns_case_insensitive_limited_prefix_matches(self):
        trie = PrefixTrie(); trie.insert("Central", "c"); trie.insert("Century", "x")
        self.assertEqual(trie.search("CE", 1), ["c"])
