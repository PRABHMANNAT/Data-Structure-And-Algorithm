from hashlib import sha256

class BloomFilter:
    def __init__(self, size=128, hash_count=3): self.bits = [False] * size; self.hash_count = hash_count
    def _indices(self, value):
        raw = str(value).encode()
        for salt in range(self.hash_count):
            yield int.from_bytes(sha256(raw + bytes([salt])).digest()[:8], "big") % len(self.bits)
    def add(self, value):
        for index in self._indices(value): self.bits[index] = True
    def might_contain(self, value): return all(self.bits[index] for index in self._indices(value))
