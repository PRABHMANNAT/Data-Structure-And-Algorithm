from dataclasses import dataclass


@dataclass(frozen=True)
class Workload:
    keys: list[str]
    capacity: int
