"""Deterministic, non-preemptive list scheduling on identical workers."""

import heapq


def schedule(tasks, workers):
    pending = {t.name: t for t in tasks}
    done = set()
    running = []
    free = list(range(workers))
    heapq.heapify(free)
    now = 0
    rows = []
    while pending or running:
        while running and running[0][0] <= now:
            _, worker, name = heapq.heappop(running)
            done.add(name)
            heapq.heappush(free, worker)
        ready = sorted(
            (t for t in pending.values() if set(t.parents) <= done),
            key=lambda t: (-t.duration, t.name),
        )
        for task in ready[: len(free)]:
            worker = heapq.heappop(free)
            end = now + task.duration
            rows.append(dict(task=task.name, worker=worker + 1, start=now, end=end))
            heapq.heappush(running, (end, worker, task.name))
            del pending[task.name]
        if running:
            now = running[0][0]
        elif pending:
            raise ValueError("Dependency cycle prevents scheduling")
    return rows, now
