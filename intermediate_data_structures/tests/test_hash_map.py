import unittest
from intermediate_data_structures.intermediate_ds.hash_map import HashMap
class HashMapTests(unittest.TestCase):
    def test_store_update_delete(self):
        mapping = HashMap(); mapping.set("x", 1); mapping.set("x", 2)
        self.assertEqual(mapping.get("x"), 2); self.assertTrue(mapping.delete("x"))
if __name__ == "__main__": unittest.main()
