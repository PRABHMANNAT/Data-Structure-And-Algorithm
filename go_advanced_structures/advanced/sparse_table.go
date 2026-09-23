package advanced

type SparseTable struct{ table [][]int; log []int }
func NewSparseTable(values []int)*SparseTable{n:=len(values);lg:=make([]int,n+1);for i:=2;i<=n;i++{lg[i]=lg[i/2]+1};levels:=0;if n>0{levels=lg[n]+1};tab:=make([][]int,levels);if n>0{tab[0]=append([]int(nil),values...);for k:=1;k<levels;k++{width:=n-(1<<k)+1;tab[k]=make([]int,width);for i:=range tab[k]{tab[k][i]=min(tab[k-1][i],tab[k-1][i+(1<<(k-1))])}}};return &SparseTable{tab,lg}}
func min(a,b int)int{if a<b{return a};return b}
func (s *SparseTable) Min(left,right int)(int,error){if left<0||right<left||right>=len(s.log)-1{return 0,ErrInvalidRange};k:=s.log[right-left+1];return min(s.table[k][left],s.table[k][right-(1<<k)+1]),nil}
