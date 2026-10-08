"""Double polynomial hashes for strings, with O(1) window hashes."""

MODULI = (1_000_000_007, 1_000_000_009)
BASE = 911_382_323


class RollingHash:
    def __init__(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.length = len(text)
        self._powers = [[1] for _ in MODULI]
        self._prefixes = [[0] for _ in MODULI]
        for char in text:
            value = ord(char) + 1
            for power, prefix, modulus in zip(self._powers, self._prefixes, MODULI):
                power.append(power[-1] * BASE % modulus)
                prefix.append((prefix[-1] * BASE + value) % modulus)

    def digest(self, start: int, end: int) -> tuple[int, int]:
        if not (0 <= start <= end <= self.length):
            raise IndexError("invalid substring range")
        size = end - start
        return tuple((prefix[end] - prefix[start] * power[size]) % modulus
                     for power, prefix, modulus in zip(self._powers, self._prefixes, MODULI))  # type: ignore[return-value]
