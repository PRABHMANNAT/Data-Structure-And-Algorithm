#pragma once
#include <deque>
#include <optional>
#include <utility>
namespace dsa { template<class T> class Deque { std::deque<T> data_; public: void push_front(T v){data_.push_front(std::move(v));} void push_back(T v){data_.push_back(std::move(v));} [[nodiscard]] std::optional<T> pop_front(){if(data_.empty())return {};auto v=std::move(data_.front());data_.pop_front();return v;} [[nodiscard]] std::optional<T> pop_back(){if(data_.empty())return {};auto v=std::move(data_.back());data_.pop_back();return v;} [[nodiscard]] std::size_t size()const{return data_.size();} }; }
