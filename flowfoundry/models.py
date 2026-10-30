from dataclasses import dataclass


@dataclass(frozen=True)
class Arc:
    source: str
    target: str
    capacity: int
