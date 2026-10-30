"""Consistent hashing with weighted virtual nodes and clockwise ownership."""

from hashlib import sha256
from bisect import bisect_left


def token(value):
    return int.from_bytes(sha256(value.encode()).digest(), "big")


class Ring:
    def __init__(self, servers, replicas=16):
        self.entries = sorted(
            (token(f"{server.name}#{i}"), server.name)
            for server in servers
            for i in range(replicas * server.weight)
        )
        if not self.entries:
            raise ValueError("A ring needs a server")
        self.tokens = [item[0] for item in self.entries]

    def owner(self, key):
        return self.entries[
            bisect_left(self.tokens, token("key:" + key)) % len(self.entries)
        ][1]

    def preference(self, key, count):
        start = bisect_left(self.tokens, token("key:" + key))
        found = []
        for offset in range(len(self.entries)):
            name = self.entries[(start + offset) % len(self.entries)][1]
            if name not in found:
                found.append(name)
            if len(found) == count:
                break
        return found
