import unittest
from search_engine.boolean_search import evaluate
from search_engine.inverted_index import InvertedIndex
class BooleanTests(unittest.TestCase):
 def test_combines_and_negates_term_postings(self):
  i=InvertedIndex();i.add("a","red blue");i.add("b","red");self.assertEqual(evaluate(i,("red","AND","NOT","blue"),("a","b")),("b",))
