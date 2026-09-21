import unittest
from transit_simulator.graph import TransitGraph
from transit_simulator.models import Connection, Stop
from transit_simulator.router import EarliestArrivalRouter


class RouterTests(unittest.TestCase):
    def test_finds_earliest_feasible_multileg_journey(self):
        graph = TransitGraph()
        for name in "abc": graph.add_stop(Stop(name, name.upper()))
        graph.add_connection(Connection("ab", "a", "b", 5, 10, "Blue"))
        graph.add_connection(Connection("bc", "b", "c", 12, 20, "Red"))
        graph.add_connection(Connection("ac", "a", "c", 6, 30, "Green"))
        result = EarliestArrivalRouter(graph).route("a", "c", 0)
        self.assertEqual(([edge.id for edge in result.connections], result.arrival), (["ab", "bc"], 20))

    def test_skips_connection_that_violates_transfer_buffer(self):
        graph = TransitGraph()
        for name in "abc": graph.add_stop(Stop(name, name.upper()))
        graph.add_connection(Connection("ab", "a", "b", 1, 10, "Blue"))
        graph.add_connection(Connection("too-soon", "b", "c", 11, 14, "Red"))
        graph.add_connection(Connection("valid", "b", "c", 12, 15, "Red"))
        self.assertEqual(EarliestArrivalRouter(graph, 2).route("a", "c", 0).connections[-1].id, "valid")

    def test_returns_none_when_destination_is_unreachable(self):
        graph = TransitGraph(); graph.add_stop(Stop("a", "A")); graph.add_stop(Stop("b", "B"))
        self.assertIsNone(EarliestArrivalRouter(graph).route("a", "b", 0))

    def test_accepts_a_connection_at_requested_departure(self):
        graph = TransitGraph(); graph.add_stop(Stop("a", "A")); graph.add_stop(Stop("b", "B"))
        graph.add_connection(Connection("exact", "a", "b", 10, 14, "L"))
        self.assertEqual(EarliestArrivalRouter(graph).route("a", "b", 10).arrival, 14)
