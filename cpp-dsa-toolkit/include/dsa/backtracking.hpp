#pragma once
#include <vector>
#include <utility>
namespace dsa { template<class T>std::vector<std::vector<T>>permutations(std::vector<T>values){std::vector<std::vector<T>>out;auto visit=[&](auto&&self,int at)->void{if(at==static_cast<int>(values.size())){out.push_back(values);return;}for(int i=at;i<static_cast<int>(values.size());++i){std::swap(values[at],values[i]);self(self,at+1);std::swap(values[at],values[i]);}};visit(visit,0);return out;}inline int n_queens(int n){int count=0;std::vector<bool>col(n),a(2*n),b(2*n);auto place=[&](auto&&self,int row)->void{if(row==n){++count;return;}for(int c=0;c<n;++c)if(!col[c]&&!a[row-c+n]&&!b[row+c]){col[c]=a[row-c+n]=b[row+c]=true;self(self,row+1);col[c]=a[row-c+n]=b[row+c]=false;}};place(place,0);return count;} }
