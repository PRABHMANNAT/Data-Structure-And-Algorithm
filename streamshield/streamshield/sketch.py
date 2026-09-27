from __future__ import annotations

import hashlib
import math


class CountMinSketch:
    """Mergeable Count-Min Sketch: estimates never undercount."""

    def __init__(self, epsilon: float = 0.01, confidence: float = 0.99) -> None:
        if not 0 < epsilon < 1 or not 0 < confidence < 1:
            raise ValueError("epsilon and confidence must be in (0, 1)")
        self.width = math.ceil(math.e / epsilon)
        self.depth = math.ceil(math.log(1 / (1 - confidence)))
        self._table = [[0] * self.width for _ in range(self.depth)]

    def _slot(self, key: str, row: int) -> int:
        raw = hashlib.blake2b(key.encode(), digest_size=8, person=row.to_bytes(8)).digest()
        return int.from_bytes(raw) % self.width

    def add(self, key: str, amount: int = 1) -> None:
        if amount < 0: raise ValueError("sketch only supports increments")
        for row in range(self.depth): self._table[row][self._slot(key, row)] += amount

    def estimate(self, key: str) -> int:
        return min(self._table[row][self._slot(key, row)] for row in range(self.depth))

    def merge(self, other: "CountMinSketch") -> None:
        if (self.width, self.depth) != (other.width, other.depth):
            raise ValueError("incompatible sketches")
        for a, b in zip(self._table, other._table):
            for i, value in enumerate(b): a[i] += value
