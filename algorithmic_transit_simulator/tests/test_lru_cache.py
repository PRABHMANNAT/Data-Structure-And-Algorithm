import unittest
from transit_simulator.lru_cache import LRUCache
class CacheTests(unittest.TestCase):
 def test_evicts_least_recently_used_key(self):
  cache=LRUCache(2); cache.put("a",1);cache.put("b",2);cache.get("a");cache.put("c",3)
  self.assertNotIn("b",cache);self.assertEqual(cache.get("a"),1)
