import compressor,decompressor,argparse,folderCompressor,folderdecompressor
def main():
              parser=argparse.ArgumentParser(description="Huffman Folder and File Compressor with SHA-256 & Stats")
              subparsers=parser.add_subparsers(dest="command",help="Available commands")
              # File-compressor command
              compress_parser=subparsers.add_parser("compress",help="Compress a file")
              compress_parser.add_argument("input_file",help="Path to the file to compress")
              compress_parser.add_argument("output_file",help="Name of the compressed output file")

              # File-decompressor command
              decompress_parser=subparsers.add_parser("decompress",help="Decompress a file")
              decompress_parser.add_argument("input_file",help="Path to compressed file")
              decompress_parser.add_argument("output_file",help="Path to save decompressed file")
              decompress_parser.add_argument(
                     "--original",
                     help="Original uncompressed file for SHA-256 check", required=False
              )

              # Folder-Compressor Command
              compress_folder_parser=subparsers.add_parser("compress-folder",help="Compress all files in a folder")
              compress_folder_parser.add_argument("input_folder",help="Input folder path")
              compress_folder_parser.add_argument("output_folder", help="Output folder to store compressed files")

              # Folder decompression
              decompress_folder_parser = subparsers.add_parser("decompress-folder", help="Decompress all files in a folder")
              decompress_folder_parser.add_argument("compressed_folder", help="Path to folder with .fcomp files")
              decompress_folder_parser.add_argument("output_folder", help="Where to save decompressed files")
              decompress_folder_parser.add_argument("--original_folder", help="Folder of original files for SHA-256/stat validation", required=False)

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
              elif args.command == "compress-folder":
                     folderCompressor.compress_folder(args.input_folder, args.output_folder)
                     print(f"✅ Folder compressed: {args.input_folder} -> {args.output_folder}")

              elif args.command == "decompress-folder":
                     folderdecompressor.decompress_folder(
                     args.compressed_folder, args.output_folder, args.original_folder
              )
                     check_content=folderdecompressor.compare_folder(args.output_folder,args.original_folder)
                     print(check_content)
                     if check_content==True:        
                            print(f"✅ Folder decompressed: {args.compressed_folder} -> {args.output_folder}")
                     else:
                             print(f"⚠️ Content Mismatched")
              elif args.command=="hash":
                     hash_val=decompressor.sha_256(args.file)
                     print(f"SHA-256: {hash_val}")
              elif args.command=="stats":
                     decompressor.compression_stats(args.original,args.compressed)
              else:
                     parser.print_help()
main()     

