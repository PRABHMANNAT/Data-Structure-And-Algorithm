"""Stable k-gram hashes and rightmost-minimum winnowing."""

from hashlib import blake2b

from .models import Fingerprint, Token


def kgram_hashes(tokens: list[Token], k: int) -> list[int]:
    if k < 1:
        raise ValueError("k must be positive")
    values = [token.value for token in tokens]
    return [int.from_bytes(blake2b("\x1f".join(values[i:i + k]).encode(), digest_size=8).digest(), "big")
            for i in range(len(values) - k + 1)]


def winnow(hashes: list[int], window: int) -> tuple[Fingerprint, ...]:
    if window < 1:
        raise ValueError("window must be positive")
    if not hashes:
        return ()
    width = min(window, len(hashes))
    selected: dict[int, Fingerprint] = {}
    for start in range(len(hashes) - width + 1):
        end = start + width
        minimum = min(hashes[start:end])
        position = max(index for index in range(start, end) if hashes[index] == minimum)
        selected[position] = Fingerprint(minimum, position)
    return tuple(selected[position] for position in sorted(selected))


def fingerprints(tokens: list[Token], k: int, window: int) -> tuple[Fingerprint, ...]:
    return winnow(kgram_hashes(tokens, k), window)
