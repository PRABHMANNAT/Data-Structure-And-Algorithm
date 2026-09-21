import unittest
from search_engine.trie import TermTrie
class TrieTests(unittest.TestCase):
 def test_completes_sorted_terms_from_prefix(self):
  trie=TermTrie();trie.insert("train");trie.insert("travel");self.assertEqual(trie.complete("tra"),("train","travel"))
