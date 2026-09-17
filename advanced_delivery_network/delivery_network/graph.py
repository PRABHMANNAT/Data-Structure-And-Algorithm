from .errors import DuplicateStopError, UnknownStopError
from .models import Edge, Stop

class DeliveryGraph:
    def __init__(self): self._stops = {}; self._adjacency = {}
    def add_stop(self, stop):
        if stop.code in self._stops: raise DuplicateStopError(stop.code)
        self._stops[stop.code] = stop; self._adjacency[stop.code] = {}
    def stop(self, code):
        if code not in self._stops: raise UnknownStopError(code)
        return self._stops[code]
    def add_connection(self, first, second, minutes, bidirectional=True):
        if minutes < 0: raise ValueError("minutes cannot be negative")
        self.stop(first); self.stop(second); self._adjacency[first][second] = Edge(second, minutes)
        if bidirectional: self._adjacency[second][first] = Edge(first, minutes)
    def neighbors(self, code): self.stop(code); return tuple(self._adjacency[code].values())
    def codes(self): return tuple(self._stops)
