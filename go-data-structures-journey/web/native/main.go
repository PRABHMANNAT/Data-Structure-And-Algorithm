package main

import (
	"encoding/json"
	s "github.com/your-account/go-data-structures-journey/algorithms"
	"os"
)

func main() {
	var input struct {
		Values []int `json:"values"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		panic(err)
	}
	out := s.MergeSort(input.Values)
	json.NewEncoder(os.Stdout).Encode(out)
}
