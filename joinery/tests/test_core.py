import unittest

from joinery.models import Relation
from joinery.core import optimize, cardinality
from joinery.extra import evaluate


class CoreTests(unittest.TestCase):
    def test_two_table_cost(self):
        tables = [Relation("a", 10, 1), Relation("b", 20, 1)]
        joins = {("a", "b"): 0.1}
        cost, order, _ = optimize(tables, joins)
        self.assertEqual(cost, 50)
        self.assertEqual(evaluate(order, tables, joins)[0], cost)

    def test_zero_filtered_rows(self):
        tables = [Relation("a", 100, 0), Relation("b", 200, 1)]
        self.assertEqual(optimize(tables, {("a", "b"): 0.1})[0], 200)

    def test_missing_predicate_is_cross_join(self):
        t = [Relation("a", 2, 1), Relation("b", 3, 1)]
        self.assertEqual(cardinality({"a", "b"}, t, {}), 6)
