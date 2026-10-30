"""Dinic: BFS level graphs followed by blocking-flow DFS with current-arc indices."""

from collections import deque


def maximum(network, source, sink):
    adj = network.adj
    total = 0
    phases = []
    while True:
        level = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for edge in adj[u]:
                if edge.remaining and edge.target not in level:
                    level[edge.target] = level[u] + 1
                    queue.append(edge.target)
        if sink not in level:
            break
        cursor = {u: 0 for u in adj}
        pushed = 0

        def send(u, amount):
            if u == sink:
                return amount
            while cursor[u] < len(adj[u]):
                edge = adj[u][cursor[u]]
                if edge.remaining and level.get(edge.target) == level[u] + 1:
                    flow = send(edge.target, min(amount, edge.remaining))
                    if flow:
                        edge.remaining -= flow
                        adj[edge.target][edge.reverse].remaining += flow
                        return flow
                cursor[u] += 1
            return 0

        while True:
            value = send(source, 10**18)
            if not value:
                break
            pushed += value
            total += value
        phases.append(dict(levels=level, pushed=pushed, total=total))
    return total, phases
