"""Rolling exact quartiles; outliers use the PREVIOUS full window (no leakage)."""

from collections import deque
from .core import add, remove, quantile, select, size
from .models import Reading


def rolling(values, window):
    root = None
    queue = deque()
    result = []
    for index, value in enumerate(values):
        outlier = False
        if len(queue) == window and window >= 4:
            q1, q3 = quantile(root, 0.25), quantile(root, 0.75)
            iqr = q3 - q1
            outlier = value < q1 - 1.5 * iqr or value > q3 + 1.5 * iqr
        root = add(root, value)
        queue.append(value)
        if len(queue) > window:
            root = remove(root, queue.popleft())
        result.append(
            Reading(
                index,
                value,
                size(root),
                quantile(root, 0.5),
                quantile(root, 0.25),
                quantile(root, 0.75),
                select(root, 0),
                select(root, size(root) - 1),
                outlier,
            )
        )
    return result
