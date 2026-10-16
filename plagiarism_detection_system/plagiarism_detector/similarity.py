"""Set overlap and bounded sequence similarity."""

from collections import Counter


def jaccard(left: set[int], right: set[int]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def containment(left: set[int], right: set[int]) -> float:
    smaller = min(len(left), len(right))
    return len(left & right) / smaller if smaller else 0.0


def multiset_dice(left: list[str], right: list[str]) -> float:
    if not left or not right:
        return 0.0
    common = sum((Counter(left) & Counter(right)).values())
    return 2 * common / (len(left) + len(right))


def longest_common_run(left: list[str], right: list[str], limit: int = 2000) -> int:
    """Return consecutive overlap with O(min(n,m)) memory and a size cap."""
    if limit < 1:
        raise ValueError("limit must be positive")
    left, right = left[:limit], right[:limit]
    if len(right) > len(left):
        left, right = right, left
    previous = [0] * (len(right) + 1)
    best = 0
    for value in left:
        current = [0] * (len(right) + 1)
        for index, other in enumerate(right, 1):
            if value == other:
                current[index] = previous[index - 1] + 1
                best = max(best, current[index])
        previous = current
    return best
