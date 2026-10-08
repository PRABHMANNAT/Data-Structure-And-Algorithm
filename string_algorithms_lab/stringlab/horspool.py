"""Boyer-Moore-Horspool matching with bad-character shifts."""

from .validation import empty_positions


def find_all(text: str, pattern: str) -> list[int]:
    empty = empty_positions(text, pattern)
    if empty is not None:
        return empty
    m, n = len(pattern), len(text)
    shifts = {char: m - 1 - i for i, char in enumerate(pattern[:-1])}
    matches: list[int] = []
    start = 0
    while start <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[start + j]:
            j -= 1
        if j < 0:
            matches.append(start)
            start += 1  # preserve overlapping matches
        else:
            start += shifts.get(text[start + m - 1], m)
    return matches
