import unittest
from transit_simulator.bloom_filter import BloomFilter
class BloomTests(unittest.TestCase):
 def test_never_misses_added_identifier(self):
  filter=BloomFilter();filter.add("trip-7");self.assertIn("trip-7",filter)
