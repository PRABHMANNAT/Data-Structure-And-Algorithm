"""Pairwise comparison with indexed candidates and common-code filtering."""

from collections import Counter
from dataclasses import dataclass

from .evidence import matching_spans
from .fingerprints import fingerprints
from .index import FingerprintIndex
from .models import Match, SourceDocument, Token
from .similarity import containment, jaccard, longest_common_run
from .tokenize import normalize_tokens


@dataclass(frozen=True)
class DetectorConfig:
    k: int = 5
    window: int = 4
    min_score: float = 0.35
    min_shared: int = 1
    common_fraction: float = 0.8
    max_evidence: int = 5

    def __post_init__(self) -> None:
        if self.k < 1 or self.window < 1 or self.min_shared < 1 or self.max_evidence < 1:
            raise ValueError("k, window, min_shared, and max_evidence must be positive")
        if not 0 <= self.min_score <= 1 or not 0 < self.common_fraction <= 1:
            raise ValueError("score and common_fraction must be in range")


class Detector:
    def __init__(self, config: DetectorConfig | None = None) -> None:
        self.config = config or DetectorConfig()

    def compare(self, documents: list[SourceDocument]) -> list[Match]:
        names = [document.path for document in documents]
        if len(names) != len(set(names)):
            raise ValueError("document paths must be unique")
        by_name = {document.path: document for document in documents}
        position = {name: index for index, name in enumerate(names)}
        language_counts = Counter(document.language for document in documents)
        tokens: dict[str, list[Token]] = {}
        marks = {}
        index = FingerprintIndex()
        for document in documents:
            stream = normalize_tokens(document.text, document.language)
            tokens[document.path] = stream
            marks[document.path] = fingerprints(stream, self.config.k, self.config.window)
            index.add(document.path, marks[document.path])
        frequencies = Counter((document.language, digest)
                              for document in documents
                              for digest in {mark.digest for mark in marks[document.path]})
        # A small group of identical submissions is important evidence, not boilerplate.
        usable = {document.path: {mark.digest for mark in marks[document.path]
                                  if language_counts[document.language] < 5 or
                                  frequencies[document.language, mark.digest] /
                                  language_counts[document.language] < self.config.common_fraction}
                  for document in documents}
        found: list[Match] = []
        for i, left in enumerate(documents):
            for right_name in sorted(index.candidates(marks[left.path])):
                if position[right_name] <= i:
                    continue
                right = by_name[right_name]
                if left.language != right.language:
                    continue
                a, b = usable[left.path], usable[right.path]
                shared = len(a & b)
                if shared < self.config.min_shared:
                    continue
                overlap = containment(a, b)
                union = jaccard(a, b)
                left_values = [token.value for token in tokens[left.path]]
                right_values = [token.value for token in tokens[right.path]]
                run = longest_common_run(left_values, right_values)
                sequence = run / min(len(left_values), len(right_values)) if left_values and right_values else 0.0
                score = 0.55 * overlap + 0.30 * union + 0.15 * sequence
                if score < self.config.min_score:
                    continue
                evidence = matching_spans(tokens[left.path], tokens[right.path],
                                          self.config.k, self.config.max_evidence)
                found.append(Match(left.path, right.path, round(score, 4), round(overlap, 4),
                                   round(union, 4), round(sequence, 4), shared, evidence))
        return sorted(found, key=lambda item: (-item.score, item.left, item.right))
