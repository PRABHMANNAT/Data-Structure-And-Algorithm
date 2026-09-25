package structures

// Trie indexes strings by runes.
type Trie struct{ root *trieNode }
type trieNode struct{ children map[rune]*trieNode; word bool }
func NewTrie()*Trie{return &Trie{root:&trieNode{children:map[rune]*trieNode{}}}}
func(t *Trie) Insert(s string){n:=t.root;for _,r:=range s{if n.children[r]==nil{n.children[r]=&trieNode{children:map[rune]*trieNode{}}};n=n.children[r]};n.word=true}
func(t *Trie) Contains(s string)bool{n:=t.root;for _,r:=range s{n=n.children[r];if n==nil{return false}};return n.word}
func(t *Trie) HasPrefix(s string)bool{n:=t.root;for _,r:=range s{n=n.children[r];if n==nil{return false}};return true}
