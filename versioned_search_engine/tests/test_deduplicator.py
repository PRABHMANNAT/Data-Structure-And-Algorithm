import unittest
from search_engine.deduplicator import Deduplicator
class DedupTests(unittest.TestCase):
 def test_accepts_key_only_once(self):
  d=Deduplicator();self.assertTrue(d.first_seen("x"));self.assertFalse(d.first_seen("x"))
 def test_accepts_distinct_keys(self):
  d=Deduplicator();d.first_seen("x");self.assertTrue(d.first_seen("y"))
