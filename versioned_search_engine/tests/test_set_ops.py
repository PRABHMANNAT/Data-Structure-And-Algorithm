import unittest
from search_engine.set_ops import difference,intersect,union
class SetOpsTests(unittest.TestCase):
 def test_composes_sorted_boolean_document_sets(self):self.assertEqual((intersect(("a","b"),("b","c")),union(("a",),("b",)),difference(("a","b"),("b",))),(("b",),("a","b"),("a",)))
