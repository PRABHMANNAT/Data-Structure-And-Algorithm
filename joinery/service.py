from .parse import parse
from .core import optimize
from .extra import evaluate


def run(data):
    tables, joins = parse(data)
    cost, order, states = optimize(tables, joins)
    _, ledger = evaluate(order, tables, joins)
    baseline, original = evaluate([t.name for t in tables], tables, joins)
    return dict(
        metrics=[
            ["Tables", len(tables)],
            ["Optimal model cost", round(cost, 3)],
            ["Input order cost", round(baseline, 3)],
            ["DP subsets", len(states) + len(tables)],
        ],
        order=order,
        ledger=ledger,
        baseline=original,
        states=states,
        note="Estimated cardinalities assume independent predicates. Only left-deep orders and this additive scan/output cost are optimized; no SQL is executed.",
    )
