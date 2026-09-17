import unittest
from advanced_delivery_network.delivery_network.lru_cache import LRUCache
class LRUCacheTests(unittest.TestCase):
    def test_evicts_least_recent_value(self):
        cache = LRUCache(2); cache.set("a", 1); cache.set("b", 2); cache.get("a"); cache.set("c", 3)
        self.assertIsNone(cache.get("b")); self.assertEqual(cache.get("a"), 1)
if __name__ == "__main__": unittest.main()
