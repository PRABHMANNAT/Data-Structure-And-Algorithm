from .graph import DirectedGraph

def summary(graph: DirectedGraph) -> dict[str, int]:
    return {"vertices": len(graph.vertices()), "edges": len(graph.edges())}
