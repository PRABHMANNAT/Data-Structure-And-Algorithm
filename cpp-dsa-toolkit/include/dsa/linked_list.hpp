#pragma once
#include <memory>
#include <vector>
#include <utility>
namespace dsa { template<class T> class LinkedList { struct Node{T value;std::unique_ptr<Node> next;};std::unique_ptr<Node> head_;Node* tail_{};std::size_t size_{};public:void push_front(T v){auto n=std::make_unique<Node>(std::move(v),std::move(head_));if(!tail_)tail_=n.get();head_=std::move(n);++size_;}void push_back(T v){auto n=std::make_unique<Node>(std::move(v),nullptr);auto* raw=n.get();if(tail_)tail_->next=std::move(n);else head_=std::move(n);tail_=raw;++size_;}[[nodiscard]]std::vector<T> values()const{std::vector<T> out;for(auto*n=head_.get();n;n=n->next.get())out.push_back(n->value);return out;}[[nodiscard]]std::size_t size()const{return size_;}}; }
