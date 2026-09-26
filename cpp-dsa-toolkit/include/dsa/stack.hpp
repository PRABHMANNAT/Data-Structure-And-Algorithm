#pragma once
#include <optional>
#include <utility>
#include <vector>
namespace dsa { template<class T> class Stack { std::vector<T> data_; public: void push(T value){data_.push_back(std::move(value));} [[nodiscard]] std::optional<T> pop(){if(data_.empty())return {};auto value=std::move(data_.back());data_.pop_back();return value;} [[nodiscard]] std::size_t size()const{return data_.size();} [[nodiscard]] bool empty()const{return data_.empty();} }; }
