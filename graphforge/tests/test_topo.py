from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.topo import topological_order
def test_dag_order() -> None: assert topological_order(DirectedGraph([Edge("a", "b", 1)])) == ("a", "b")
