import unittest, random, itertools

from quantilewatch.extra import rolling


class OracleTests(unittest.TestCase):
    def test_sorted_window_reference(self):
        rng = random.Random(91)
        for window in [1, 2, 4, 9, 30]:
            values = [rng.randrange(-20, 21) for _ in range(150)]
            for row in rolling(values, window):
                ordered = sorted(values[max(0, row.index - window + 1) : row.index + 1])

                def q(fraction):
                    p = (len(ordered) - 1) * fraction
                    i = int(p)
                    return ordered[i] + (
                        ordered[min(i + 1, len(ordered) - 1)] - ordered[i]
                    ) * (p - i)

                self.assertEqual(row.median, q(0.5))
                self.assertEqual(row.q1, q(0.25))
                self.assertEqual(row.q3, q(0.75))
                self.assertEqual(row.minimum, ordered[0])
                self.assertEqual(row.maximum, ordered[-1])
