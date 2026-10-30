import unittest, random, itertools

from math import prod
from joinery.models import Relation
from joinery.core import optimize


class OracleTests(unittest.TestCase):
    def test_permutation_reference(self):
        rng = random.Random(149)
        for _ in range(35):
            tables = [
                Relation(str(i), rng.randrange(1, 40), rng.choice([0.1, 0.5, 1]))
                for i in range(5)
            ]
            joins = {
                (a.name, b.name): rng.choice([0.01, 0.1, 0.5])
                for a, b in itertools.combinations(tables, 2)
                if rng.random() < 0.5
            }

            def cost(order):
                total = sum(t.filtered for t in order)
                for length in range(2, len(order) + 1):
                    chosen = order[:length]
                    names = {t.name for t in chosen}
                    total += prod(t.filtered for t in chosen) * prod(
                        s for (a, b), s in joins.items() if a in names and b in names
                    )
                return total

            expected = min(cost(order) for order in itertools.permutations(tables))
            actual = optimize(tables, joins)[0]
            self.assertAlmostEqual(actual, expected, places=5)
