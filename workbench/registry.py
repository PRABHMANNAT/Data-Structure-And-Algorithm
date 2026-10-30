"""Discover explicit project manifests; import only those checked-in adapters."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def projects():
    manifests = sorted(ROOT.glob("*/web/project.json")) + sorted(ROOT.glob("Number System/*/web/project.json"))
    result = {}
    for path in manifests:
        record = json.loads(path.read_text(encoding="utf-8"))
        for name in ('lesson', 'guide'):
            metadata=path.parent/(name+'.json')
            if metadata.is_file():record[name]=json.loads(metadata.read_text(encoding='utf-8'))
        record["folder"] = path.parent.parent.relative_to(ROOT).as_posix()
        result[record["id"]] = record
    return result


@lru_cache(maxsize=32)
def adapter(project_id):
    record = projects().get(project_id)
    if record is None:
        raise KeyError("Unknown project")
    folder = ROOT / record["folder"]
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    spec = importlib.util.spec_from_file_location("workbench_adapter_" + project_id.replace("-", "_"), folder / "web/adapter.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(project_id, payload):
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object")
    return adapter(project_id).run(payload)
