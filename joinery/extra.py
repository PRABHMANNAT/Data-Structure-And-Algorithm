"""Evaluate any order and build an incremental hash-join cost ledger."""

from .core import cardinality


def evaluate(order, tables, joins):
    lookup = {t.name: t for t in tables}
    subset = set()
    total = 0
    ledger = []
    for name in order:
        subset.add(name)
        rows = cardinality(subset, tables, joins)
        step = lookup[name].filtered + (rows if len(subset) > 1 else 0)
        total += step
        ledger.append(dict(added=name, rows=rows, step_cost=step, total=total))
    return total, ledger
