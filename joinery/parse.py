from workbench.lab_inputs import rows, real, names
from .models import Relation


def parse(data):
    tables = [
        Relation(n, real(r, 1, 100000), real(s, 0, 1))
        for n, r, s in rows(data, "tables", 3, 8)
    ]
    names([t.name for t in tables])
    known = {t.name for t in tables}
    joins = {}
    for a, b, s in rows(data, "joins", 3, 28):
        key = tuple(sorted((a, b)))
        if a == b or a not in known or b not in known or key in joins:
            raise ValueError(
                "Join pairs must be distinct known tables without duplicates"
            )
        joins[key] = real(s, 0, 1)
    if len(tables) < 2:
        raise ValueError("Enter at least two tables")
    return tables, joins
