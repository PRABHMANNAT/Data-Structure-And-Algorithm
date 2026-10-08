"""Public result objects for exact search."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SearchResult:
    algorithm: str
    pattern: str
    text_length: int
    positions: tuple[int, ...]

    @property
    def count(self) -> int:
        return len(self.positions)

    def as_dict(self) -> dict[str, object]:
        return {
            "algorithm": self.algorithm,
            "pattern": self.pattern,
            "text_length": self.text_length,
            "positions": list(self.positions),
            "count": self.count,
        }
