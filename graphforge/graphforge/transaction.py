from __future__ import annotations
from contextlib import contextmanager
from collections.abc import Iterator
from .model import Edge
from .versioned import VersionedGraph

@contextmanager
def edit(store: VersionedGraph) -> Iterator[list[Edge]]:
    additions: list[Edge] = []
    yield additions
    store.commit(tuple(additions))
