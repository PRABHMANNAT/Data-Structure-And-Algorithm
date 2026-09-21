import unittest
from search_engine.postings import PostingList
class PostingsTests(unittest.TestCase):
 def test_tracks_sorted_document_ids_and_positions(self):
  p=PostingList();p.add("b",[2]);p.add("a",[1,3]);self.assertEqual((p.documents(),p.positions("a")),(("a","b"),(1,3)))
