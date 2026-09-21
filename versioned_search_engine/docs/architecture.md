# Architecture

The `DocumentStore` owns revisioned documents. `InvertedIndex` maps normalized terms to positional posting lists, while `TermTrie` provides completion. The composed `SearchEngine` invalidates its LRU response cache whenever indexing changes.

Separate query, ranking, snapshot, and graph components keep their data structure invariants independently testable.
