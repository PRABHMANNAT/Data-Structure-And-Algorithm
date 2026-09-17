import unittest
from advanced_delivery_network.delivery_network.disjoint_set import DisjointSet
class DisjointSetTests(unittest.TestCase):
    def test_union_merges_components(self):
        items = DisjointSet("abc"); items.union("a", "b")
        self.assertEqual(items.find("a"), items.find("b")); self.assertNotEqual(items.find("a"), items.find("c"))
if __name__ == "__main__": unittest.main()
