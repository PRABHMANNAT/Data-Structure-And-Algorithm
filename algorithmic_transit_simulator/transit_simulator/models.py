from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Stop:
    id: str
    name: str
    zone: int = 1
    accessible: bool = True


@dataclass(frozen=True, slots=True)
class Connection:
    id: str
    origin: str
    destination: str
    departure: int
    arrival: int
    line: str
    capacity: int = 100
    fare: int = 0

    def __post_init__(self) -> None:
        if self.arrival < self.departure:
            raise ValueError("arrival cannot precede departure")
        if self.capacity < 1:
            raise ValueError("capacity must be positive")

    @property
    def duration(self) -> int:
        return self.arrival - self.departure


@dataclass(frozen=True, slots=True)
class Journey:
    connections: tuple[Connection, ...] = field(default_factory=tuple)

    @property
    def arrival(self) -> int | None:
        return self.connections[-1].arrival if self.connections else None

    @property
    def fare(self) -> int:
        return sum(connection.fare for connection in self.connections)
