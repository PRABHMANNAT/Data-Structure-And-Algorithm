import unittest
from intermediate_data_structures.intermediate_ds.linked_list import LinkedList
class LinkedListTests(unittest.TestCase):
    def test_insert_and_remove(self):
        linked = LinkedList(); linked.append("b"); linked.prepend("a")
        self.assertTrue(linked.remove("b")); self.assertEqual(list(linked), ["a"])
        self.assertFalse(linked.remove("missing"))
if __name__ == "__main__": unittest.main()
