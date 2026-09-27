from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class _Entry:
    key: str
    score: float


class IndexedMaxHeap:
    """Max heap with O(log n) score replacement identified by key."""

    def __init__(self) -> None:
        self._heap: list[_Entry] = []
        self._index: dict[str, int] = {}

    def set(self, key: str, score: float) -> None:
        if key in self._index:
            i = self._index[key]
            old = self._heap[i].score
            self._heap[i].score = score
            (self._up if score > old else self._down)(i)
            return
        self._index[key] = len(self._heap)
        self._heap.append(_Entry(key, score))
        self._up(len(self._heap) - 1)

    def top(self, count: int) -> list[tuple[str, float]]:
        return [(e.key, e.score) for e in sorted(self._heap, key=lambda e: (-e.score, e.key))[:count]]

    def _swap(self, a: int, b: int) -> None:
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
        self._index[self._heap[a].key], self._index[self._heap[b].key] = a, b

    def _up(self, i: int) -> None:
        while i and self._heap[(p := (i - 1) // 2)].score < self._heap[i].score:
            self._swap(i, p); i = p

    def _down(self, i: int) -> None:
        while (left := 2 * i + 1) < len(self._heap):
            right = left + 1
            child = right if right < len(self._heap) and self._heap[right].score > self._heap[left].score else left
            if self._heap[i].score >= self._heap[child].score: break
            self._swap(i, child); i = child
