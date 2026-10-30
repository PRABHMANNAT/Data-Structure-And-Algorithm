"""Order-statistic treap with duplicate counts and deterministic hash priorities."""

from hashlib import blake2b


class Node:
    def __init__(self, key):
        self.key = key
        self.count = self.size = 1
        self.left = self.right = None
        self.priority = int.from_bytes(
            blake2b(str(key).encode(), digest_size=8).digest(), "big"
        )


def size(n):
    return n.size if n else 0


def update(n):
    n.size = n.count + size(n.left) + size(n.right)
    return n


def rotate(n, left):
    p = n.right if left else n.left
    if left:
        n.right = p.left
        p.left = n
    else:
        n.left = p.right
        p.right = n
    update(n)
    return update(p)


def add(n, key):
    if not n:
        return Node(key)
    if key == n.key:
        n.count += 1
    elif key < n.key:
        n.left = add(n.left, key)
        if n.left.priority < n.priority:
            n = rotate(n, False)
    else:
        n.right = add(n.right, key)
        if n.right.priority < n.priority:
            n = rotate(n, True)
    return update(n)


def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.priority < b.priority:
        a.right = merge(a.right, b)
        return update(a)
    b.left = merge(a, b.left)
    return update(b)


def remove(n, key):
    if not n:
        raise KeyError(key)
    if key == n.key:
        if n.count > 1:
            n.count -= 1
        else:
            return merge(n.left, n.right)
    elif key < n.key:
        n.left = remove(n.left, key)
    else:
        n.right = remove(n.right, key)
    return update(n)


def select(n, rank):
    if n is None or not 0 <= rank < size(n):
        raise IndexError(rank)
    left = size(n.left)
    if rank < left:
        return select(n.left, rank)
    if rank < left + n.count:
        return n.key
    return select(n.right, rank - left - n.count)


def quantile(n, q):
    if not 0 <= q <= 1:
        raise ValueError("Quantile must be between zero and one")
    position = (size(n) - 1) * q
    lo = int(position)
    fraction = position - lo
    return (
        select(n, lo) * (1 - fraction) + select(n, min(lo + 1, size(n) - 1)) * fraction
    )
