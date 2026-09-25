package structures

import "cmp"

// BinarySearchTree indexes ordered values.
type BinarySearchTree[T cmp.Ordered] struct{ root *bstNode[T] }
type bstNode[T cmp.Ordered] struct{ value T; left,right *bstNode[T] }
func(t *BinarySearchTree[T]) Insert(v T){if t.root==nil{t.root=&bstNode[T]{value:v};return};for n:=t.root;;{if v==n.value{return};if v<n.value{if n.left==nil{n.left=&bstNode[T]{value:v};return};n=n.left}else{if n.right==nil{n.right=&bstNode[T]{value:v};return};n=n.right}}}
func(t *BinarySearchTree[T]) Contains(v T)bool{for n:=t.root;n!=nil;{if n.value==v{return true};if v<n.value{n=n.left}else{n=n.right}};return false}
func(t *BinarySearchTree[T]) InOrder()[]T{out:=[]T{};var visit func(*bstNode[T]);visit=func(n *bstNode[T]){if n!=nil{visit(n.left);out=append(out,n.value);visit(n.right)}};visit(t.root);return out}
