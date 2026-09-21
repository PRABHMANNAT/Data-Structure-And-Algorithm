from dataclasses import dataclass

@dataclass(frozen=True)
class Interval:
    start: int; end: int; value: object
    def overlaps(self, other): return self.start < other.end and other.start < self.end

class IntervalIndex:
    """Sorted interval collection optimized for small platform schedules."""
    def __init__(self): self._intervals=[]
    def add(self, interval):
        if interval.end <= interval.start: raise ValueError("interval must have positive length")
        self._intervals.append(interval); self._intervals.sort(key=lambda item:item.start)
    def conflicts(self, interval):
        return [item for item in self._intervals if item.overlaps(interval)]
