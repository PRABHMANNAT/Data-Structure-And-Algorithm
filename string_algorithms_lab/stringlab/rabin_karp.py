"""Rolling-hash exact search; candidates are verified against the text."""

from .rolling_hash import RollingHash
from .validation import empty_positions


def find_all(text: str, pattern: str) -> list[int]:
    empty = empty_positions(text, pattern)
    if empty is not None:
        return empty
    if len(pattern) > len(text):
        return []
    haystack = RollingHash(text)
    target = RollingHash(pattern).digest(0, len(pattern))
    return [i for i in range(len(text) - len(pattern) + 1)
            if haystack.digest(i, i + len(pattern)) == target
            and text.startswith(pattern, i)]
