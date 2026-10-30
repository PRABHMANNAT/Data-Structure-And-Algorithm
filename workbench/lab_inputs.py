"""Bounded text inputs for the advanced Python labs; no third-party runtime."""

import math
from .validation import integer, text


def rows(data, key, width, limit=100):
    content = text(data, key).strip()
    values = [row.split() for row in content.splitlines() if row.strip()]
    if not values or len(values) > limit or any(len(row) != width for row in values):
        raise ValueError(
            f"{key}: enter 1–{limit} lines with {width} space-separated fields each"
        )
    return values


def real(value, minimum=-1e6, maximum=1e6):
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("Expected a finite number") from None
    if not math.isfinite(number) or not minimum <= number <= maximum:
        raise ValueError(f"Number must be finite and between {minimum} and {maximum}")
    return number


def whole(value, minimum=0, maximum=1000000):
    return integer({"value": value}, "value", minimum=minimum, maximum=maximum)


def names(values):
    if any(not value or len(value) > 40 for value in values) or len(values) != len(
        set(values)
    ):
        raise ValueError("Names must be unique, nonempty and at most 40 characters")


def words(data, key, limit=300):
    values = text(data, key).replace(",", " ").split()
    if not values or len(values) > limit or any(len(value) > 80 for value in values):
        raise ValueError(f"{key}: enter 1–{limit} keys of at most 80 characters")
    return values
