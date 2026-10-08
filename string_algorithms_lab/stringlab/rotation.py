"""Booth's algorithm for the lexicographically least rotation."""


def minimal_rotation(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    n = len(text)
    if not n:
        return ""
    doubled = text + text
    i, j, offset = 0, 1, 0
    while i < n and j < n and offset < n:
        a, b = doubled[i + offset], doubled[j + offset]
        if a == b:
            offset += 1
        elif a > b:
            i += offset + 1
            if i <= j:
                i = j + 1
            offset = 0
        else:
            j += offset + 1
            if j <= i:
                j = i + 1
            offset = 0
    start = min(i, j)
    return doubled[start:start + n]
