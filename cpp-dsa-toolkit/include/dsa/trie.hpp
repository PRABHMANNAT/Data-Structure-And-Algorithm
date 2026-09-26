#pragma once
#include <memory>
#include <string_view>
#include <unordered_map>
namespace dsa { class Trie { struct Node{std::unordered_map<char,std::unique_ptr<Node>> next;bool terminal{};};Node root_;public:void insert(std::string_view word){auto*n=&root_;for(char c:word){auto& slot=n->next[c];if(!slot)slot=std::make_unique<Node>();n=slot.get();}n->terminal=true;}bool contains(std::string_view word)const{return locate(word)&&locate(word)->terminal;}bool starts_with(std::string_view prefix)const{return locate(prefix)!=nullptr;}private:const Node* locate(std::string_view s)const{auto*n=&root_;for(char c:s){auto it=n->next.find(c);if(it==n->next.end())return nullptr;n=it->second.get();}return n;}}; }
