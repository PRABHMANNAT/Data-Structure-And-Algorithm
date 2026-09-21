import unittest
from transit_simulator.disjoint_set import DisjointSet

class DisjointSetTests(unittest.TestCase):
    def test_merges_components_and_avoids_duplicate_union(self):
        sets = DisjointSet(["a", "b", "c"])
        self.assertTrue(sets.union("a", "b")); self.assertFalse(sets.union("a", "b"))
        self.assertTrue(sets.connected("a", "b")); self.assertFalse(sets.connected("a", "c"))
