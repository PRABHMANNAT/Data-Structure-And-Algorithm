"""Loopback-only web UI and JSON API for comparing local documents."""

import argparse
import base64
import binascii
import json
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .engine import Detector, DetectorConfig
from .ingest import document_from_bytes

MAX_REQUEST_BYTES = 32_000_000
MAX_FILE_BYTES = 8_000_000
MAX_FILES = 50


def analyze(payload: object) -> dict:
    """Validate browser input and return a serializable comparison report."""
    if not isinstance(payload, dict):
        raise ValueError("Expected a JSON object")
    entries = payload.get("files")
    if not isinstance(entries, list) or not 2 <= len(entries) <= MAX_FILES:
        raise ValueError("Choose between 2 and 50 files")
    threshold = payload.get("threshold", 0.35)
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)):
        raise ValueError("Threshold must be a number from 0 to 1")
    config = DetectorConfig(min_score=float(threshold))
    documents = []
    names = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("Each file needs a name and text content")
        name = entry.get("name")
        content = entry.get("content")
        encoded = entry.get("content_base64")
        if not isinstance(name, str) or (isinstance(content, str) == isinstance(encoded, str)):
            raise ValueError("Each file needs a name and one content field")
        name = name.replace("\\", "/").split("/")[-1]
        if not name or len(name) > 120 or name in names:
            raise ValueError("File names must be unique and at most 120 characters")
        if isinstance(encoded, str):
            if len(encoded) > (MAX_FILE_BYTES * 4 // 3 + 8):
                raise ValueError(f"{name} exceeds the 8 MB file limit")
            try:
                data = base64.b64decode(encoded, validate=True)
            except binascii.Error as exc:
                raise ValueError(f"Invalid encoded content for {name}") from exc
        else:
            data = content.encode("utf-8")
        if len(data) > MAX_FILE_BYTES:
            raise ValueError(f"{name} exceeds the 8 MB file limit")
        names.add(name)
        documents.append(document_from_bytes(name, data))
    matches = Detector(config).compare(documents)
    return {"files": len(documents), "matches": [asdict(match) for match in matches]}


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status: int, payload: dict) -> None:
        self._send(status, json.dumps(payload).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self) -> None:
        if self.path == "/":
            content = Path(__file__).with_name("web_ui.html").read_bytes()
            self._send(200, content, "text/html; charset=utf-8")
        elif self.path == "/api/health":
            self._json(200, {"status": "ok"})
        else:
            self._json(404, {"error": "Not found"})

    def do_POST(self) -> None:
        if self.path != "/api/compare":
            self._json(404, {"error": "Not found"})
            return
        if self.headers.get_content_type() != "application/json":
            self._json(415, {"error": "Use application/json"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_REQUEST_BYTES:
                raise ValueError("Request must be between 1 byte and 32 MB")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            result = analyze(payload)
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            self._json(400, {"error": str(exc)})
            return
        self._json(200, result)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Serve the local plagiarism detector web UI")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Plagiarism detector running at http://127.0.0.1:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
