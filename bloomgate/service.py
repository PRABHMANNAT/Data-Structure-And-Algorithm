from collections import Counter
from math import exp
from .parse import parse
from .core import Bloom
from .extra import Sketch


def run(data):
    c = parse(data)
    bloom = Bloom(c.bits, c.hashes)
    sketch = Sketch(c.width)
    exact = Counter(c.items)
    for key in c.items:
        bloom.add(key)
        sketch.add(key)
    checks = [
        dict(
            key=key,
            maybe=bloom.contains(key),
            present=key in exact,
            estimate=sketch.estimate(key),
            actual=exact[key],
            positions=bloom.positions(key),
        )
        for key in c.queries
    ]
    absent = sum(not r["present"] for r in checks)
    fp = sum(r["maybe"] and not r["present"] for r in checks)
    return dict(
        metrics=[
            ["Unique inserts", len(exact)],
            ["Occupied bits", bloom.occupied()],
            ["False positives", fp],
            ["Absent queries", absent],
        ],
        checks=checks,
        bits=[int(bool(bloom.array[i // 8] & (1 << (i % 8)))) for i in range(c.bits)],
        counters=sketch.rows,
        estimated_fpr=(1 - exp(-c.hashes * len(exact) / c.bits)) ** c.hashes,
        observed_fpr=fp / absent if absent else None,
    )
