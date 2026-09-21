import unittest
from transit_simulator.event_queue import Event,EventQueue
class EventQueueTests(unittest.TestCase):
 def test_releases_events_in_time_order(self):
  q=EventQueue();q.schedule(Event(9,"late",None));q.schedule(Event(2,"early",None))
  self.assertEqual([x.kind for x in q.pop_ready(5)],["early"])
 def test_includes_event_at_deadline(self):
  q=EventQueue();q.schedule(Event(5,"deadline",None));self.assertEqual(q.pop_ready(5)[0].kind,"deadline")
