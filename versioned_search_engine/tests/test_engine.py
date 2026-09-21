import unittest
from search_engine.engine import SearchEngine
from search_engine.models import Document
class EngineTests(unittest.TestCase):
 def test_returns_ranked_document_hits(self):
  e=SearchEngine();e.add(Document("a","Rail","rail rail map"));e.add(Document("b","Bus","rail map"));self.assertEqual(e.search("rail")[0].document_id,"a")
 def test_reindexes_cache_after_document_write(self):
  e=SearchEngine();e.add(Document("a","A","rail"));e.search("rail");e.add(Document("b","B","rail rail"));self.assertEqual(e.search("rail")[0].document_id,"b")
 def test_returns_empty_for_unmatched_query(self):
  self.assertEqual(SearchEngine().search("missing"),())
