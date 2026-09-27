from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True, slots=True)
class Event:
    key: str
    timestamp: int
    value: float = 1.0
    labels: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.key:
            raise ValueError("event key cannot be empty")
        if self.timestamp < 0:
            raise ValueError("timestamp must be non-negative")
