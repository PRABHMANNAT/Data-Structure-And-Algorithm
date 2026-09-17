import heapq
from itertools import count

class EventQueue:
    def __init__(self): self._events = []; self._order = count()
    def schedule(self, time, event): heapq.heappush(self._events, (time, next(self._order), event))
    def next(self):
        if not self._events: raise IndexError("no scheduled events")
        return heapq.heappop(self._events)[2]
    def __len__(self): return len(self._events)
