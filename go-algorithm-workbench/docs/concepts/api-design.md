# API design

The workbench returns `(value, ok)` for absence rather than relying on a zero
value. Constructors validate non-negotiable invariants such as cache capacity.
