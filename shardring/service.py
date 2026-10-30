from collections import Counter
from .parse import parse
from .core import Ring
from .extra import rendezvous


def run(data):
    servers, added, keys, replicas = parse(data)
    after = servers + [added]
    before = Ring(servers, replicas)
    ring = Ring(after, replicas)
    assignments = []
    for key in keys:
        a, b = before.owner(key), ring.owner(key)
        ra, rb = rendezvous(servers, key), rendezvous(after, key)
        assignments.append(
            dict(
                key=key,
                before=a,
                after=b,
                moved=a != b,
                rendezvous_before=ra,
                rendezvous_after=rb,
                rendezvous_moved=ra != rb,
                replicas=ring.preference(key, min(3, len(after))),
            )
        )
    counts = Counter(row["after"] for row in assignments)
    return dict(
        metrics=[
            ["Keys", len(keys)],
            ["Virtual nodes", len(ring.entries)],
            ["Ring moves", sum(r["moved"] for r in assignments)],
            ["Rendezvous moves", sum(r["rendezvous_moved"] for r in assignments)],
        ],
        assignments=assignments,
        distribution=[[s.name, counts[s.name]] for s in after],
        ring=[[round(t / 2**256, 6), n] for t, n in ring.entries],
    )
