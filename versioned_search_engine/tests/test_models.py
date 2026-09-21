import unittest
from search_engine.models import Document,SearchHit
class ModelTests(unittest.TestCase):
 def test_document_and_hit_are_immutable_values(self):
  self.assertEqual(Document("1","T","B").id, "1");self.assertEqual(SearchHit("1",1.0,("x",)).score,1.0)
