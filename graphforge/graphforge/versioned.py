from __future__ import annotations
from .errors import InvalidRevision
from .graph import DirectedGraph
from .model import Edge

class VersionedGraph:
    def __init__(self) -> None: self._revisions = [DirectedGraph()]
    @property
    def head(self) -> int: return len(self._revisions) - 1
    def read(self, revision: int | None = None) -> DirectedGraph:
        revision = self.head if revision is None else revision
        if not 0 <= revision <= self.head: raise InvalidRevision(str(revision))
        return self._revisions[revision].copy()
    def commit(self, additions: tuple[Edge, ...] = (), removals: tuple[tuple[str, str], ...] = ()) -> int:
        graph = self.read()
        for source, target in removals: graph.remove(source, target)
        for edge in additions: graph.add(edge)
        self._revisions.append(graph); return self.head
