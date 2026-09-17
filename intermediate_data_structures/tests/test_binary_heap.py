import unittest
from intermediate_data_structures.intermediate_ds.binary_heap import MinHeap
class MinHeapTests(unittest.TestCase):
    def test_sorted_removal(self):
        heap = MinHeap()
        for value in [4, 1, 3, 2]: heap.push(value)
        self.assertEqual([heap.pop() for _ in range(4)], [1, 2, 3, 4])
if __name__ == "__main__": unittest.main()
