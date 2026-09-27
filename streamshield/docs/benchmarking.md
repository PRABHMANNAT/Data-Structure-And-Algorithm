# Benchmarking

Benchmark ingestion separately from serialisation. Use an event distribution with
both a hot-key tail and realistic disorder; uniform keys hide candidate-management
costs, while perfectly ordered timestamps hide watermark behaviour.
