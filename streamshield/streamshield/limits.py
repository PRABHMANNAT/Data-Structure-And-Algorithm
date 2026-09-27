from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ResourceLimits:
    max_key_length: int = 256
    max_labels: int = 32

    def validate_key(self, key: str) -> None:
        if len(key) > self.max_key_length: raise ValueError("event key exceeds configured limit")
