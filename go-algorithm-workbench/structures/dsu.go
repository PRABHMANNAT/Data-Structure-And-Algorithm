package structures

// DisjointSet supports connectivity queries using path compression and union by size.
type DisjointSet struct {
	parent, size []int
	groups       int
}

// NewDisjointSet creates n singleton groups.
func NewDisjointSet(n int) *DisjointSet {
	p := make([]int, n)
	s := make([]int, n)
	for i := range p {
		p[i] = i
		s[i] = 1
	}
	return &DisjointSet{parent: p, size: s, groups: n}
}

// Find returns a value's group representative in near-constant amortized time.
func (d *DisjointSet) Find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.Find(d.parent[x])
	}
	return d.parent[x]
}

// Union combines groups and reports whether they were different.
func (d *DisjointSet) Union(a, b int) bool {
	a = d.Find(a)
	b = d.Find(b)
	if a == b {
		return false
	}
	if d.size[a] < d.size[b] {
		a, b = b, a
	}
	d.parent[b] = a
	d.size[a] += d.size[b]
	d.groups--
	return true
}

// Connected reports whether two values share a group.
func (d *DisjointSet) Connected(a, b int) bool { return d.Find(a) == d.Find(b) }

// Groups returns the current number of components.
func (d *DisjointSet) Groups() int { return d.groups }
