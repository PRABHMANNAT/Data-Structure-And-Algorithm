"""Residual network retaining separate reverse arcs for parallel/antiparallel edges."""

from dataclasses import dataclass


@dataclass
class Residual:
    target: str
    reverse: int
    remaining: int


class Network:
    def __init__(self, arcs):
        self.adj = {v: [] for a in arcs for v in (a.source, a.target)}
        self.original = []
        for arc in arcs:
            a, b = arc.source, arc.target
            i, j = len(self.adj[a]), len(self.adj[b])
            self.adj[a].append(Residual(b, j, arc.capacity))
            self.adj[b].append(Residual(a, i, 0))
            self.original.append((arc, i))

    def reachable(self, source):
        seen = {source}
        stack = [source]
        while stack:
            for edge in self.adj[stack.pop()]:
                if edge.remaining > 0 and edge.target not in seen:
                    seen.add(edge.target)
                    stack.append(edge.target)
        return seen
