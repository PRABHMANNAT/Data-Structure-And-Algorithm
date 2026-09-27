from __future__ import annotations

from collections import deque
from .model import Event


class SlidingWindow:
    """Timestamp-ordered exact window; expiry is amortised O(1)."""

    def __init__(self, width_ms: int) -> None:
        if width_ms <= 0: raise ValueError("width must be positive")
        self.width_ms, self._events, self._sum = width_ms, deque(), 0.0

    def add(self, event: Event) -> None:
        self._events.append(event); self._sum += event.value

    def expire(self, watermark: int) -> int:
        cutoff, expired = watermark - self.width_ms, 0
        while self._events and self._events[0].timestamp <= cutoff:
            self._sum -= self._events.popleft().value; expired += 1
        return expired

    @property
    def total(self) -> float: return self._sum
    @property
    def count(self) -> int: return len(self._events)
