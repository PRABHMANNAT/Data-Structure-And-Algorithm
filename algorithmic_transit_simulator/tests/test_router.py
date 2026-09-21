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
