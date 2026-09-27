# Security

GraphForge has no network I/O. Callers parsing untrusted edge feeds should impose
node, edge, and JSON line limits before constructing graph objects to avoid resource
exhaustion. Do not expose arbitrary historical revisions without retention controls.
