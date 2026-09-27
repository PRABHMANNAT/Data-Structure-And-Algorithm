# Transactions

The `edit` context stages additions and creates one revision only if the context
exits normally. For multi-writer services, serialize commits or use compare-and-swap
revision numbers in a storage adapter.
