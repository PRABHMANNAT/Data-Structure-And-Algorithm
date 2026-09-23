package search

import "sort"
type trieNode struct{ children map[rune]*trieNode; terminal bool }
type Trie struct{ root *trieNode }
func NewTrie()*Trie{return &Trie{root:&trieNode{children:map[rune]*trieNode{}}}}
func (t *Trie) Insert(word string){n:=t.root;for _,r:=range word{if n.children[r]==nil{n.children[r]=&trieNode{children:map[rune]*trieNode{}}};n=n.children[r]};n.terminal=true}
func (t *Trie) Complete(prefix string,limit int)[]string{n:=t.root;for _,r:=range prefix{n=n.children[r];if n==nil{return nil}};out:=[]string{};var walk func(*trieNode,string);walk=func(x *trieNode,s string){if len(out)>=limit{return};if x.terminal{out=append(out,s)};for r,c:=range x.children{walk(c,s+string(r))}};walk(n,prefix);sort.Strings(out);if len(out)>limit{return out[:limit]};return out}
