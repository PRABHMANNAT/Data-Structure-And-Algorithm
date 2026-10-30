import unittest, random, itertools

from dagflow.models import Task
from dagflow.core import analyze
from dagflow.extra import schedule


class OracleTests(unittest.TestCase):
    def test_random_dags_against_path_recursion(self):
        rng = random.Random(11)
        for _ in range(80):
            tasks = [
                Task(
                    str(i),
                    rng.randint(1, 9),
                    tuple(str(j) for j in range(i) if rng.random() < 0.3),
                )
                for i in range(8)
            ]
            lookup = {t.name: t for t in tasks}

            def finish(name):
                return lookup[name].duration + max(
                    (finish(p) for p in lookup[name].parents), default=0
                )

            bound = max(finish(t.name) for t in tasks)
            self.assertEqual(analyze(tasks)[-1], bound)
            for workers in [1, 2, 4]:
                rows, end = schedule(tasks, workers)
                by_name = {r["task"]: r for r in rows}
                self.assertGreaterEqual(end, bound)
                for t in tasks:
                    for parent in t.parents:
                        self.assertLessEqual(
                            by_name[parent]["end"], by_name[t.name]["start"]
                        )
                for a, b in itertools.combinations(rows, 2):
                    if a["worker"] == b["worker"]:
                        self.assertTrue(
                            a["end"] <= b["start"] or b["end"] <= a["start"]
                        )
