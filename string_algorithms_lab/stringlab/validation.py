"""Shared input rules for matching functions."""


def validate_text_pattern(text: str, pattern: str) -> None:
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("text and pattern must be strings")


def empty_positions(text: str, pattern: str) -> list[int] | None:
    """An empty pattern matches at every boundary, including the end."""
    validate_text_pattern(text, pattern)
    return list(range(len(text) + 1)) if not pattern else None


def validate_patterns(patterns: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    values = tuple(patterns)
    if not values or any(not isinstance(p, str) or not p for p in values):
        raise ValueError("patterns must contain at least one nonempty string")
    return tuple(dict.fromkeys(values))
