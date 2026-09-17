import unittest
from intermediate_data_structures.intermediate_ds.deque import Deque
class DequeTests(unittest.TestCase):
    def test_both_ends(self):
        items = Deque(); items.append_left(2); items.append_right(3); items.append_left(1)
        self.assertEqual((items.pop_left(), items.pop_right()), (1, 3))
if __name__ == "__main__": unittest.main()
