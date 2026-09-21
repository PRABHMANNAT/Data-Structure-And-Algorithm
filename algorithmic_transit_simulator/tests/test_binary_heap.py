import unittest
from transit_simulator.binary_heap import MinHeap


class HeapTests(unittest.TestCase):
    def test_priority_and_insertion_order_are_preserved(self):
        heap = MinHeap[str]()
        heap.push(3, "late")
        heap.push(1, "first")
        heap.push(1, "second")
        self.assertEqual([heap.pop(), heap.pop(), heap.pop()], [(1, "first"), (1, "second"), (3, "late")])
