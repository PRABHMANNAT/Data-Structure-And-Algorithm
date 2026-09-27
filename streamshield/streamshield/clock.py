from __future__ import annotations

import time


class MonotonicClock:
    """Millisecond clock with non-decreasing results across wall-clock changes."""

    def __init__(self) -> None:
        self._last = 0

    def now_ms(self) -> int:
        self._last = max(self._last, time.time_ns() // 1_000_000)
        return self._last
