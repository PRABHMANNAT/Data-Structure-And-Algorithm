import unittest
from intermediate_data_structures.intermediate_ds.circular_queue import CircularQueue
class CircularQueueTests(unittest.TestCase):
    def test_wraps_around(self):
        queue = CircularQueue(2); queue.enqueue(1); queue.enqueue(2); self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3); self.assertEqual([queue.dequeue(), queue.dequeue()], [2, 3])
if __name__ == "__main__": unittest.main()
