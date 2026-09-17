import unittest
from intermediate_data_structures.intermediate_ds.queue import Queue
class QueueTests(unittest.TestCase):
    def test_fifo(self):
        queue = Queue(); queue.enqueue("a"); queue.enqueue("b")
        self.assertEqual((queue.dequeue(), queue.peek()), ("a", "b"))
if __name__ == "__main__": unittest.main()
