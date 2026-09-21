import re
_WORD = re.compile(r"[a-z0-9]+")
def tokenize(text: str) -> list[str]:
    return _WORD.findall(text.casefold())
def term_positions(text: str) -> dict[str, list[int]]:
    result = {}
    for position, token in enumerate(tokenize(text)): result.setdefault(token, []).append(position)
    return result
