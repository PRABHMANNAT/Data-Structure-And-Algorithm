"""JSON CLI: python -m quantilewatch --example 0, or --input payload.json."""

import argparse, json, sys
from pathlib import Path
from .service import run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--example", type=int, default=0)
    args = parser.parse_args()
    try:
        presets = json.loads(
            (Path(__file__).parent / "web/project.json").read_text(encoding="utf-8")
        )["presets"]
        if not 0 <= args.example < len(presets):
            raise ValueError("Example index out of range")
        payload = (
            json.loads(args.input.read_text(encoding="utf-8"))
            if args.input
            else presets[args.example]["input"]
        )
        if not isinstance(payload, dict):
            raise ValueError("Input must be a JSON object")
        print(json.dumps(run(payload), ensure_ascii=False, allow_nan=False, indent=2))
        return 0
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
