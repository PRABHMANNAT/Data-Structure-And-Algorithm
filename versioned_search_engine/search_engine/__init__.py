"""Data structure driven full-text search primitives."""
from .engine import SearchEngine
from .models import Document, SearchHit
__all__ = ["Document", "SearchEngine", "SearchHit"]
