"""Deterministic, size-bounded discovery of supported files."""

from pathlib import Path

from .ingest import document_from_bytes
from .languages import language_for
from .models import SourceDocument

DEFAULT_EXCLUDES = {".git", ".venv", "venv", "node_modules", "__pycache__", "dist", "build"}


def discover(root: str | Path, max_bytes: int = 8_000_000,
             excludes: set[str] | None = None) -> list[SourceDocument]:
    path = Path(root).resolve()
    if not path.exists():
        raise FileNotFoundError(path)
    if max_bytes < 1:
        raise ValueError("max_bytes must be positive")
    blocked = DEFAULT_EXCLUDES | (excludes or set())
    paths = [path] if path.is_file() else path.rglob("*")
    documents: list[SourceDocument] = []
    for candidate in sorted(paths):
        if not candidate.is_file() or any(part in blocked for part in candidate.relative_to(path.parent if path.is_file() else path).parts):
            continue
        language = language_for(candidate)
        if language is None or candidate.stat().st_size > max_bytes:
            continue
        try:
            document = document_from_bytes(str(candidate), candidate.read_bytes())
        except (ValueError, OSError):
            continue
        documents.append(document)
    return documents
