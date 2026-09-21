from __future__ import annotations

from collections import defaultdict
from .errors import UnknownStopError
from .models import Connection, Stop


class TransitGraph:
    def __init__(self) -> None:
        self.stops: dict[str, Stop] = {}
        self._outgoing: dict[str, list[Connection]] = defaultdict(list)

    def add_stop(self, stop: Stop) -> None:
        self.stops[stop.id] = stop

    def add_connection(self, connection: Connection) -> None:
        if connection.origin not in self.stops or connection.destination not in self.stops:
            raise UnknownStopError("connections require known endpoint stops")
        self._outgoing[connection.origin].append(connection)
        self._outgoing[connection.origin].sort(key=lambda item: (item.departure, item.arrival, item.id))

    def departures_from(self, stop_id: str, earliest: int = 0) -> tuple[Connection, ...]:
        if stop_id not in self.stops:
            raise UnknownStopError(stop_id)
        return tuple(item for item in self._outgoing[stop_id] if item.departure >= earliest)

    def connections(self) -> tuple[Connection, ...]:
        return tuple(item for values in self._outgoing.values() for item in values)
