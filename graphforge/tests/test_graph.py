from graphforge.graph import DirectedGraph
from graphforge.model import Edge
def test_neighbors_are_sorted() -> None: assert DirectedGraph([Edge("a", "c", 1), Edge("a", "b", 1)]).neighbors("a")[0][0] == "b"
