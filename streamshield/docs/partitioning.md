# Partitioning

Hash by event key before sending records to engines. Maintain independent
watermarks per partition and report their minimum for a globally conservative
frontier. Do not merge windows that have different lateness policies.
