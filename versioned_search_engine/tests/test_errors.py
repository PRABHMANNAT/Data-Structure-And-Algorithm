import unittest
from search_engine.errors import SearchError,UnknownDocumentError
class ErrorTests(unittest.TestCase):
 def test_document_error_is_search_error(self):self.assertIsInstance(UnknownDocumentError(),SearchError)
