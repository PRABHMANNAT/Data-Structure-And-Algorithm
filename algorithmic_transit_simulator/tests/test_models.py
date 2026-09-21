import unittest

from transit_simulator.models import Connection, Journey, Stop


class ModelTests(unittest.TestCase):
    def test_stop_is_immutable_and_connection_exposes_duration(self):
        stop = Stop("a", "Atlas", zone=2)
        trip = Connection("c1", "a", "b", 10, 25, "Blue", fare=4)
        self.assertEqual((stop.name, trip.duration), ("Atlas", 15))

    def test_connection_rejects_backwards_times(self):
        with self.assertRaises(ValueError):
            Connection("bad", "a", "b", 10, 9, "Blue")

    def test_connection_rejects_nonpositive_capacity(self):
        with self.assertRaises(ValueError):
            Connection("bad", "a", "b", 1, 2, "Blue", capacity=0)

    def test_journey_aggregates_arrival_and_fare(self):
        trip = Connection("c1", "a", "b", 10, 25, "Blue", fare=4)
        self.assertEqual((Journey((trip,)).arrival, Journey((trip,)).fare), (25, 4))
