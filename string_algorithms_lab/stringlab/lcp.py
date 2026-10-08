"""Kasai's linear-time longest-common-prefix array."""

from .suffix_array import suffix_array


def lcp_array(text: str, order: list[int] | None = None) -> list[int]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if order is None:
        order = suffix_array(text)
    n = len(text)
    if len(order) != n or set(order) != set(range(n)):
        raise ValueError("order must be a permutation of suffix positions")
    ranks = [0] * n
    for rank, position in enumerate(order):
        ranks[position] = rank
    lcp = [0] * n
    common = 0
    for position in range(n):
        rank = ranks[position]
        if rank == 0:
            common = 0
            continue
        previous = order[rank - 1]
        while position + common < n and previous + common < n and text[position + common] == text[previous + common]:
            common += 1
        lcp[rank] = common
        common = max(0, common - 1)
    return lcp
