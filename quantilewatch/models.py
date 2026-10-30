from dataclasses import dataclass


@dataclass(frozen=True)
class Reading:
    index: int
    value: int
    count: int
    median: float
    q1: float
    q3: float
    minimum: int
    maximum: int
    outlier: bool
