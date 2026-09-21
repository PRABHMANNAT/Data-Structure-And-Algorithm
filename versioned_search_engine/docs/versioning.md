# Versioning and cache policy

The document store increments its revision on each add, replacement, or removal. Search response cache keys include this revision and the composed engine clears cached responses after an indexing mutation. Snapshot storage deep-copies captured state to support reliable restoration.
