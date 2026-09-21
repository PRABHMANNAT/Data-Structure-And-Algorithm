from dataclasses import dataclass, field

@dataclass(frozen=True)
class Document:
    id: str
    title: str
    body: str
    links: tuple[str, ...] = field(default_factory=tuple)

@dataclass(frozen=True)
class SearchHit:
    document_id: str
    score: float
    matched_terms: tuple[str, ...]
