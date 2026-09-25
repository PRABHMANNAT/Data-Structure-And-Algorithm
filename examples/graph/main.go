package main

import (
	"fmt"
	"github.com/your-account/go-data-structures-journey/structures"
)

func main() { g := structures.NewGraph[string](); g.AddEdge("start", "finish"); fmt.Println(g.BreadthFirst("start")) }
