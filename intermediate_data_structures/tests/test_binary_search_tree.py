import unittest
from intermediate_data_structures.intermediate_ds.binary_search_tree import BinarySearchTree
class BinarySearchTreeTests(unittest.TestCase):
    def test_search_and_inorder(self):
        tree = BinarySearchTree()
        for value in [5, 2, 8, 1, 3]: tree.insert(value)
        self.assertTrue(tree.contains(3)); self.assertEqual(tree.inorder(), [1, 2, 3, 5, 8])
if __name__ == "__main__": unittest.main()
