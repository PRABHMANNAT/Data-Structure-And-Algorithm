import unittest

from dagflow.models import Task
from dagflow.core import analyze
from dagflow.extra import schedule


class CoreTests(unittest.TestCase):
    def test_critical_slack(self):
        t = [Task("a", 4, ()), Task("b", 2, ()), Task("c", 1, ("a", "b"))]
        order, early, late, _, finish = analyze(t)
        self.assertEqual(finish, 5)
        self.assertEqual(late["b"] - early["b"], 2)

    def test_cycle(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            analyze([Task("a", 1, ("b",)), Task("b", 1, ("a",))])

    def test_one_worker(self):
        rows, end = schedule([Task("a", 2, ()), Task("b", 3, ())], 1)
        self.assertEqual(end, 5)
        self.assertEqual(rows[0]["task"], "b")
