#include "huffman/huffman.hpp"
#include <cassert>
#include <fstream>
#include <iterator>
int main(){std::ofstream("round-trip-input.txt",std::ios::binary)<<"huffman huffman huffman";huffman::Codec{}.compress("round-trip-input.txt","round-trip.huf");huffman::Codec{}.decompress("round-trip.huf","round-trip-output.txt");std::ifstream in("round-trip-output.txt",std::ios::binary);std::string restored((std::istreambuf_iterator<char>(in)),{});assert(restored=="huffman huffman huffman");}
