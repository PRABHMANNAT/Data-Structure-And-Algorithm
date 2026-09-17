import unittest
from intermediate_data_structures.intermediate_ds.dynamic_array import DynamicArray
class DynamicArrayTests(unittest.TestCase):
    def test_growth_and_order(self):
        items = DynamicArray(1)
        for value in range(8): items.append(value)
        self.assertEqual(list(items), list(range(8)))
        self.assertEqual(items.pop(), 7)
    def test_bounds(self):
        with self.assertRaises(IndexError): DynamicArray().get(0)
if __name__ == "__main__": unittest.main()
