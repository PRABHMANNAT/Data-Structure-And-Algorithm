"""An unrelated sieve example for the demonstration corpus."""


def primes_below(limit):
    is_prime = [True] * limit
    if limit > 0:
        is_prime[0] = False
    if limit > 1:
        is_prime[1] = False
    factor = 2
    while factor * factor < limit:
        if is_prime[factor]:
            for multiple in range(factor * factor, limit, factor):
                is_prime[multiple] = False
        factor += 1
    return [number for number, valid in enumerate(is_prime) if valid]
