package main

import (
	"encoding/json"
	s "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_search_structures/search"
	"os"
)

func main() {
	var input struct {
		Words  []string
		Prefix string
		Limit  int
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		panic(err)
	}
	trie := s.NewTrie()
	for _, word := range input.Words {
		trie.Insert(word)
	}
	json.NewEncoder(os.Stdout).Encode(trie.Complete(input.Prefix, input.Limit))
}
