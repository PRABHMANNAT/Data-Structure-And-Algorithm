package advanced

import "math/rand"
type treapNode struct{ key,priority int; left,right *treapNode }
type Treap struct{ root *treapNode }
func treapRotateRight(n *treapNode)*treapNode{x:=n.left;n.left=x.right;x.right=n;return x}
func treapRotateLeft(n *treapNode)*treapNode{x:=n.right;n.right=x.left;x.left=n;return x}
func treapInsert(n *treapNode,k int)*treapNode{if n==nil{return &treapNode{key:k,priority:rand.Int()}};if k<n.key{n.left=treapInsert(n.left,k);if n.left.priority<n.priority{n=treapRotateRight(n)}}else if k>n.key{n.right=treapInsert(n.right,k);if n.right.priority<n.priority{n=treapRotateLeft(n)}};return n}
func (t *Treap) Insert(k int){t.root=treapInsert(t.root,k)}
func (t *Treap) Contains(k int)bool{for n:=t.root;n!=nil;{if n.key==k{return true};if k<n.key{n=n.left}else{n=n.right}};return false}
