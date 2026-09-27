# API contract

`RouteEngine.route` returns `None` for an unreachable target and a `Route` for a
reachable one. Revisions are zero-based and invalid revision requests raise
`InvalidRevision`; callers should treat a revision as an immutable read token.
