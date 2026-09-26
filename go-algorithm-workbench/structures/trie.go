package structures

// Trie stores UTF-8 strings as runes. Insert and lookup take O(L).
type Trie struct{ root *trieNode }
type trieNode struct {
	children map[rune]*trieNode
	terminal bool
}

// NewTrie creates an empty trie.
func NewTrie() *Trie { return &Trie{root: &trieNode{children: make(map[rune]*trieNode)}} }

// Insert records word.
func (t *Trie) Insert(word string) {
	n := t.root
	for _, r := range word {
		if n.children[r] == nil {
			n.children[r] = &trieNode{children: make(map[rune]*trieNode)}
		}
		n = n.children[r]
	}
	n.terminal = true
}

// Contains reports whether word was inserted.
func (t *Trie) Contains(word string) bool { n := t.walk(word); return n != nil && n.terminal }

// HasPrefix reports whether any word starts with prefix.
func (t *Trie) HasPrefix(prefix string) bool { return t.walk(prefix) != nil }
func (t *Trie) walk(s string) *trieNode {
	n := t.root
	for _, r := range s {
		n = n.children[r]
		if n == nil {
			return nil
		}
	}
	return n
}
