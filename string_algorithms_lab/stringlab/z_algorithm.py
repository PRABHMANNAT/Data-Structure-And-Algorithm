"""Z array: longest prefix beginning at every sequence position."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def z_values(values: Sequence[T]) -> list[int]:
    z = [0] * len(values)
    left = right = 0
    for i in range(1, len(values)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(values) and values[z[i]] == values[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z
