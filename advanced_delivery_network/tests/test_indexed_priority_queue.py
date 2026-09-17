import unittest
from advanced_delivery_network.delivery_network.indexed_priority_queue import IndexedPriorityQueue
class IndexedPriorityQueueTests(unittest.TestCase):
    def test_decrease_key_changes_next_result(self):
        queue = IndexedPriorityQueue(); queue.push_or_decrease("a", 8); queue.push_or_decrease("b", 5); queue.push_or_decrease("a", 2)
        self.assertEqual([queue.pop(), queue.pop()], [(2, "a"), (5, "b")])
if __name__ == "__main__": unittest.main()
