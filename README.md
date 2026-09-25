# File Zipper — Huffman Encoding

A dependency-free C++20 command-line compressor that creates `.huf` archives using Huffman prefix codes. Archives include a frequency table, allowing deterministic decompression.

```bash
filezip compress input.txt output.huf
filezip decompress output.huf restored.txt
```
