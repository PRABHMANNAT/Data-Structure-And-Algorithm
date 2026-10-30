"""Myers shortest edit script over lines, retaining frontiers for backtracking."""

from .models import Edit


def diff(a, b):
    n, m = len(a), len(b)
    v = {1: 0}
    trace = []
    for d in range(n + m + 1):
        trace.append(v.copy())
        for k in range(-d, d + 1, 2):
            x = (
                v.get(k + 1, 0)
                if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1))
                else v.get(k - 1, 0) + 1
            )
            y = x - k
            while x < n and y < m and a[x] == b[y]:
                x += 1
                y += 1
            v[k] = x
            if x >= n and y >= m:
                return backtrack(trace, a, b)


def backtrack(trace, a, b):
    x, y = len(a), len(b)
    edits = []
    for d in range(len(trace) - 1, -1, -1):
        v = trace[d]
        k = x - y
        previous = (
            k + 1
            if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1))
            else k - 1
        )
        px = v.get(previous, 0)
        py = px - previous
        while x > px and y > py:
            edits.append(Edit("equal", a[x - 1]))
            x -= 1
            y -= 1
        if d:
            if x == px:
                edits.append(Edit("insert", b[y - 1]))
                y -= 1
            else:
                edits.append(Edit("delete", a[x - 1]))
                x -= 1
    return list(reversed(edits))
