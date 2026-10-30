"""Exact circular range query, pruning by distance to each split plane."""


def within(root, x, y, radius):
    result = []
    visited = 0

    def visit(node):
        nonlocal visited
        if node is None:
            return
        visited += 1
        p = node.point
        if p.distance2(x, y) <= radius * radius:
            result.append(p)
        delta = (x if node.axis == 0 else y) - p.coordinate(node.axis)
        if delta <= radius:
            visit(node.left)
        if delta >= -radius:
            visit(node.right)

    visit(root)
    return sorted(result, key=lambda p: p.name), visited
