from .graph import DirectedGraph

def validate(graph: DirectedGraph, max_vertices: int = 100_000) -> None:
    if len(graph.vertices()) > max_vertices: raise ValueError("graph exceeds configured vertex limit")
