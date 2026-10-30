"""Exact LFU with LRU tie-breaking, using ordered frequency buckets."""

from collections import OrderedDict


class LFU:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.freq = {}
        self.buckets = {}
        self.minimum = 0

    def access(self, key):
        hit = key in self.freq
        evicted = None
        if hit:
            old = self.freq[key]
            del self.buckets[old][key]
            if not self.buckets[old]:
                del self.buckets[old]
                if self.minimum == old:
                    self.minimum = old + 1
            count = old + 1
        else:
            if len(self.freq) == self.capacity:
                evicted, _ = self.buckets[self.minimum].popitem(last=False)
                del self.freq[evicted]
                if not self.buckets[self.minimum]:
                    del self.buckets[self.minimum]
            count = 1
            self.minimum = 1
        self.freq[key] = count
        self.buckets.setdefault(count, OrderedDict())[key] = None
        return hit, evicted

    def snapshot(self):
        return [
            [key, self.freq[key]]
            for count in sorted(self.buckets)
            for key in self.buckets[count]
        ]
