# Versioning model

Commits append a new graph revision. Reads copy that immutable state so callers can
run long algorithms without lock coupling to future edits. Retention is deliberately
unbounded in this learning implementation; a service should compact old revisions.
