from dataclasses import dataclass


@dataclass(frozen=True)
class Booking:
    name: str
    start: int
    end: int
    value: int

    def overlaps(self, start, end):
        return self.start < end and start < self.end
