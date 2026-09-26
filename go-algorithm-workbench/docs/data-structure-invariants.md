# Data-structure invariants

- A stack exposes only the final slice element.
- A queue's active interval begins at its head index.
- Heap parents are never greater than their children under `less`.
- AVL child heights differ by at most one.
- Every trie node owns its outgoing rune map.
- LRU list front is the most recently accessed entry.
