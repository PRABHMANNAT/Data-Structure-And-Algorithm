"""Inverted fingerprint index for candidate retrieval."""

from collections import defaultdict

from .models import Fingerprint


class FingerprintIndex:
    def __init__(self) -> None:
        self._postings: dict[int, set[str]] = defaultdict(set)

    def add(self, name: str, fingerprints: tuple[Fingerprint, ...]) -> None:
        for item in fingerprints:
            self._postings[item.digest].add(name)

    def candidates(self, fingerprints: tuple[Fingerprint, ...]) -> set[str]:
        result: set[str] = set()
        for item in fingerprints:
            result.update(self._postings.get(item.digest, ()))
        return result

    def frequency(self, digest: int) -> int:
        return len(self._postings.get(digest, ()))
