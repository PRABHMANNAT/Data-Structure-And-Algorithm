"""Kahn topological ordering and forward/backward critical-path passes."""

import heapq


def analyze(tasks):
    lookup = {t.name: t for t in tasks}
    children = {t.name: [] for t in tasks}
    degree = {t.name: len(t.parents) for t in tasks}
    for task in tasks:
        for parent in task.parents:
            children[parent].append(task.name)
    ready = [name for name, d in degree.items() if d == 0]
    heapq.heapify(ready)
    order = []
    early = {}
    while ready:
        name = heapq.heappop(ready)
        order.append(name)
        early[name] = max(
            (early[p] + lookup[p].duration for p in lookup[name].parents), default=0
        )
        for child in children[name]:
            degree[child] -= 1
            if degree[child] == 0:
                heapq.heappush(ready, child)
    if len(order) != len(tasks):
        raise ValueError(
            "Dependency cycle: "
            + ", ".join(sorted(name for name, d in degree.items() if d))
        )
    finish = max(early[n] + lookup[n].duration for n in order)
    late = {}
    for name in reversed(order):
        late[name] = (
            min((late[c] for c in children[name]), default=finish)
            - lookup[name].duration
        )
    return order, early, late, children, finish
