import compressor,decompressor,argparse
def main():
       parser=argparse.ArgumentParser(description="Huffman File Compressor with SHA-256 & Stats")

       subparsers=parser.add_subparsers(dest="command",help="commands")

       # compress command
       compress_parser=subparsers.add_parser("compress",help="Compress a file")
       compress_parser.add_argument("input_file",help="Path to the file to compress")
       compress_parser.add_argument("output_file",help="Name of the compressed output file")

       # Decompress command
       decompress_parser=subparsers.add_parser("decompress",help="Decompress a file")
       decompress_parser.add_argument("input_file",help="Path to compressed file")
       decompress_parser.add_argument("output_file",help="Path to save decompressed file")
       decompress_parser.add_argument(
              "--original",
              help="Original uncompressed file for SHA-256 check", required=False
       )
       # SHA-256 check command
       hash_parser=subparsers.add_parser("hash",help="Generate SHA-256 hash")
       hash_parser.add_argument("file",help="File to hash")
       # Compression Stats command
       stats_parser=subparsers.add_parser("stats",help="Show compression stats")
       stats_parser.add_argument("original",help="Original file")
       stats_parser.add_argument("compressed",help="Compressed file")
       args=parser.parse_args()
       if args.command=="compress":
              compressor.compress_file(args.input_file,args.output_file)
              print(f"✅ Compressed and saved as: {args.output_file}")
       elif args.command=="decompress":
              compressed_info,decompressed_info=decompressor.decompress_file(args.input_file,args.output_file,args.original)
              print(f"✅ Decompressed and saved as: {args.output_file}")
              if args.original:
                     if compressed_info==decompressed_info:
                            hash_1=decompressor.sha_256(args.original)
                            hash_2=decompressor.sha_256(args.output_file)
                            if hash_1 == hash_2:
                                   print("🔒 SHA-256 Verified: File integrity OK")
                            else:
                                   print("⚠️ Warning: File mismatch detected!")
                     else:
                            print("File content not Matched..")
              
       elif args.command=="hash":
              hash_val=decompressor.sha_256(args.file)
              print(f"SHA-256: {hash_val}")
       elif args.command=="stats":
              decompressor.compression_stats(args.original,args.compressed)
       else:
              parser.print_help()
main()



      