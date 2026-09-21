import unittest
from search_engine.document_store import DocumentStore
from search_engine.models import Document
class StoreTests(unittest.TestCase):
 def test_mutations_advance_revision(self):
  store=DocumentStore();store.put(Document("a","A","B"));self.assertEqual(store.revision,1);self.assertTrue(store.remove("a"));self.assertEqual(store.revision,2)
 def test_missing_document_is_not_removed(self):self.assertFalse(DocumentStore().remove("missing"))
