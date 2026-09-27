from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from .errors import LateEvent
from .heavy_hitters import MisraGries
from .indexed_heap import IndexedMaxHeap
from .model import Event
from .sketch import CountMinSketch
from .watermark import Watermark
from .window import SlidingWindow


@dataclass(frozen=True, slots=True)
class EngineStats:
    accepted: int
    rejected_late: int
    watermark: int


class StreamEngine:
    """Single-partition event-time stream processor."""

    def __init__(self, window_ms: int = 60_000, lateness_ms: int = 5_000) -> None:
        self._watermark = Watermark(lateness_ms)
        self._window = SlidingWindow(window_ms)
        self._sketch, self._heavy, self._leaders = CountMinSketch(), MisraGries(), IndexedMaxHeap()
        self._accepted = self._late = 0

    def ingest(self, event: Event) -> None:
        if event.timestamp < self._watermark.value:
            self._late += 1; raise LateEvent(f"event at {event.timestamp} precedes watermark")
        self._watermark.observe(event.timestamp); self._window.add(event)
        self._sketch.add(event.key); self._heavy.add(event.key)
        self._leaders.set(event.key, self._sketch.estimate(event.key)); self._window.expire(self._watermark.value)
        self._accepted += 1

    def leaders(self, count: int = 10) -> list[tuple[str, int]]:
        candidates = self._heavy.candidates
        return [(key, int(score)) for key, score in self._leaders.top(count) if key in candidates]

    def stats(self) -> EngineStats:
        return EngineStats(self._accepted, self._late, self._watermark.value)

    def window_total(self) -> float: return self._window.total
