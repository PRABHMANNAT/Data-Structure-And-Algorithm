import unittest
from search_engine.link_graph import LinkGraph
class LinkGraphTests(unittest.TestCase):
 def test_recommends_two_hop_documents(self):
  g=LinkGraph();g.add("a","b");g.add("b","c");self.assertEqual(g.recommend("a"),("c",))
 def test_excludes_source_from_recommendations(self):
  g=LinkGraph();g.add("a","b");g.add("b","a");self.assertEqual(g.recommend("a"),())
 def test_returns_empty_for_leaf_document(self):self.assertEqual(LinkGraph().recommend("leaf"),())
