"""Compile fixed, repository-owned bridges. User input is stdin, never shell code."""
from pathlib import Path
import hashlib
import os
import shutil
import subprocess
import threading

ROOT = Path(__file__).resolve().parents[1]
LOCK = threading.Lock()


def checked_process(command, **kwargs):
    try:
        return subprocess.run(command, **kwargs)
    except subprocess.TimeoutExpired:
        raise RuntimeError("The native process timed out. Try a smaller input.") from None
    except OSError as error:
        if getattr(error, "winerror", None) == 4551:
            raise RuntimeError("Windows Application Control blocked this compiled program. The project can run on a machine whose application policy permits local development builds.") from None
        raise RuntimeError(f"Could not start the native program: {error}") from None


def compiler():
    configured = os.environ.get("CXX")
    candidates = [configured, shutil.which("g++"), shutil.which("clang++"),
                  str(ROOT.parent / ".tools/w64devkit/bin/g++.exe")]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError("C++ compiler unavailable. Install g++ or set CXX to its full path, then restart the server.")


def execute(project, payload, sources=None):
    folder = ROOT / project
    go = (folder / "go.mod").exists()
    source_paths = list(folder.rglob("*.go" if go else "*.hpp"))
    source_paths += list(folder.rglob("*.h")) + list(folder.rglob("*.cpp"))
    if go:
        source_paths += [folder / "go.mod"]
    digest = hashlib.sha256(b"".join(path.read_bytes() for path in sorted(source_paths))).hexdigest()[:16]
    cache = ROOT / ".workbench-cache"
    cache.mkdir(exist_ok=True)
    binary = cache / (folder.name.replace(" ", "-") + "-" + digest + (".exe" if os.name == "nt" else ""))
    with LOCK:
        if not binary.exists():
            if go:
                executable = shutil.which("go")
                if not executable:
                    raise RuntimeError("Go unavailable. Install Go 1.27+ and restart the server.")
                command = [executable, "build", "-o", str(binary), "./web/native"]
            else:
                command = [compiler(), "-std=c++20", "-O2", "-Iinclude", "-Isrc", "web/native.cpp"] + (sources or []) + ["-o", str(binary)]
            result = checked_process(command, cwd=folder, capture_output=True, text=True, timeout=90)
            if result.returncode:
                raise RuntimeError("Native build failed: " + result.stderr[-2500:])
    result = checked_process([str(binary)], input=payload, cwd=folder, capture_output=True, text=True, timeout=8)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Native program rejected this input")
    return result.stdout.strip()
