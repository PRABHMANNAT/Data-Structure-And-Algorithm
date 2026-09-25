#include "huffman/huffman.hpp"
#include <array>
#include <cstdint>
#include <fstream>
#include <memory>
#include <queue>
#include <stdexcept>
#include <string>
#include <vector>

namespace huffman {
namespace {
struct Node { std::uint64_t frequency{}; int symbol{-1}; std::shared_ptr<Node> left, right; bool leaf() const { return !left && !right; } };
using NodePtr = std::shared_ptr<Node>;
struct Earlier { bool operator()(const NodePtr& a, const NodePtr& b) const { return a->frequency > b->frequency; } };
NodePtr tree(const std::array<std::uint64_t,256>& frequencies) { std::priority_queue<NodePtr,std::vector<NodePtr>,Earlier> heap; for(int i=0;i<256;++i) if(frequencies[i]) heap.push(std::make_shared<Node>(Node{frequencies[i],i})); if(heap.empty()) return {}; if(heap.size()==1) return heap.top(); while(heap.size()>1){auto a=heap.top();heap.pop();auto b=heap.top();heap.pop();heap.push(std::make_shared<Node>(Node{a->frequency+b->frequency,-1,a,b}));} return heap.top(); }
void codes(const NodePtr& node, const std::string& path, std::array<std::string,256>& out) { if(node->leaf()){out[node->symbol]=path.empty()?"0":path;return;} codes(node->left,path+"0",out);codes(node->right,path+"1",out); }
void write_u64(std::ostream& out,std::uint64_t value){for(int i=0;i<8;++i)out.put(static_cast<char>((value>>(i*8))&0xff));}
std::uint64_t read_u64(std::istream& in){std::uint64_t value=0;for(int i=0;i<8;++i){auto c=in.get();if(c==EOF)throw std::runtime_error("truncated archive header");value|=std::uint64_t(static_cast<unsigned char>(c))<<(i*8);}return value;}
}
void Codec::compress(const std::filesystem::path& input,const std::filesystem::path& archive) const { std::ifstream in(input,std::ios::binary);if(!in)throw std::runtime_error("cannot read input");std::vector<unsigned char> data((std::istreambuf_iterator<char>(in)),{});std::array<std::uint64_t,256> freq{};for(auto b:data)++freq[b];auto root=tree(freq);std::array<std::string,256> table{};if(root)codes(root,"",table);std::ofstream out(archive,std::ios::binary);if(!out)throw std::runtime_error("cannot write archive");out.write("HUF1",4);write_u64(out,data.size());for(auto n:freq)write_u64(out,n);unsigned char byte=0;int bits=0;for(auto b:data)for(char bit:table[b]){byte=(byte<<1)|(bit-'0');if(++bits==8){out.put(byte);byte=0;bits=0;}}if(bits)out.put(byte<<(8-bits)); }
void Codec::decompress(const std::filesystem::path& archive,const std::filesystem::path& output) const { std::ifstream in(archive,std::ios::binary);if(!in)throw std::runtime_error("cannot read archive");char magic[4];in.read(magic,4);if(std::string(magic,4)!="HUF1")throw std::runtime_error("unsupported archive");auto count=read_u64(in);std::array<std::uint64_t,256> freq{};for(auto& n:freq)n=read_u64(in);std::ofstream out(output,std::ios::binary);if(!out)throw std::runtime_error("cannot write output");auto root=tree(freq);if(!root)return;if(root->leaf()){for(std::uint64_t i=0;i<count;++i)out.put(static_cast<char>(root->symbol));return;}auto node=root;std::uint64_t written=0;char raw;while(written<count&&in.get(raw)){auto byte=static_cast<unsigned char>(raw);for(int shift=7;shift>=0&&written<count;--shift){node=((byte>>shift)&1)?node->right:node->left;if(node->leaf()){out.put(static_cast<char>(node->symbol));++written;node=root;}}}if(written!=count)throw std::runtime_error("truncated archive payload"); }
}
