from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.serializer import dump, load

def test_graph_roundtrip() -> None:
    assert load(dump(DirectedGraph([Edge("a", "b", 1)]))).edges() == (Edge("a", "b", 1),)
