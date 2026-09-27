from __future__ import annotations
import heapq

class MinQueue:
    """Lazy-deletion priority queue with deterministic tie breaking."""
    def __init__(self) -> None: self._heap: list[tuple[float, str]] = []
    def push(self, priority: float, item: str) -> None: heapq.heappush(self._heap, (priority, item))
    def pop(self) -> tuple[float, str]: return heapq.heappop(self._heap)
    def __bool__(self) -> bool: return bool(self._heap)
