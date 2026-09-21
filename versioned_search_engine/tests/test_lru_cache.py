import unittest
from search_engine.lru_cache import LRUCache
class CacheTests(unittest.TestCase):
 def test_discards_oldest_key_at_capacity(self):
  c=LRUCache(1);c.put("a",1);c.put("b",2);self.assertIsNone(c.get("a"));self.assertEqual(c.get("b"),2)
