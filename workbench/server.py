"""Loopback-only development server: python -m workbench.server."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import time
from urllib.parse import unquote, urlsplit
from .registry import ROOT, projects, run


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' blob: data:; connect-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'self'")
        super().end_headers()

    def respond(self, status, value):
        encoded = json.dumps(value, ensure_ascii=False, allow_nan=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        route = unquote(urlsplit(self.path).path)
        if route == "/api/projects":
            self.respond(200, list(projects().values()))
            return
        # Never serve Git internals, hidden files, caches, or arbitrary directories.
        resolved = (ROOT / route.lstrip("/")).resolve()
        if not resolved.is_relative_to(ROOT) or any(part.startswith(".") for part in Path(route).parts):
            self.send_error(404)
            return
        if route == "/":
            self.path = "/workbench/index.html"
        elif resolved.is_dir():
            if not (resolved / "index.html").is_file():
                self.send_error(404)
                return
        super().do_GET()

    def do_POST(self):
        route = urlsplit(self.path).path
        if not route.startswith("/api/run/"):
            self.respond(404, {"error": "Unknown endpoint"})
            return
        # Disallow cross-origin browser requests and DNS-rebinding hostnames.
        host = self.headers.get("Host", "")
        allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        origin = self.headers.get("Origin")
        if host not in allowed or (origin and origin not in {"http://" + h for h in allowed}):
            self.respond(403, {"error": "Use the local workbench origin"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 65536:
                self.respond(413, {"error": "Input must be between 1 byte and 64 KiB"})
                return
            data = json.loads(self.rfile.read(length))
            started = time.perf_counter()
            result = run(route.removeprefix("/api/run/"), data)
            self.respond(200, {"result": result, "elapsed_ms": round((time.perf_counter() - started) * 1000, 2)})
        except KeyError as error:
            self.respond(404, {"error": str(error)})
        except (ValueError, TypeError) as error:
            self.respond(400, {"error": str(error)})
        except (RuntimeError, TimeoutError) as error:
            self.respond(503, {"error": str(error)})
        except Exception as error:
            self.respond(500, {"error": f"{type(error).__name__}: {error}"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Workbench: http://127.0.0.1:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
