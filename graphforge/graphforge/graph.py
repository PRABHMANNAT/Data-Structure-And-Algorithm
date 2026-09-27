from __future__ import annotations
from collections import defaultdict
from collections.abc import Iterable
from .model import Edge

class DirectedGraph:
    """Immutable-friendly directed adjacency representation."""
    def __init__(self, edges: Iterable[Edge] = ()) -> None:
        self._adj: dict[str, dict[str, float]] = defaultdict(dict)
        for edge in edges: self.add(edge)
    def add(self, edge: Edge) -> None:
        self._adj[edge.source][edge.target] = edge.weight; self._adj.setdefault(edge.target, {})
    def remove(self, source: str, target: str) -> None: self._adj.get(source, {}).pop(target, None)
    def neighbors(self, vertex: str) -> tuple[tuple[str, float], ...]: return tuple(sorted(self._adj.get(vertex, {}).items()))
    def vertices(self) -> tuple[str, ...]: return tuple(sorted(self._adj))
    def edges(self) -> tuple[Edge, ...]: return tuple(Edge(a, b, w) for a in self.vertices() for b, w in self.neighbors(a))
    def copy(self) -> "DirectedGraph": return DirectedGraph(self.edges())
