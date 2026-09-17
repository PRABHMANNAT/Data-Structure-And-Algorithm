import unittest
from intermediate_data_structures.intermediate_ds.disjoint_set import DisjointSet
class DisjointSetTests(unittest.TestCase):
    def test_union_and_find(self):
        groups = DisjointSet(["a", "b", "c"]); self.assertTrue(groups.union("a", "b"))
        self.assertEqual(groups.find("a"), groups.find("b")); self.assertNotEqual(groups.find("a"), groups.find("c"))
if __name__ == "__main__": unittest.main()
