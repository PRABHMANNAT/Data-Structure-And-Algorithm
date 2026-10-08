"""Prefix (failure) function for Knuth-Morris-Pratt."""


def prefix_function(pattern: str) -> list[int]:
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi
