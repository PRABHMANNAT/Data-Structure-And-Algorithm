from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    name: str
    duration: int
    parents: tuple[str, ...]
