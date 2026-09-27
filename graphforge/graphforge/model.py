from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Edge:
    source: str
    target: str
    weight: float
    def __post_init__(self) -> None:
        if not self.source or not self.target: raise ValueError("vertices cannot be empty")
        if self.weight < 0: raise ValueError("negative edges are not supported")

@dataclass(frozen=True, slots=True)
class Route:
    vertices: tuple[str, ...]
    cost: float
