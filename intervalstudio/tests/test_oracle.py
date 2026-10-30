import unittest, random, itertools

from intervalstudio.models import Booking
from intervalstudio.core import insert, overlaps
from intervalstudio.extra import optimal


class OracleTests(unittest.TestCase):
    def test_all_subsets_and_linear_overlap(self):
        rng = random.Random(51)
        for _ in range(70):
            jobs = []
            root = None
            for i in range(8):
                start = rng.randrange(12)
                job = Booking(
                    str(i), start, start + rng.randint(1, 6), rng.randrange(20)
                )
                jobs.append(job)
                root = insert(root, job)
            best = 0
            for mask in range(1 << len(jobs)):
                chosen = [j for i, j in enumerate(jobs) if mask >> i & 1]
                if all(
                    not a.overlaps(b.start, b.end)
                    for a, b in itertools.combinations(chosen, 2)
                ):
                    best = max(best, sum(j.value for j in chosen))
            self.assertEqual(optimal(jobs)[0], best)
            start = rng.randrange(12)
            end = start + 3
            self.assertEqual(
                overlaps(root, start, end),
                sorted(j.name for j in jobs if j.overlaps(start, end)),
            )
