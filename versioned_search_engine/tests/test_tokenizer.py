import unittest
from search_engine.tokenizer import term_positions,tokenize
class TokenizerTests(unittest.TestCase):
 def test_normalizes_words_and_preserves_positions(self):
  self.assertEqual(tokenize("Fast, FAST trains!"),["fast","fast","trains"]);self.assertEqual(term_positions("go go now")["go"],[0,1])
