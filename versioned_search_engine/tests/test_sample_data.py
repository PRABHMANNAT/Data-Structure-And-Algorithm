import unittest
from pathlib import Path
from search_engine.json_io import load_documents
class DataTests(unittest.TestCase):
 def test_sample_corpus_has_linked_documents(self):self.assertEqual(len(load_documents(Path(__file__).parents[1]/"data"/"sample_documents.json")),3)
