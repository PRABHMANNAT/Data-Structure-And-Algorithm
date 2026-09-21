import unittest
from transit_simulator.disruptions import DisruptionBoard
from transit_simulator.graph import TransitGraph
from transit_simulator.models import Connection,Stop
from transit_simulator.resilience import operational_graph
class ResilienceTests(unittest.TestCase):
 def test_removes_cancelled_edges_from_operational_network(self):
  graph=TransitGraph();graph.add_stop(Stop("a","A"));graph.add_stop(Stop("b","B"));graph.add_connection(Connection("x","a","b",1,2,"L"));board=DisruptionBoard();board.cancel("x")
  self.assertEqual(operational_graph(graph,board).connections(),())
