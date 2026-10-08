"""Exact search via a Z array and a guaranteed unique sentinel."""

from .validation import empty_positions
from .z_algorithm import z_values


def find_all(text: str, pattern: str) -> list[int]:
    empty = empty_positions(text, pattern)
    if empty is not None:
        return empty
    combined: list[object] = [*pattern, object(), *text]
    z = z_values(combined)
    start = len(pattern) + 1
    return [i - start for i in range(start, len(z)) if z[i] >= len(pattern)]
