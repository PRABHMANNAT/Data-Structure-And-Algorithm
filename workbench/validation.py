"""Small, explicit input contracts shared by the project adapters."""
import math


def text(data, key, default="", limit=12000):
    value = data.get(key, default)
    if not isinstance(value, str) or len(value) > limit:
        raise ValueError(f"{key} must be text with at most {limit} characters")
    return value


def integer(data, key, default=0, minimum=-1000000, maximum=1000000):
    value = data.get(key, default)
    if isinstance(value, bool):
        raise ValueError(f"{key} must be a whole number")
    try:
        result = int(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{key} must be a whole number") from None
    if str(result) != str(value).strip() or not minimum <= result <= maximum:
        raise ValueError(f"{key} must be a whole number from {minimum} to {maximum}")
    return result


def numbers(data, key="values", limit=100):
    raw = text(data, key, "7, 3, 9, 1, 5")
    parts = raw.replace(",", " ").split()
    if not parts or len(parts) > limit:
        raise ValueError(f"Enter 1–{limit} integers separated by commas or spaces")
    return [integer({"v": part}, "v") for part in parts]


def lines(data, key, limit=100):
    rows = [row.strip() for row in text(data, key).splitlines() if row.strip()]
    if not rows or len(rows) > limit:
        raise ValueError(f"{key} needs 1–{limit} nonempty rows")
    return rows


def edges(data):
    output = []
    for row in lines(data, "edges", 80):
        fields = row.replace(",", " ").split()
        if len(fields) != 3:
            raise ValueError("Each edge must contain: origin destination weight")
        source, target, weight = fields
        try:
            cost = float(weight)
        except ValueError:
            raise ValueError("Edge weights must be numbers") from None
        if not math.isfinite(cost) or cost < 0 or cost > 1000000:
            raise ValueError("Edge weights must be finite, nonnegative, and at most 1000000")
        output.append((source, target, cost))
    return output
