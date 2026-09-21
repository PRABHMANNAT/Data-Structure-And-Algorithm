import unittest
from search_engine.query_parser import parse
class ParserTests(unittest.TestCase):
 def test_normalizes_operators_and_terms(self):self.assertEqual(parse("Fast AND (train OR bus)"),("fast","AND","(","train","OR","bus",")"))
 def test_rejects_blank_query(self):
  from search_engine.errors import QuerySyntaxError
  with self.assertRaises(QuerySyntaxError):parse("   ")
