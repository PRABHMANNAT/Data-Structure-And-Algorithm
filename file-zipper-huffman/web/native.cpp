#include "huffman/huffman.hpp"
    #include <iostream>
    #include <string>
    int main(){try{std::string source,archive,decoded;std::getline(std::cin,source);std::getline(std::cin,archive);std::getline(std::cin,decoded);huffman::Codec codec;codec.compress(source,archive);codec.decompress(archive,decoded);std::cout<<"ok\n";}catch(const std::exception& error){std::cerr<<error.what();return 2;}}
