import unittest
from transit_simulator.graph import TransitGraph
from transit_simulator.models import Connection, Stop
from transit_simulator.network_analysis import connected_components, isolated_stops

class NetworkAnalysisTests(unittest.TestCase):
    def test_groups_stops_even_when_connection_is_one_way(self):
        graph = TransitGraph()
        for x in "abc": graph.add_stop(Stop(x, x))
        graph.add_connection(Connection("ab", "a", "b", 1, 2, "L"))
        self.assertEqual({frozenset(x) for x in connected_components(graph)}, {frozenset("ab"), frozenset("c")})

    def test_identifies_singleton_stop_as_isolated(self):
        graph = TransitGraph(); graph.add_stop(Stop("solo", "Solo"))
        self.assertEqual(isolated_stops(graph), {"solo"})
