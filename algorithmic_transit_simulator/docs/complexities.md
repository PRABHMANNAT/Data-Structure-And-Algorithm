# Complexity guide

| Component | Primary operation | Cost |
| --- | --- | --- |
| MinHeap | push/pop | O(log n) |
| EarliestArrivalRouter | route search | O((V + E) log V) |
| PrefixTrie | prefix lookup | O(prefix + results) |
| DisjointSet | union/find amortized | O(alpha(n)) |
| AVLTree | insertion/range boundary | O(log n) |
| LRUCache | get/put | O(1) |

The interval collection uses a sorted list intentionally; it is appropriate for the modest number of arrivals assigned to a single platform.
