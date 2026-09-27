# Architecture

The engine is partition-local: it never pretends that separate partitions have a
global ordering. A `Watermark` defines the admissible event-time frontier; the
window then expires old events, while frequency structures accumulate candidates.
