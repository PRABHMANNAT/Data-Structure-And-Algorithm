#include <cassert>
#include "dsa/avl_tree.hpp"
#include "dsa/disjoint_set.hpp"
#include "dsa/lru_cache.hpp"
#include "dsa/min_heap.hpp"
#include "dsa/stack.hpp"
#include "dsa/trie.hpp"
int main(){dsa::Stack<int>s;s.push(4);assert(s.pop()==4);dsa::MinHeap<int>h;h.push(3);h.push(1);assert(h.pop()==1);dsa::DisjointSet d(3);d.unite(0,1);assert(d.connected(0,1));dsa::Trie t;t.insert("tree");assert(t.contains("tree"));dsa::AvlTree<int>a;a.insert(3);a.insert(2);a.insert(1);assert(a.contains(2));dsa::LruCache<int,int>c(1);c.put(1,2);assert(c.get(1)==2);}
