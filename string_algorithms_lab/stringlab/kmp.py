"""Linear-time exact matching with the prefix function."""

from .prefix import prefix_function
from .validation import empty_positions


def find_all(text: str, pattern: str) -> list[int]:
    empty = empty_positions(text, pattern)
    if empty is not None:
        return empty
    pi = prefix_function(pattern)
    positions: list[int] = []
    j = 0
    for i, char in enumerate(text):
        while j and char != pattern[j]:
            j = pi[j - 1]
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            positions.append(i - j + 1)
            j = pi[j - 1]
    return positions
