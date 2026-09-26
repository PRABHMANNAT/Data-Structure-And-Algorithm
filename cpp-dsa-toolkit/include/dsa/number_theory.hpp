#pragma once
#include <numeric>
#include <vector>
namespace dsa { inline int gcd(int a,int b){return std::gcd(a,b);}inline std::vector<int>sieve(int n){std::vector<bool>marked(n+1);std::vector<int>out;for(int x=2;x<=n;++x)if(!marked[x]){out.push_back(x);if(x<=n/x)for(int y=x*x;y<=n;y+=x)marked[y]=true;}return out;} }
