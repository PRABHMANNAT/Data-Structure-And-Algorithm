import unittest
from search_engine import Document,SearchEngine,SearchHit
class PublicApiTests(unittest.TestCase):
 def test_exports_primary_engine_types(self):self.assertTrue(Document and SearchEngine and SearchHit)
