package main

import (
	"encoding/json"
	s "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go-algorithm-workbench/algorithms"
	"os"
)

func main() {
	var input struct {
		Values []int `json:"values"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		panic(err)
	}
	out := append([]int{}, input.Values...)
	s.QuickSort(out)
	json.NewEncoder(os.Stdout).Encode(out)
}
