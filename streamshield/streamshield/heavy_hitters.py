from __future__ import annotations


class MisraGries:
    """Tracks all keys whose frequency exceeds 1/(k+1) of the stream."""

    def __init__(self, capacity: int = 64) -> None:
        if capacity < 1: raise ValueError("capacity must be positive")
        self.capacity, self._counts = capacity, {}

    def add(self, key: str) -> None:
        if key in self._counts:
            self._counts[key] += 1
        elif len(self._counts) < self.capacity:
            self._counts[key] = 1
        else:
            self._counts = {k: v - 1 for k, v in self._counts.items() if v > 1}

    @property
    def candidates(self) -> frozenset[str]:
        return frozenset(self._counts)
