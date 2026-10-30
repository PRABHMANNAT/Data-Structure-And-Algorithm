from .parse import parse
from .core import insert, overlaps
from .extra import optimal


def run(data):
    jobs, start, end = parse(data)
    root = None
    for job in jobs:
        root = insert(root, job)
    value, chosen, dp = optimal(jobs)
    conflicts = overlaps(root, start, end)
    return dict(
        metrics=[
            ["Bookings", len(jobs)],
            ["Optimal value", value],
            ["Selected", len(chosen)],
            ["Query overlaps", len(conflicts)],
        ],
        bookings=[
            dict(name=j.name, start=j.start, end=j.end, value=j.value) for j in jobs
        ],
        chosen=[j.name for j in chosen],
        conflicts=conflicts,
        query=[start, end],
        dp=dp,
        height=root.height,
    )
