package main
import("fmt"; ds "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_data_structures_lab/structures")
func main(){g:=ds.NewGraph();g.AddEdge("start","finish");fmt.Println("BFS:",g.BFS("start"))}
