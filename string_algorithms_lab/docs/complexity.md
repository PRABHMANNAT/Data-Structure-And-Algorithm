# Complexity guide

Let `n` be text length, `m` pattern length, `P` the sum of all pattern lengths, `z` the number of matches, and `a`, `b` the lengths of two compared strings. Space excludes returned results unless noted.

| Operation | Time | Extra space |
| --- | --- | --- |
| Naive exact search | O(nm) | O(1) |
| KMP prefix and search | O(n + m) | O(m) |
| Z search | O(n + m) | O(n + m) |
| Rabin–Karp | O(n + m) expected; O(nm) with many verified collisions | O(n + m) |
| Horspool | O(nm) worst case | O(min(m, alphabet)) |
| Aho–Corasick build and search | O(P + n + z) under constant-time dictionary operations | O(P + z) |
| Suffix array rank doubling | O(n log² n) | O(n) |
| Kasai LCP | O(n) after suffix array | O(n) |
| Suffix index query | O(m log n + z log z) including sorted positions | O(z) |
| Manacher palindrome | O(n) | O(n) |
| Levenshtein distance | O(ab) | O(min(a, b)) |
| LCS reconstruction | O(ab) | O(ab) |
| Longest common substring | O(ab) | O(b) |
| Booth minimal rotation | O(n) | O(n) for doubled text |
| Glob matching | O(nm) worst case with retries | O(1) |

Python substring comparisons and dictionary operations have their own costs. The suffix query bound accounts for comparing up to `m` characters at each binary-search step. Rolling hashes never determine a match alone: candidate windows are verified to avoid false positives.
