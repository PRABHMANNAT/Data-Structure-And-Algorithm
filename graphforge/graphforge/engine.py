from __future__ import annotations
from .astar import astar
from .cache import LRU
from .graph import DirectedGraph
from .model import Edge, Route
from .shortest_path import dijkstra
from .versioned import VersionedGraph

class RouteEngine:
    def __init__(self) -> None: self.store, self.cache = VersionedGraph(), LRU[tuple[int, str, str], Route | None]()
    def add(self, edge: Edge) -> int: return self.store.commit((edge,))
    def route(self, source: str, target: str, revision: int | None = None) -> Route | None:
        revision = self.store.head if revision is None else revision; key = (revision, source, target)
        cached = self.cache.get(key)
        if cached is not None: return cached
        route = dijkstra(self.store.read(revision), source, target); self.cache.put(key, route); return route
    def informed_route(self, source: str, target: str, heuristic) -> Route | None:
        return astar(self.store.read(), source, target, heuristic)
