# HuffmanCompressor

A Python-based command-line tool for compressing and decompressing files and folders using Huffman coding. Supports SHA-256 hashing for integrity verification and provides compression statistics.

---

## 🔧 Features

- 📦 Lossless file and folder compression using Huffman Encoding
- 🔐 SHA-256 hash verification for file integrity
- 📊 Displays compression statistics
- 🧭 Command-Line Interface (CLI) for seamless interaction
- 🗂️ Recursive folder compression with preserved structure

---

## 📈 Compression Example

- Original file size: 169,901 bytes  
- Compressed file size: 95,893 bytes  
- Compression Ratio: 43.56%

---

## 📁 Project Structure

HuffmanCompressor/
│
├── compressor.py # File compression logic
├── decompressor.py # File decompression, SHA-256, and stats
├── cli.py # CLI driver script
├── folder_compress.py # Folder compression
├── folder_decompress.py # Folder decompression
├── testfiles/ # Sample test files
├── Compressed/ # Output folder for compressed data
├── Decompressed/ # Output folder for decompressed data
└── README.md

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/HuffmanCompressor.git
cd HuffmanCompressor

-compress a single file
python cli.py compress input.txt output.fcomp

-Decompress a single file
python cli.py decompress output.fcomp output.txt --original input.txt

-Hash the file
python cli.py hash input.txt

-Compression Stats
python cli.py stats input.txt output.fcomp

-Compress the folder
python folder_compress.py

-Decompress the folder
python folder_decompress.py

✅ Decompressed and saved as: output.txt  
🔒 SHA-256 Verified: File integrity OK
