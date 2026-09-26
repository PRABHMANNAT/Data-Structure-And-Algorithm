package main

import (
	"flag"
	"fmt"
	"github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go-algorithm-workbench/algorithms"
	"os"
)

func main() {
	demo := flag.String("demo", "dijkstra", "demo: dijkstra, sort, kmp")
	flag.Parse()
	switch *demo {
	case "dijkstra":
		g := algorithms.Graph{}
		g.AddEdge(1, 2, 4)
		g.AddEdge(1, 3, 1)
		g.AddEdge(3, 2, 2)
		fmt.Println(g.Dijkstra(1))
	case "sort":
		values := []int{7, 2, 9, 1, 2}
		algorithms.QuickSort(values)
		fmt.Println(values)
	case "kmp":
		fmt.Println(algorithms.KMP("abracadabra", "abra"))
	default:
		fmt.Fprintln(os.Stderr, "unknown demo")
		os.Exit(2)
	}
}
