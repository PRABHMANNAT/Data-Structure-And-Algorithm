import unittest
from search_engine.inverted_index import InvertedIndex
class IndexTests(unittest.TestCase):
 def test_replaces_previous_document_terms(self):
  i=InvertedIndex();i.add("a","red blue");i.add("a","green");self.assertEqual(i.documents("red"),());self.assertEqual(i.documents("green"),("a",))
 def test_removes_document_postings(self):
  i=InvertedIndex();i.add("a","red");i.remove("a");self.assertEqual(i.documents("red"),())
