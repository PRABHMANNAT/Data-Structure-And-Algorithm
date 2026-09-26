package algorithms

import (
	"reflect"
	"testing"
)

func TestSortAndSearch(t *testing.T) {
	input := []int{4, 1, 3, 1, 2}
	if got := MergeSort(input); !reflect.DeepEqual(got, []int{1, 1, 2, 3, 4}) {
		t.Fatal(got)
	}
	QuickSort(input)
	if BinarySearch(input, 3) != 3 || LowerBound(input, 1) != 0 {
		t.Fatal("search failed")
	}
}
func TestTraversalAndTopologicalSort(t *testing.T) {
	g := Graph{}
	g.AddEdge(1, 2, 1)
	g.AddEdge(1, 3, 1)
	g.AddEdge(2, 4, 1)
	if got := g.BFS(1); !reflect.DeepEqual(got, []int{1, 2, 3, 4}) {
		t.Fatal(got)
	}
	if _, ok := g.TopologicalSort(); !ok {
		t.Fatal("DAG rejected")
	}
}
func TestDijkstra(t *testing.T) {
	g := Graph{}
	g.AddEdge(1, 2, 4)
	g.AddEdge(1, 3, 1)
	g.AddEdge(3, 2, 2)
	if got := g.Dijkstra(1)[2]; got != 3 {
		t.Fatalf("distance %d", got)
	}
}
func TestSCC(t *testing.T) {
	g := Graph{}
	g.AddEdge(1, 2, 1)
	g.AddEdge(2, 1, 1)
	g.AddEdge(2, 3, 1)
	g.AddEdge(3, 4, 1)
	g.AddEdge(4, 3, 1)
	if len(g.StronglyConnectedComponents()) != 2 {
		t.Fatal("wrong component count")
	}
}
func TestDynamicProgramming(t *testing.T) {
	if Knapsack01([]int{1, 3, 4}, []int{15, 20, 30}, 4) != 35 {
		t.Fatal("knapsack")
	}
	if LongestIncreasingSubsequence([]int{10, 9, 2, 5, 3, 7, 101, 18}) != 4 {
		t.Fatal("lis")
	}
	if LongestCommonSubsequence("abcde", "ace") != 3 {
		t.Fatal("lcs")
	}
}
func TestKMP(t *testing.T) {
	if got := KMP("abababa", "aba"); !reflect.DeepEqual(got, []int{0, 2, 4}) {
		t.Fatal(got)
	}
}
