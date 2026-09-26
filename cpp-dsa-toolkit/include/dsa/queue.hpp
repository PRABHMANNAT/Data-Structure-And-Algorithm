#pragma once
#include <deque>
#include <optional>
#include <utility>
namespace dsa { template<class T> class Queue { std::deque<T> data_; public: void enqueue(T value){data_.push_back(std::move(value));} [[nodiscard]] std::optional<T> dequeue(){if(data_.empty())return {};auto value=std::move(data_.front());data_.pop_front();return value;} [[nodiscard]] std::size_t size()const{return data_.size();} [[nodiscard]] bool empty()const{return data_.empty();} }; }
