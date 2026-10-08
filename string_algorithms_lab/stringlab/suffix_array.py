"""Suffix array constructed by rank doubling."""


def suffix_array(text: str) -> list[int]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    n = len(text)
    order = list(range(n))
    ranks = [ord(char) for char in text]
    width = 1
    while width < n:
        order.sort(key=lambda i: (ranks[i], ranks[i + width] if i + width < n else -1))
        next_ranks = [0] * n
        for i in range(1, n):
            previous, current = order[i - 1], order[i]
            a = (ranks[previous], ranks[previous + width] if previous + width < n else -1)
            b = (ranks[current], ranks[current + width] if current + width < n else -1)
            next_ranks[current] = next_ranks[previous] + (a != b)
        ranks = next_ranks
        if ranks[order[-1]] == n - 1:
            break
        width *= 2
    return order
