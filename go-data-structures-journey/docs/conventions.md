# API conventions

Operations that may not produce a value return `(value, ok)`. Empty collections therefore do not need to panic or reserve a sentinel value. Generic type parameters keep the structures reusable while preserving compile-time safety.
