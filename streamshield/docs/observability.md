# Observability

`EngineStats` exposes accepted and late counts plus the current watermark. Export
these as counters/gauges from the host service. Alert on sustained late-event rates
because they indicate source clock skew, delayed delivery, or a lateness budget set too low.
