import unittest
from search_engine.bloom_filter import BloomFilter
class BloomTests(unittest.TestCase):
 def test_never_rejects_added_key(self):
  b=BloomFilter();b.add("doc-1");self.assertIn("doc-1",b)
 def test_supports_multiple_added_keys(self):
  b=BloomFilter();b.add("a");b.add("b");self.assertIn("b",b)
