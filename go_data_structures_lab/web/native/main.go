package main

import (
	"encoding/json"
	s "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_data_structures_lab/structures"
	"os"
)

func main() {
	var input struct {
		Values []int `json:"values"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		panic(err)
	}
	heap := s.NewMinHeap[int](func(a, b int) bool { return a < b })
	for _, v := range input.Values {
		heap.Push(v)
	}
	out := []int{}
	for heap.Len() > 0 {
		v, err := heap.Pop()
		if err != nil {
			panic(err)
		}
		out = append(out, v)
	}
	json.NewEncoder(os.Stdout).Encode(out)
}
