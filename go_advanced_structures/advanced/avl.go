package advanced

type avlNode struct{ key,height int; left,right *avlNode }
type AVL struct{ root *avlNode; size int }
func height(n *avlNode)int{if n==nil{return 0};return n.height}
func max(a,b int)int{if a>b{return a};return b}
func refresh(n *avlNode){n.height=1+max(height(n.left),height(n.right))}
func rotateRight(y *avlNode)*avlNode{x:=y.left;t:=x.right;x.right=y;y.left=t;refresh(y);refresh(x);return x}
func rotateLeft(x *avlNode)*avlNode{y:=x.right;t:=y.left;y.left=x;x.right=t;refresh(x);refresh(y);return y}
func balance(n *avlNode)*avlNode{refresh(n);d:=height(n.left)-height(n.right);if d>1{if height(n.left.left)<height(n.left.right){n.left=rotateLeft(n.left)};return rotateRight(n)};if d < -1 {if height(n.right.right)<height(n.right.left){n.right=rotateRight(n.right)};return rotateLeft(n)};return n}
func insert(n *avlNode,k int)(*avlNode,bool){if n==nil{return &avlNode{key:k,height:1},true};if k<n.key{var add bool;n.left,add=insert(n.left,k);if add{return balance(n),true}}else if k>n.key{var add bool;n.right,add=insert(n.right,k);if add{return balance(n),true}};return n,false}
func (t *AVL) Insert(k int)bool{var added bool;t.root,added=insert(t.root,k);if added{t.size++};return added}
func (t *AVL) Contains(k int)bool{for n:=t.root;n!=nil;{if k==n.key{return true};if k<n.key{n=n.left}else{n=n.right}};return false}
func (t *AVL) Len()int{return t.size}
func (t *AVL) InOrder()[]int{out:=[]int{};var walk func(*avlNode);walk=func(n *avlNode){if n!=nil{walk(n.left);out=append(out,n.key);walk(n.right)}};walk(t.root);return out}
