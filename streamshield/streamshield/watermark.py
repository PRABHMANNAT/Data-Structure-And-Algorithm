from __future__ import annotations


class Watermark:
    """Monotonic watermark derived from the largest observed event-time."""

    def __init__(self, lateness_ms: int) -> None:
        if lateness_ms < 0: raise ValueError("lateness cannot be negative")
        self.lateness_ms, self._max_seen = lateness_ms, -1

    def observe(self, timestamp: int) -> int:
        self._max_seen = max(self._max_seen, timestamp)
        return self.value

    @property
    def value(self) -> int: return max(0, self._max_seen - self.lateness_ms)
