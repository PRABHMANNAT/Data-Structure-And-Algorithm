"""Anchored glob matching for '*' and '?' wildcards."""


def glob_match(text: str, pattern: str) -> bool:
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("text and pattern must be strings")
    i = j = 0
    star = -1
    retry = 0
    while i < len(text):
        if j < len(pattern) and (pattern[j] == "?" or pattern[j] == text[i]):
            i += 1
            j += 1
        elif j < len(pattern) and pattern[j] == "*":
            star = j
            retry = i
            j += 1
        elif star >= 0:
            retry += 1
            i = retry
            j = star + 1
        else:
            return False
    return all(char == "*" for char in pattern[j:])
