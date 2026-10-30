from dataclasses import dataclass


@dataclass(frozen=True)
class Relation:
    name: str
    rows: float
    selectivity: float

    @property
    def filtered(self):
        return self.rows * self.selectivity
