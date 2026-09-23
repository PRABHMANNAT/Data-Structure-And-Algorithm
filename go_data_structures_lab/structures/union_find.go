package structures

type UnionFind struct{ parent,size []int }
func NewUnionFind(n int)*UnionFind{p:=make([]int,n);s:=make([]int,n);for i:=range p{p[i]=i;s[i]=1};return &UnionFind{p,s}}
func (u *UnionFind) Find(x int)int{if u.parent[x]!=x{u.parent[x]=u.Find(u.parent[x])};return u.parent[x]}
func (u *UnionFind) Union(a,b int)bool{a=u.Find(a);b=u.Find(b);if a==b{return false};if u.size[a]<u.size[b]{a,b=b,a};u.parent[b]=a;u.size[a]+=u.size[b];return true}
func (u *UnionFind) Connected(a,b int)bool{return u.Find(a)==u.Find(b)}
