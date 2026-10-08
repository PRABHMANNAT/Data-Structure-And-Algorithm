"""Longest common contiguous substring with two DP rows."""


def longest_common_substring(left: str, right: str) -> str:
    if not isinstance(left, str) or not isinstance(right, str):
        raise TypeError("inputs must be strings")
    previous = [0] * (len(right) + 1)
    best_end = best_length = 0
    for i, char in enumerate(left, 1):
        current = [0] * (len(right) + 1)
        for j, other in enumerate(right, 1):
            if char == other:
                current[j] = previous[j - 1] + 1
                if current[j] > best_length:
                    best_length, best_end = current[j], i
        previous = current
    return left[best_end - best_length:best_end]
