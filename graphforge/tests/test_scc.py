from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.scc import strongly_connected
def test_cycle_is_component() -> None: assert ("a", "b") in strongly_connected(DirectedGraph([Edge("a", "b", 1), Edge("b", "a", 1)]))
