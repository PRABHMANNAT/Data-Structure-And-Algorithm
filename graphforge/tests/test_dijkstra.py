from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.shortest_path import dijkstra
def test_shortest_route() -> None: assert dijkstra(DirectedGraph([Edge("a", "b", 1), Edge("b", "c", 1), Edge("a", "c", 5)]), "a", "c").cost == 2
