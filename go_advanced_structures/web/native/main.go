package main

import (
	"encoding/json"
	a "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_advanced_structures/advanced"
	"os"
)

func main() {
	var input struct {
		Values      []int
		Left, Right int
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		panic(err)
	}
	f := a.NewFenwick(len(input.Values))
	for i, v := range input.Values {
		f.Add(i, v)
	}
	s := a.NewSegmentTree(input.Values)
	x, err := f.Range(input.Left, input.Right)
	if err != nil {
		panic(err)
	}
	y, err := s.Sum(input.Left, input.Right)
	if err != nil {
		panic(err)
	}
	prefix := []int{}
	for i := range input.Values {
		prefix = append(prefix, f.Prefix(i))
	}
	json.NewEncoder(os.Stdout).Encode(map[string]any{"fenwick": x, "segment": y, "prefix": prefix})
}
