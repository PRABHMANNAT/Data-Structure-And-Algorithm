import unittest
from search_engine.priority_queue import TopK
class TopKTests(unittest.TestCase):
 def test_retains_largest_scores(self):
  q=TopK(2);q.add(1,"a");q.add(3,"c");q.add(2,"b");self.assertEqual(q.results(),("c","b"))
 def test_accepts_fewer_than_k_items(self):
  q=TopK(3);q.add(1,"a");self.assertEqual(q.results(),("a",))
 def test_breaks_equal_score_ties_by_value(self):
  q=TopK(2);q.add(1,"a");q.add(1,"b");self.assertEqual(q.results(),("b","a"))
