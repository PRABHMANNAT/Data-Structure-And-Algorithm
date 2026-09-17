class HashMap:
    def __init__(self, capacity=8): self._buckets = [[] for _ in range(capacity)]; self._size = 0
    def _bucket(self, key): return self._buckets[hash(key) % len(self._buckets)]
    def __len__(self): return self._size
    def set(self, key, value):
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key: pair[1] = value; return
        bucket.append([key, value]); self._size += 1
    def get(self, key, default=None):
        for stored, value in self._bucket(key):
            if stored == key: return value
        return default
    def delete(self, key):
        bucket = self._bucket(key)
        for index, (stored, _) in enumerate(bucket):
            if stored == key: bucket.pop(index); self._size -= 1; return True
        return False
