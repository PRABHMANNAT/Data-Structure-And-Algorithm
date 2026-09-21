import unittest
from transit_simulator.avl_tree import AVLTree
class AVLTests(unittest.TestCase):
 def test_balances_sorted_insertions_and_scans_range(self):
  tree=AVLTree()
  for n in range(8): tree.insert(n,str(n))
  self.assertLessEqual(tree.root.height,4); self.assertEqual(tree.range(2,4),[(2,"2"),(3,"3"),(4,"4")])
