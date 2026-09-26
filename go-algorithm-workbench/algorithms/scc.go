package algorithms

// StronglyConnectedComponents returns graph components via Kosaraju's algorithm.
func (g Graph) StronglyConnectedComponents() [][]int {
	seen := map[int]bool{}
	order := []int{}
	var finish func(int)
	finish = func(v int) {
		seen[v] = true
		for _, e := range g[v] {
			if !seen[e.To] {
				finish(e.To)
			}
		}
		order = append(order, v)
	}
	for v := range g {
		if !seen[v] {
			finish(v)
		}
	}
	reversed := Graph{}
	for v := range g {
		if _, ok := reversed[v]; !ok {
			reversed[v] = nil
		}
		for _, e := range g[v] {
			reversed.AddEdge(e.To, v, e.Weight)
		}
	}
	seen = map[int]bool{}
	components := [][]int{}
	var collect func(int, *[]int)
	collect = func(v int, c *[]int) {
		seen[v] = true
		*c = append(*c, v)
		for _, e := range reversed[v] {
			if !seen[e.To] {
				collect(e.To, c)
			}
		}
	}
	for i := len(order) - 1; i >= 0; i-- {
		v := order[i]
		if !seen[v] {
			c := []int{}
			collect(v, &c)
			components = append(components, c)
		}
	}
	return components
}
