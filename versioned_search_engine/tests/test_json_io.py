import tempfile,unittest
from search_engine.json_io import dump_documents,load_documents
from search_engine.models import Document
class JsonTests(unittest.TestCase):
 def test_round_trips_documents(self):
  with tempfile.TemporaryDirectory() as folder:
   path=f"{folder}/docs.json";dump_documents((Document("a","A","B"),),path);self.assertEqual(load_documents(path)[0].id,"a")
