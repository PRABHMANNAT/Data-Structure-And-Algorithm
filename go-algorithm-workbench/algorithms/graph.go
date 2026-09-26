package algorithms

import "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go-algorithm-workbench/structures"

// Edge represents a weighted directed edge.
type Edge struct{ To, Weight int }

// Graph stores a directed adjacency list. Missing vertices have no outgoing edges.
type Graph map[int][]Edge

// AddEdge appends a directed weighted edge.
func (g Graph) AddEdge(from, to, weight int) {
	g[from] = append(g[from], Edge{to, weight})
	if _, ok := g[to]; !ok {
		g[to] = nil
	}
}

// BFS visits vertices in breadth-first order from start.
func (g Graph) BFS(start int) []int {
	seen := map[int]bool{start: true}
	q := structures.Queue[int]{}
	q.Enqueue(start)
	out := []int{}
	for q.Len() > 0 {
		v, _ := q.Dequeue()
		out = append(out, v)
		for _, e := range g[v] {
			if !seen[e.To] {
				seen[e.To] = true
				q.Enqueue(e.To)
			}
		}
	}
	return out
}

// DFS visits vertices in depth-first pre-order from start.
func (g Graph) DFS(start int) []int {
	seen := map[int]bool{}
	out := []int{}
	var visit func(int)
	visit = func(v int) {
		seen[v] = true
		out = append(out, v)
		for _, e := range g[v] {
			if !seen[e.To] {
				visit(e.To)
			}
		}
	}
	visit(start)
	return out
}

// TopologicalSort returns a valid ordering for a DAG and false for a cycle.
func (g Graph) TopologicalSort() ([]int, bool) {
	in := map[int]int{}
	for v, edges := range g {
		if _, ok := in[v]; !ok {
			in[v] = 0
		}
		for _, e := range edges {
			in[e.To]++
		}
	}
	q := structures.Queue[int]{}
	for v, d := range in {
		if d == 0 {
			q.Enqueue(v)
		}
	}
	out := make([]int, 0, len(in))
	for q.Len() > 0 {
		v, _ := q.Dequeue()
		out = append(out, v)
		for _, e := range g[v] {
			in[e.To]--
			if in[e.To] == 0 {
				q.Enqueue(e.To)
			}
		}
	}
	return out, len(out) == len(in)
}
