# API contract

`StreamEngine.ingest` either accepts exactly one valid event or raises `LateEvent`.
`leaders` returns only verified candidate keys; frequency values remain Count-Min
Sketch estimates and must be interpreted as upper bounds.
