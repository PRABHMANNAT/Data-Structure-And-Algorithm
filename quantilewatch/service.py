from dataclasses import asdict
from .parse import parse
from .extra import rolling


def run(data):
    values, window = parse(data)
    trace = rolling(values, window)
    return dict(
        metrics=[
            ["Samples", len(values)],
            ["Window", window],
            ["Final median", trace[-1].median],
            ["Outliers", sum(r.outlier for r in trace)],
        ],
        trace=[asdict(r) for r in trace],
        values=values,
    )
