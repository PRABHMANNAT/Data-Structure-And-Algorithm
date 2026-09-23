package advanced

type DSU struct{ parent,size []int }
func NewDSU(n int)*DSU{p:=make([]int,n);s:=make([]int,n);for i:=range p{p[i]=i;s[i]=1};return &DSU{p,s}}
func (d *DSU) Find(x int)int{if d.parent[x]!=x{d.parent[x]=d.Find(d.parent[x])};return d.parent[x]}
func (d *DSU) Union(a,b int)bool{a=d.Find(a);b=d.Find(b);if a==b{return false};if d.size[a]<d.size[b]{a,b=b,a};d.parent[b]=a;d.size[a]+=d.size[b];return true}
func (d *DSU) Connected(a,b int)bool{return d.Find(a)==d.Find(b)}
