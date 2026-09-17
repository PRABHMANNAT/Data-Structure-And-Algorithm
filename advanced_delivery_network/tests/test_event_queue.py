import unittest
from advanced_delivery_network.delivery_network.event_queue import EventQueue
class EventQueueTests(unittest.TestCase):
    def test_orders_events_and_preserves_ties(self):
        queue = EventQueue(); queue.schedule(5, "later"); queue.schedule(3, "first"); queue.schedule(3, "second")
        self.assertEqual([queue.next(), queue.next(), queue.next()], ["first", "second", "later"])
if __name__ == "__main__": unittest.main()
