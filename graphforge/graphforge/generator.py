from .graph import DirectedGraph
from .model import Edge

def line_graph(size: int) -> DirectedGraph:
    return DirectedGraph(Edge(str(i), str(i + 1), 1) for i in range(max(0, size - 1)))
