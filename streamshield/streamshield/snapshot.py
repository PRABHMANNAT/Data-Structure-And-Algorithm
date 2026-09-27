from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path
from .engine import StreamEngine


def save_stats(engine: StreamEngine, path: str | Path) -> None:
    payload = json.dumps(asdict(engine.stats()), sort_keys=True).encode()
    envelope = {"checksum": hashlib.sha256(payload).hexdigest(), "payload": payload.decode()}
    Path(path).write_text(json.dumps(envelope, sort_keys=True), encoding="utf-8")


def load_stats(path: str | Path) -> dict[str, int]:
    envelope = json.loads(Path(path).read_text(encoding="utf-8")); payload = envelope["payload"].encode()
    if hashlib.sha256(payload).hexdigest() != envelope["checksum"]: raise ValueError("snapshot checksum mismatch")
    return json.loads(payload)
