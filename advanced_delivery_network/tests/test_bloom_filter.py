import unittest
from advanced_delivery_network.delivery_network.bloom_filter import BloomFilter
class BloomFilterTests(unittest.TestCase):
    def test_added_values_are_never_false_negatives(self):
        filter_ = BloomFilter(); filter_.add("blocked-road")
        self.assertTrue(filter_.might_contain("blocked-road"))
if __name__ == "__main__": unittest.main()
