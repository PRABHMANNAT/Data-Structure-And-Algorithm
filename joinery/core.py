"""Selinger-style subset DP for optimal left-deep orders under a stated model."""

from math import prod


def cardinality(subset, tables, joins):
    chosen = [t for t in tables if t.name in subset]
    return prod(t.filtered for t in chosen) * prod(
        s for (a, b), s in joins.items() if a in subset and b in subset
    )


def optimize(tables, joins):
    n = len(tables)
    dp = {}
    trace = []
    for i, t in enumerate(tables):
        dp[1 << i] = (t.filtered, (t.name,))
    for mask in range(1, 1 << n):
        if mask in dp:
            continue
        subset = {tables[i].name for i in range(n) if mask >> i & 1}
        output = cardinality(subset, tables, joins)
        candidates = []
        for i, t in enumerate(tables):
            if mask >> i & 1:
                cost, order = dp[mask ^ (1 << i)]
                candidate = cost + t.filtered + output
                candidates.append((candidate, order + (t.name,)))
        dp[mask] = min(candidates)
        trace.append(
            dict(
                tables=sorted(subset), rows=output, cost=dp[mask][0], order=dp[mask][1]
            )
        )
    cost, order = dp[(1 << n) - 1]
    return cost, order, trace
