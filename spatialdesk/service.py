from .parse import parse
from .core import Node, nearest
from .extra import within


def run(data):
    points, x, y, k, radius = parse(data)
    root = Node(points)
    hits, visited = nearest(root, x, y, k)
    circle, checked = within(root, x, y, radius)
    return dict(
        metrics=[
            ["Indexed points", len(points)],
            ["Neighbors", len(hits)],
            ["kNN visits", len(visited)],
            ["Within radius", len(circle)],
        ],
        points=[[p.name, p.x, p.y] for p in points],
        query=[x, y],
        radius=radius,
        neighbors=[[p.name, round(d**0.5, 6)] for d, p in hits],
        inside=[p.name for p in circle],
        visited=visited,
        range_visits=checked,
    )
