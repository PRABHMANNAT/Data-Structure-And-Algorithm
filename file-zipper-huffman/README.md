# File Zipper — Huffman Encoding

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Compression room workspace](http://127.0.0.1:8765/file-zipper-huffman/web/).

Compress text with the C++ Huffman codec, decompress it, and verify an exact byte-for-byte round trip.

The interface runs the native C++ implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Repeated language, One symbol.

A C++20 compiler must be available as `g++` or through the `CXX` environment variable. The server builds the checked-in bridge on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free C++20 command-line compressor that creates `.huf` archives using Huffman prefix codes. Archives include a frequency table, allowing deterministic decompression.

```bash
filezip compress input.txt output.huf
filezip decompress output.huf restored.txt
```
