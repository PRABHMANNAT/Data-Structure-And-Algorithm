# Recovery

The starter snapshot records observable counters and protects them with SHA-256.
Production deployments should atomically write a full source-of-truth event log,
then rebuild probabilistic structures from that log after a process restart.
