# Algorithms and use cases

All offsets are Python string indices (Unicode code points), and exact matchers include overlapping matches. An empty exact pattern matches at every boundary, including the end. Multi-pattern and streaming search require nonempty patterns.

## Exact matching

- **Naive** checks each possible start. It is a clear oracle for tests and useful on tiny inputs.
- **KMP** reuses the prefix function after a mismatch. Use it for guaranteed linear-time single-pattern search.
- **Z search** computes prefix lengths over `pattern + sentinel + text`; the sentinel is a unique object, so user characters cannot collide with it.
- **Rabin–Karp** uses two rolling hashes to reject most windows quickly and verifies each candidate with an exact string comparison. It is useful when hashing is itself part of the lesson.
- **Horspool** compares windows right to left and skips ahead using a bad-character table. It tends to perform well on ordinary text, while retaining overlapping matches.

## Indexing and multiple patterns

- **Aho–Corasick** builds a trie, failure links, and inherited outputs. One pass finds all occurrences of many patterns, including patterns that are suffixes of other matches.
- **Suffix array** sorts suffix positions with rank doubling. `SuffixIndex` binary-searches matching prefixes for repeated queries against one text.
- **Kasai LCP** computes common-prefix lengths of neighboring suffixes and supports the longest-repeated-substring query.

## Sequence analysis

- **Manacher** finds the longest palindromic substring in linear time; ties choose the earliest occurrence.
- **Levenshtein distance** counts insertions, deletions, and substitutions with two DP rows.
- **LCS** reconstructs one longest common subsequence; **common substring** requires consecutive characters and uses two DP rows.
- **Booth** finds the lexicographically least rotation.
- **Glob** matches an entire string with `?` for one character and `*` for any sequence.

`KMPStream` and `AhoStream` preserve automaton state between chunks and report offsets in the whole stream.
