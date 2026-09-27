from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.traversal import bfs
def test_bfs() -> None: assert bfs(DirectedGraph([Edge("a", "b", 1)]), "a") == ("a", "b")
