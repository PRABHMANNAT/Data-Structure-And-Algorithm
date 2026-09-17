import unittest
from intermediate_data_structures.intermediate_ds.priority_queue import PriorityQueue
class PriorityQueueTests(unittest.TestCase):
    def test_priority_and_stability(self):
        queue = PriorityQueue(); queue.push("later", 2); queue.push("first", 1); queue.push("second", 1)
        self.assertEqual([queue.pop(), queue.pop(), queue.pop()], ["first", "second", "later"])
if __name__ == "__main__": unittest.main()
