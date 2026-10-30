"""Median-split 2D KD tree with exact branch-and-bound k-nearest search."""

import heapq


class Node:
    def __init__(self, points, depth=0):
        if depth == 0:
            self.ranks = {
                name: i for i, name in enumerate(sorted(p.name for p in points))
            }
        self.axis = depth % 2
        ordered = sorted(points, key=lambda p: (p.coordinate(self.axis), p.name))
        mid = len(ordered) // 2
        self.point = ordered[mid]
        self.left = Node(ordered[:mid], depth + 1) if mid else None
        self.right = (
            Node(ordered[mid + 1 :], depth + 1) if mid + 1 < len(ordered) else None
        )


def nearest(root, x, y, k):
    heap = []
    visited = []

    def visit(node):
        if node is None:
            return
        p = node.point
        visited.append(p.name)
        distance = p.distance2(x, y)
        # Unique integer tie ranks keep heap entries totally ordered.
        rank = ranks[p.name]
        entry = (-distance, -rank, p)
        if len(heap) < k:
            heapq.heappush(heap, entry)
        elif (distance, rank) < (-heap[0][0], -heap[0][1]):
            heapq.heapreplace(heap, entry)
        delta = (x if node.axis == 0 else y) - p.coordinate(node.axis)
        near, far = (node.left, node.right) if delta < 0 else (node.right, node.left)
        visit(near)
        if len(heap) < k or delta * delta <= -heap[0][0]:
            visit(far)

    ranks = root.ranks
    visit(root)
    return (
        sorted([(-d, p) for d, _, p in heap], key=lambda item: (item[0], item[1].name)),
        visited,
    )
