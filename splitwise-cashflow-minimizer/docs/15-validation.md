# Validation

The library rejects empty payers, empty groups, empty participant names, duplicate participants, and negative amounts. Uneven cent splits are valid and preserve the full payment. The browser additionally requires positive amounts, limits input size, and accepts simple names that are safe to export in CSV.
