from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from .engine import StreamEngine
from .model import Event


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Process JSONL StreamShield events")
    parser.add_argument("--window-ms", type=int, default=60_000)
    parser.add_argument("--lateness-ms", type=int, default=5_000)
    args = parser.parse_args(argv); engine = StreamEngine(args.window_ms, args.lateness_ms)
    for line in sys.stdin:
        raw = json.loads(line); engine.ingest(Event(**raw))
    print(json.dumps({"stats": asdict(engine.stats()), "leaders": engine.leaders()}))
    return 0


if __name__ == "__main__": raise SystemExit(main())
