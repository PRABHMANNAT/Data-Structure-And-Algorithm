"""Count-Min Sketch: minimum across independent nonnegative counter rows."""

from .core import digest


class Sketch:
    def __init__(self, width, depth=4):
        self.width = width
        self.depth = depth
        self.rows = [[0] * width for _ in range(depth)]

    def add(self, key, count=1):
        if count < 0:
            raise ValueError("Count-Min requires nonnegative increments")
        for row in range(self.depth):
            self.rows[row][digest(key, row + 100) % self.width] += count

    def estimate(self, key):
        return min(
            self.rows[row][digest(key, row + 100) % self.width]
            for row in range(self.depth)
        )
