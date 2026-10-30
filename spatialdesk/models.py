from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    name: str
    x: float
    y: float

    def coordinate(self, axis):
        return self.x if axis == 0 else self.y

    def distance2(self, x, y):
        return (self.x - x) ** 2 + (self.y - y) ** 2
