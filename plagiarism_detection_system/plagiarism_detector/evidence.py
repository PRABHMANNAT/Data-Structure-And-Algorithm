"""Find nonoverlapping matching token spans for human review."""

from .models import Evidence, Token


def matching_spans(left: list[Token], right: list[Token], minimum: int = 5,
                   max_spans: int = 5) -> tuple[Evidence, ...]:
    if minimum < 1 or max_spans < 1:
        raise ValueError("minimum and max_spans must be positive")
    positions: dict[str, list[int]] = {}
    for index, token in enumerate(right):
        positions.setdefault(token.value, []).append(index)
    candidates: list[Evidence] = []
    for i, token in enumerate(left):
        for j in positions.get(token.value, ()):
            if i and j and left[i - 1].value == right[j - 1].value:
                continue
            length = 0
            while i + length < len(left) and j + length < len(right) and \
                    left[i + length].value == right[j + length].value:
                length += 1
            if length >= minimum:
                candidates.append(Evidence(i, j, length, left[i].line, right[j].line))
    candidates.sort(key=lambda span: (-span.length, span.left_start, span.right_start))
    selected: list[Evidence] = []
    for span in candidates:
        if all(span.left_start + span.length <= other.left_start or
               other.left_start + other.length <= span.left_start for other in selected):
            selected.append(span)
        if len(selected) >= max_spans:
            break
    return tuple(selected)
