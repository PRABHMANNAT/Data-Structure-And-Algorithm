#include "huffman/huffman.hpp"
#include <iostream>

int main(int argc,char** argv){if(argc!=4){std::cerr<<"usage: filezip <compress|decompress> <input> <output>\n";return 1;}try{huffman::Codec codec;if(std::string(argv[1])=="compress")codec.compress(argv[2],argv[3]);else if(std::string(argv[1])=="decompress")codec.decompress(argv[2],argv[3]);else throw std::runtime_error("unknown mode");}catch(const std::exception& error){std::cerr<<"error: "<<error.what()<<"\n";return 2;}}
