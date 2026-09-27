from graphforge.astar import astar
from graphforge.graph import DirectedGraph
from graphforge.model import Edge
def test_zero_heuristic_matches_dijkstra() -> None: assert astar(DirectedGraph([Edge("a", "b", 2)]), "a", "b", lambda _: 0).cost == 2
