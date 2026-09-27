from __future__ import annotations
from .graph import DirectedGraph
from .model import Route
from .shortest_path import dijkstra

def k_shortest(graph: DirectedGraph, source: str, target: str, limit: int = 3) -> tuple[Route, ...]:
    """Small deterministic simple-path enumerator suitable for bounded route alternatives."""
    found: list[Route] = []; queue: list[tuple[tuple[str, ...], float]] = [((source,), 0.0)]
    while queue and len(found) < limit:
        path, cost = queue.pop(0); vertex = path[-1]
        if vertex == target: found.append(Route(path, cost)); continue
        for nxt, weight in graph.neighbors(vertex):
            if nxt not in path: queue.append((path + (nxt,), cost + weight))
        queue.sort(key=lambda item: (item[1], item[0]))
    return tuple(found)
