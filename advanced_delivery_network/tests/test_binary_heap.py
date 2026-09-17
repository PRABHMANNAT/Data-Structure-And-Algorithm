import unittest
from advanced_delivery_network.delivery_network.binary_heap import BinaryMinHeap
class HeapTests(unittest.TestCase):
    def test_pop_returns_ascending_values(self):
        heap = BinaryMinHeap()
        for value in [7, 1, 4, 2]: heap.push(value)
        self.assertEqual([heap.pop() for _ in range(4)], [1, 2, 4, 7])
if __name__ == "__main__": unittest.main()
