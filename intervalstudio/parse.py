from workbench.lab_inputs import rows, whole, names
from .models import Booking


def parse(data):
    jobs = [
        Booking(n, whole(s), whole(e), whole(v))
        for n, s, e, v in rows(data, "bookings", 4, 100)
    ]
    names([j.name for j in jobs])
    start = whole(data.get("start", 0))
    end = whole(data.get("end", 10))
    if start >= end or any(j.start >= j.end for j in jobs):
        raise ValueError(
            "Every interval needs start < end; intervals are half-open [start,end)"
        )
    return jobs, start, end
