# Design decisions

The store uses explicit revisions instead of hidden mutation. This makes cache
correctness mechanical: cache keys include the revision. Core algorithms avoid third
party dependencies to keep their asymptotic behaviour easy to inspect and teach.
