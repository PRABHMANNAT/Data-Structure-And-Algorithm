import unittest, random, itertools

from textloom.core import diff
from textloom.extra import apply, invert


class OracleTests(unittest.TestCase):
    def test_minimality_against_lcs_dynamic_program(self):
        rng = random.Random(71)
        for _ in range(250):
            a = [rng.choice("abc") for _ in range(rng.randrange(15))]
            b = [rng.choice("abc") for _ in range(rng.randrange(15))]
            dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    dp[i + 1][j + 1] = (
                        dp[i][j] + 1 if x == y else max(dp[i][j + 1], dp[i + 1][j])
                    )
            edits = diff(a, b)
            self.assertEqual(
                sum(e.kind != "equal" for e in edits), len(a) + len(b) - 2 * dp[-1][-1]
            )
            self.assertEqual(apply(a, edits), b)
            self.assertEqual(apply(b, invert(edits)), a)
