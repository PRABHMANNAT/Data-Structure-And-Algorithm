from dataclasses import dataclass


@dataclass(frozen=True)
class Server:
    name: str
    weight: int
