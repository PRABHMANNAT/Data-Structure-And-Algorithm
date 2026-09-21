import unittest
from search_engine.snapshots import SnapshotStore
class SnapshotTests(unittest.TestCase):
 def test_restores_isolated_state_copy(self):
  s=SnapshotStore();state={"a":[1]};s.save(state);state["a"].append(2);self.assertEqual(s.restore(0),{"a":[1]})
 def test_counts_captured_revisions(self):
  s=SnapshotStore();s.save({});s.save({});self.assertEqual(len(s),2)
