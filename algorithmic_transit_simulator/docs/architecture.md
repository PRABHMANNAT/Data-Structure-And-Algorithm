# Architecture

`TransitGraph` owns the timetable adjacency lists. `EarliestArrivalRouter` runs a time-dependent Dijkstra traversal over those lists with `MinHeap`. `TransitService` combines graph mutation, prefix lookup, and cached planning.

Operations are separated from route search: `DisruptionBoard` derives an operational graph, `PlatformScheduler` guards platform dwell intervals, and `Simulator` drains timestamped events while collecting metrics.

This separation makes routing deterministic and leaves side-effectful operations easy to test.
