"""Fixed-width Bloom bitset with stable salted hash functions."""

from hashlib import blake2b


def digest(key, salt):
    return int.from_bytes(
        blake2b(
            key.encode("utf-8"), digest_size=8, person=salt.to_bytes(8, "big")
        ).digest(),
        "big",
    )


class Bloom:
    def __init__(self, bits, hashes):
        self.bits = bits
        self.hashes = hashes
        self.array = bytearray((bits + 7) // 8)

    def positions(self, key):
        return [digest(key, i) % self.bits for i in range(self.hashes)]

    def add(self, key):
        for bit in self.positions(key):
            self.array[bit // 8] |= 1 << (bit % 8)

    def contains(self, key):
        return all(
            self.array[bit // 8] & (1 << (bit % 8)) for bit in self.positions(key)
        )

    def occupied(self):
        return sum(byte.bit_count() for byte in self.array)
