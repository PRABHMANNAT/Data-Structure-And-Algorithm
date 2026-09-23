package advanced

type SegmentTree struct{ n int; tree []int }
func NewSegmentTree(values []int)*SegmentTree{n:=1;for n<len(values){n*=2};t:=&SegmentTree{n:n,tree:make([]int,2*n)};copy(t.tree[n:],values);for i:=n-1;i>0;i--{t.tree[i]=t.tree[2*i]+t.tree[2*i+1]};return t}
func (t *SegmentTree) Set(index,value int)error{if index<0||index>=t.n{return ErrInvalidRange};i:=t.n+index;t.tree[i]=value;for i/=2;i>0;i/=2{t.tree[i]=t.tree[2*i]+t.tree[2*i+1]};return nil}
func (t *SegmentTree) Sum(left,right int)(int,error){if left<0||right<left||right>=t.n{return 0,ErrInvalidRange};left+=t.n;right+=t.n;s:=0;for left<=right{if left%2==1{s+=t.tree[left];left++};if right%2==0{s+=t.tree[right];right--};left/=2;right/=2};return s,nil}
