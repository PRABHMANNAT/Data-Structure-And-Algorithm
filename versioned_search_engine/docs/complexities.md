# Complexity notes

Posting lookup is O(1) average by term; Boolean operations are linear in their materialized sets. Trie completion is proportional to prefix traversal plus reported matches. BM25 scoring visits the query terms for each candidate. The LRU cache provides O(1) get/put operations.
