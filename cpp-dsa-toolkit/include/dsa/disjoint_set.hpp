#pragma once
#include <numeric>
#include <vector>
namespace dsa { class DisjointSet { std::vector<int> parent_,size_;int groups_;public:explicit DisjointSet(int n):parent_(n),size_(n,1),groups_(n){std::iota(parent_.begin(),parent_.end(),0);}int find(int x){return parent_[x]==x?x:parent_[x]=find(parent_[x]);}bool unite(int a,int b){a=find(a);b=find(b);if(a==b)return false;if(size_[a]<size_[b])std::swap(a,b);parent_[b]=a;size_[a]+=size_[b];--groups_;return true;}bool connected(int a,int b){return find(a)==find(b);}int groups()const{return groups_;}}; }
