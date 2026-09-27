# Security posture

Input JSON is parsed only from the caller's stream and snapshots are checksum
verified. Deployments should cap line length, event-key length, and snapshot path
permissions at their boundary; this library deliberately owns no network surface.
