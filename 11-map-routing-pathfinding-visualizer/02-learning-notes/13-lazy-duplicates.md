# Lazy duplicate entries

Improved routes add a new queue entry instead of decreasing a key in place. A closed-set check safely ignores an older duplicate when it is popped.
