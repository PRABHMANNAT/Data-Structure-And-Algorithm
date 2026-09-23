package structures

import "sort"
type trieNode struct { children map[rune]*trieNode; word bool }
type Trie struct { root *trieNode }
func NewTrie()*Trie{return &Trie{root:&trieNode{children:map[rune]*trieNode{}}}}
func (t *Trie) Insert(word string){n:=t.root;for _,r:=range word{if n.children[r]==nil{n.children[r]=&trieNode{children:map[rune]*trieNode{}}};n=n.children[r]};n.word=true}
func (t *Trie) Contains(word string)bool{n:=t.root;for _,r:=range word{n=n.children[r];if n==nil{return false}};return n.word}
func (t *Trie) Prefixes(prefix string)[]string{n:=t.root;for _,r:=range prefix{n=n.children[r];if n==nil{return nil}};out:=[]string{};var walk func(*trieNode,string);walk=func(x *trieNode,s string){if x.word{out=append(out,s)};for r,c:=range x.children{walk(c,s+string(r))}};walk(n,prefix);sort.Strings(out);return out}
