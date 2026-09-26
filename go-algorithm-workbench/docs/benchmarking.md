# Benchmarking

Use Go's built-in benchmark harness to compare implementations:

```bash
go test -bench=. -benchmem ./...
```

Benchmark with representative input distributions; already sorted data can
hide the behavior of partition-based sorting algorithms.
