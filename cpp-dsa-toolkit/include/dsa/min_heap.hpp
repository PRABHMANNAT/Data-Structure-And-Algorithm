#pragma once
#include <functional>
#include <optional>
#include <queue>
#include <vector>
namespace dsa { template<class T,class Compare=std::greater<T>> class MinHeap { std::priority_queue<T,std::vector<T>,Compare> data_;public:void push(T v){data_.push(std::move(v));}[[nodiscard]]std::optional<T> pop(){if(data_.empty())return {};auto v=data_.top();data_.pop();return v;}[[nodiscard]]std::size_t size()const{return data_.size();}[[nodiscard]]bool empty()const{return data_.empty();}}; }
