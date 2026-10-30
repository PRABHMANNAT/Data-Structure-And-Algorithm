from workbench.lab_inputs import rows, real, whole, names
from .models import Point


def parse(data):
    points = [
        Point(name, real(x), real(y)) for name, x, y in rows(data, "points", 3, 150)
    ]
    names([p.name for p in points])
    return (
        points,
        real(data.get("x", 0)),
        real(data.get("y", 0)),
        whole(data.get("k", 3), 1, len(points)),
        real(data.get("radius", 5), 0),
    )
