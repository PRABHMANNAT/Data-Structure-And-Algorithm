"""Weighted interval scheduling: predecessor binary search + optimal substructure."""

from bisect import bisect_right


def optimal(jobs):
    ordered = sorted(jobs, key=lambda j: (j.end, j.start, j.name))
    ends = [j.end for j in ordered]
    dp = [0]
    parents = []
    for i, job in enumerate(ordered):
        parent = bisect_right(ends, job.start, 0, i)
        parents.append(parent)
        dp.append(max(dp[-1], job.value + dp[parent]))
    chosen = []
    i = len(ordered)
    while i:
        job = ordered[i - 1]
        parent = parents[i - 1]
        if job.value + dp[parent] > dp[i - 1]:
            chosen.append(job)
            i = parent
        else:
            i -= 1
    return dp[-1], list(reversed(chosen)), dp
