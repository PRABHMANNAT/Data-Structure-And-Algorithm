from dataclasses import dataclass


@dataclass(frozen=True)
class Edit:
    kind: str
    text: str
