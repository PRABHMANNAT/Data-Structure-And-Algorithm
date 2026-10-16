# Reviewing a flagged pair

Start with the two original source files and the report's line numbers. Confirm
that the matching spans contain distinctive decisions rather than assignment
scaffolding, standard library idioms, or a common textbook algorithm. Compare
the full context around each span and note any matching errors, unusual choices,
or shared comments that the normalized score alone cannot explain.

Check whether the assignment supplied starter code or allowed pair work. If a
large cohort shares the same template, run the detector on the whole cohort so
very common fingerprints can be filtered. Small cohorts receive no automatic
common-code suppression, because three identical submissions may itself be a
signal worth inspecting.

Record the manual evidence and give the authors a chance to explain their work
through the process required by the course. A threshold crossing alone should
never be the final decision.
