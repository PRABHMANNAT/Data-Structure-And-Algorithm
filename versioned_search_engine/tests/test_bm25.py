import unittest
from search_engine.bm25 import score
from search_engine.inverted_index import InvertedIndex
class BM25Tests(unittest.TestCase):
 def test_rewards_repeated_query_term(self):
  i=InvertedIndex();i.add("a","rail rail rail");i.add("b","rail");self.assertGreater(score(i,"a",["rail"],{"a":3,"b":1},2),score(i,"b",["rail"],{"a":3,"b":1},2))
