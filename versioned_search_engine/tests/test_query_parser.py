import unittest
from search_engine.query_parser import parse
class ParserTests(unittest.TestCase):
 def test_normalizes_operators_and_terms(self):self.assertEqual(parse("Fast AND (train OR bus)"),("fast","AND","(","train","OR","bus",")"))
