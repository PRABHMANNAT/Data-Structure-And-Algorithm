"""Levenshtein distance with a two-row dynamic program."""


def edit_distance(left: str, right: str) -> int:
    if not isinstance(left, str) or not isinstance(right, str):
        raise TypeError("inputs must be strings")
    if len(left) < len(right):
        left, right = right, left
    previous = list(range(len(right) + 1))
    for row, char in enumerate(left, 1):
        current = [row]
        for col, other in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[col] + 1,
                               previous[col - 1] + (char != other)))
        previous = current
    return previous[-1]
