from dataclasses import dataclass

@dataclass(frozen=True)
class Stop:
    code: str
    name: str

@dataclass(frozen=True)
class Edge:
    destination: str
    minutes: int

@dataclass(frozen=True)
class Route:
    stops: tuple[str, ...]
    minutes: int
