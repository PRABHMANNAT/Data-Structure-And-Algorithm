#pragma once

#include <filesystem>

namespace huffman {
class Codec {
 public:
  void compress(const std::filesystem::path& input, const std::filesystem::path& archive) const;
  void decompress(const std::filesystem::path& archive, const std::filesystem::path& output) const;
};
}
