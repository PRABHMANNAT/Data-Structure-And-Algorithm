import unittest
from search_engine.deduplicator import Deduplicator
class DedupTests(unittest.TestCase):
 def test_accepts_key_only_once(self):
  d=Deduplicator();self.assertTrue(d.first_seen("x"));self.assertFalse(d.first_seen("x"))
