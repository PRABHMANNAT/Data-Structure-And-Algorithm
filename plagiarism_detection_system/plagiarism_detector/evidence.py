"""Find nonoverlapping matching token spans for human review."""

from .models import Evidence, Token


def matching_spans(left: list[Token], right: list[Token], minimum: int = 5,
                   max_spans: int = 5) -> tuple[Evidence, ...]:
    if minimum < 1 or max_spans < 1:
        raise ValueError("minimum and max_spans must be positive")
    if len(left) < minimum or len(right) < minimum:
        return ()
    positions: dict[tuple[str, ...], list[int]] = {}
    right_values = [token.value for token in right]
    left_values = [token.value for token in left]
    for index in range(len(right) - minimum + 1):
        key = tuple(right_values[index:index + minimum])
        bucket = positions.setdefault(key, [])
        if len(bucket) < 100:
            bucket.append(index)
    candidates: list[Evidence] = []
    checked = 0
    for i in range(len(left) - minimum + 1):
        key = tuple(left_values[i:i + minimum])
        for j in positions.get(key, ()):
            checked += 1
            if checked > 50_000:
                break
            if i and j and left_values[i - 1] == right_values[j - 1]:
                continue
            length = minimum
            while i + length < len(left) and j + length < len(right) and \
                    left_values[i + length] == right_values[j + length]:
                length += 1
            candidates.append(Evidence(i, j, length, left[i].line, right[j].line))
        if checked > 50_000:
            break
    candidates.sort(key=lambda span: (-span.length, span.left_start, span.right_start))
    selected: list[Evidence] = []
    for span in candidates:
        if all(span.left_start + span.length <= other.left_start or
               other.left_start + other.length <= span.left_start for other in selected):
            selected.append(span)
        if len(selected) >= max_spans:
            break
    return tuple(selected)
