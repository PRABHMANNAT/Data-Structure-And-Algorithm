#pragma once
#include <list>
#include <optional>
#include <stdexcept>
#include <utility>
#include <unordered_map>
namespace dsa { template<class K,class V> class LruCache { using Item=std::pair<K,V>;std::size_t capacity_;std::list<Item> order_;std::unordered_map<K,typename std::list<Item>::iterator> index_;public:explicit LruCache(std::size_t c):capacity_(c){if(!c)throw std::invalid_argument("capacity must be positive");}std::optional<V> get(const K&k){auto it=index_.find(k);if(it==index_.end())return {};order_.splice(order_.begin(),order_,it->second);return it->second->second;}void put(K k,V v){auto it=index_.find(k);if(it!=index_.end()){it->second->second=std::move(v);order_.splice(order_.begin(),order_,it->second);return;}order_.emplace_front(std::move(k),std::move(v));index_[order_.front().first]=order_.begin();if(index_.size()>capacity_){index_.erase(order_.back().first);order_.pop_back();}}std::size_t size()const{return index_.size();}}; }
