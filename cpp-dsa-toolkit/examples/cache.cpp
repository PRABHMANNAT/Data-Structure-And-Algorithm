#include <cassert>
#include "dsa/lru_cache.hpp"
int main(){dsa::LruCache<int,int>cache(2);cache.put(1,10);cache.put(2,20);cache.get(1);cache.put(3,30);assert(!cache.get(2));}
