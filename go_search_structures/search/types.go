package search

// Document is the input unit stored by the in-memory index.
type Document struct{ ID,Text string }
type Result struct{ ID string; Score int }
