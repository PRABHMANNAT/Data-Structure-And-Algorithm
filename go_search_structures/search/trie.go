package search

import "sort"

type trieNode struct {
	children map[rune]*trieNode
	terminal bool
}
type Trie struct{ root *trieNode }

func NewTrie() *Trie { return &Trie{root: &trieNode{children: map[rune]*trieNode{}}} }
func (t *Trie) Insert(word string) {
	n := t.root
	for _, r := range word {
		if n.children[r] == nil {
			n.children[r] = &trieNode{children: map[rune]*trieNode{}}
		}
		n = n.children[r]
	}
	n.terminal = true
}

// Complete visits sorted branches before limiting, so top-k is deterministic.
func (t *Trie) Complete(prefix string, limit int) []string {
	if limit <= 0 {
		return []string{}
	}
	n := t.root
	for _, r := range prefix {
		n = n.children[r]
		if n == nil {
			return []string{}
		}
	}
	out := []string{}
	var walk func(*trieNode, string)
	walk = func(node *trieNode, word string) {
		if len(out) >= limit {
			return
		}
		if node.terminal {
			out = append(out, word)
		}
		keys := make([]rune, 0, len(node.children))
		for r := range node.children {
			keys = append(keys, r)
		}
		sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
		for _, r := range keys {
			walk(node.children[r], word+string(r))
		}
	}
	walk(n, prefix)
	return out
}
