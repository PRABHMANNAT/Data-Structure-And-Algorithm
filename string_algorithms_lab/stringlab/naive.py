"""Reference exact matcher used to check optimized algorithms."""

from .validation import empty_positions


def find_all(text: str, pattern: str) -> list[int]:
    empty = empty_positions(text, pattern)
    if empty is not None:
        return empty
    return [i for i in range(len(text) - len(pattern) + 1)
            if text.startswith(pattern, i)]
