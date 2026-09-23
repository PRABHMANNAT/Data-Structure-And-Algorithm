package advanced

type Fenwick struct{ tree []int }
func NewFenwick(n int)*Fenwick{return &Fenwick{tree:make([]int,n+1)}}
func (f *Fenwick) Add(i,delta int){for i++;i<len(f.tree);i+=i&-i{f.tree[i]+=delta}}
func (f *Fenwick) Prefix(i int)int{s:=0;for i++;i>0;i-=i&-i{s+=f.tree[i]};return s}
func (f *Fenwick) Range(left,right int)(int,error){if left<0||right<left||right>=len(f.tree)-1{return 0,ErrInvalidRange};s:=f.Prefix(right);if left>0{s-=f.Prefix(left-1)};return s,nil}
