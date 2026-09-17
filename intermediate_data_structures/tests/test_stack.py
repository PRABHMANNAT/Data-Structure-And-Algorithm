import unittest
from intermediate_data_structures.intermediate_ds.stack import Stack
class StackTests(unittest.TestCase):
    def test_lifo(self):
        stack = Stack(); stack.push(1); stack.push(2)
        self.assertEqual((stack.peek(), stack.pop(), stack.pop()), (2, 2, 1))
if __name__ == "__main__": unittest.main()
