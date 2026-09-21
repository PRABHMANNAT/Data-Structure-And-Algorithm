import unittest
from transit_simulator.errors import UnknownStopError
from transit_simulator.graph import TransitGraph
from transit_simulator.models import Connection, Stop


class GraphTests(unittest.TestCase):
    def test_departures_are_sorted_and_filtered(self):
        graph = TransitGraph(); graph.add_stop(Stop("a", "A")); graph.add_stop(Stop("b", "B"))
        graph.add_connection(Connection("late", "a", "b", 20, 30, "L"))
        graph.add_connection(Connection("early", "a", "b", 10, 15, "L"))
        self.assertEqual([c.id for c in graph.departures_from("a", 15)], ["late"])

    def test_connection_requires_known_endpoints(self):
        with self.assertRaises(UnknownStopError):
            TransitGraph().add_connection(Connection("x", "a", "b", 1, 2, "L"))
