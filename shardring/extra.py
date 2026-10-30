"""Weighted rendezvous hashing via independent exponential races."""

from math import log
from .core import token


def rendezvous(servers, key):
    # Map to the open unit interval using 52 bits (avoid float rounding to one).
    def score(server):
        u = ((token(server.name + "|" + key) >> 204) + 1) / (2**52 + 1)
        return -log(u) / server.weight, server.name

    return min(servers, key=score).name
