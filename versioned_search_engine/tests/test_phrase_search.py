import unittest
from search_engine.inverted_index import InvertedIndex
from search_engine.phrase_search import phrase_matches
class PhraseTests(unittest.TestCase):
 def test_matches_adjacent_terms_only(self):
  i=InvertedIndex();i.add("a","fast train home");i.add("b","fast local train");self.assertEqual(phrase_matches(i,"fast train"),("a",))
 def test_empty_phrase_has_no_matches(self):self.assertEqual(phrase_matches(InvertedIndex(),""),())
 def test_phrase_matching_is_case_insensitive(self):
  i=InvertedIndex();i.add("a","Fast Train");self.assertEqual(phrase_matches(i,"FAST train"),("a",))
