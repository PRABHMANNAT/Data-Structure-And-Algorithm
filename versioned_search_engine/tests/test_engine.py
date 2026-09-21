import unittest
from search_engine.engine import SearchEngine
from search_engine.models import Document
class EngineTests(unittest.TestCase):
 def test_returns_ranked_document_hits(self):
  e=SearchEngine();e.add(Document("a","Rail","rail rail map"));e.add(Document("b","Bus","rail map"));self.assertEqual(e.search("rail")[0].document_id,"a")
