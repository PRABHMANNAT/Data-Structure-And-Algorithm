from .intervals import Interval, IntervalIndex
from .models import Connection

class PlatformScheduler:
    def __init__(self): self._platforms={}
    def reserve(self, platform: str, connection: Connection, dwell: int = 1):
        index=self._platforms.setdefault(platform,IntervalIndex())
        slot=Interval(connection.arrival,connection.arrival+dwell,connection.id)
        conflicts=index.conflicts(slot)
        if not conflicts: index.add(slot)
        return conflicts
