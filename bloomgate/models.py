from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    items: list[str]
    queries: list[str]
    bits: int
    hashes: int
    width: int
