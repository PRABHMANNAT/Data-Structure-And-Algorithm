package algorithms

import "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go-algorithm-workbench/structures"

type distanceNode struct{ vertex, distance int }

// Dijkstra computes shortest distances from source for graphs with non-negative weights.
func (g Graph) Dijkstra(source int) map[int]int {
	const inf = int(^uint(0) >> 1)
	dist := map[int]int{}
	for v := range g {
		dist[v] = inf
	}
	dist[source] = 0
	heap := structures.NewMinHeap(func(a, b distanceNode) bool { return a.distance < b.distance })
	heap.Push(distanceNode{source, 0})
	for heap.Len() > 0 {
		current, _ := heap.Pop()
		if current.distance != dist[current.vertex] {
			continue
		}
		for _, e := range g[current.vertex] {
			next := current.distance + e.Weight
			if next < dist[e.To] {
				dist[e.To] = next
				heap.Push(distanceNode{e.To, next})
			}
		}
	}
	return dist
}

// ShortestPath rebuilds a path using a predecessor map. It returns nil when unreachable.
func ShortestPath(previous map[int]int, source, target int) []int {
	path := []int{}
	for current := target; ; {
		path = append(path, current)
		if current == source {
			break
		}
		next, ok := previous[current]
		if !ok {
			return nil
		}
		current = next
	}
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}
