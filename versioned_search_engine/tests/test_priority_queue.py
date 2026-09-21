import unittest
from search_engine.priority_queue import TopK
class TopKTests(unittest.TestCase):
 def test_retains_largest_scores(self):
  q=TopK(2);q.add(1,"a");q.add(3,"c");q.add(2,"b");self.assertEqual(q.results(),("c","b"))
