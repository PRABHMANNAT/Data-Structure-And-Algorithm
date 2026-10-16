"""Immutable values shared across the detector pipeline."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceDocument:
    path: str
    text: str
    language: str


@dataclass(frozen=True)
class Token:
    value: str
    line: int
    column: int


@dataclass(frozen=True)
class Fingerprint:
    digest: int
    position: int


@dataclass(frozen=True)
class Evidence:
    left_start: int
    right_start: int
    length: int
    left_line: int
    right_line: int


@dataclass(frozen=True)
class Match:
    left: str
    right: str
    score: float
    containment: float
    jaccard: float
    sequence: float
    shared_fingerprints: int
    evidence: tuple[Evidence, ...]
