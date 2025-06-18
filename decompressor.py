import compressor
import json
import hashlib
import os
def decompress_file(file_path,output_file,original_file_path):
      # load the compressed file
       freq_table,compressed_data=load_compressor(file_path)
       # build the huffman tree
       tree_root=compressor.build_huffman_tree(freq_table)
       original_string=bytes_to_string(compressed_data)
       final_str=remove_padding(original_string)
       decoded_data=decode_bitstring(final_str,tree_root)
       compressed_info,decompressed_info=write_decompressed(file_path,output_file,original_file_path,decoded_data)
       return compressed_info,decompressed_info
def load_compressor(file_path):
       with open(file_path,'rb') as f:
              # Read freq table size
              freq_size_bytes=f.read(4)
              freq_size=int.from_bytes(freq_size_bytes,'big')

              # Read freq table
              freq_bytes=f.read(freq_size)
              freq_json=freq_bytes.decode('utf-8')
              freq_table={int(k):v for k,v in json.loads(freq_json).items()}
              compressed_data=f.read()
       return freq_table,compressed_data




# convert the bytes data into bit string
def bytes_to_string(compressed_bytes):
       bit_string=''
       for bytes in compressed_bytes:
              bit_string+=f"{bytes:08b}"
       return bit_string
# original_string=bytes_to_string(compressed_data)


# remove the padding information
def remove_padding(bit_string):
       padding_len=int(bit_string[:8],2)
       bit_string=bit_string[8:]
       if padding_len>0:
              bit_string=bit_string[:-padding_len]
       return bit_string


def decode_bitstring(bit_string, tree_root):
    decoded_bytes = bytearray()
    node = tree_root
    for bit in bit_string:
        node = node.left if bit == '0' else node.right
        if node.symbol is not None:
            decoded_bytes.append(node.symbol)
            node = tree_root
    return decoded_bytes



# write the decompressed data
def write_decompressed(file_path,output_file,original_file_path,decoded_data):
       with open(output_file, 'wb') as f:
              f.write(decoded_data)
       # check whether the compressed data and decompressed data are same 
       with open(original_file_path) as f:
              compressed_data=f.read()
       with open(output_file) as f:
              decompressed_data=f.read()
       return compressed_data,decompressed_data


# use SHA-256 algorithm for actual data file
def sha_256(file_path):
      sha=hashlib.sha256()
      with open(file_path,'rb') as f:
            while chunk:=f.read(8192):
                  sha.update(chunk)
      return sha.hexdigest()



def check(compressed_data,decompressed_data):
       if compressed_data==decompressed_data:
                     return True
       else:
              return False
       
# Get the compression stats
def compression_stats(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    ratio = (1 - compressed_size / original_size) * 100
    print(f"Original: {original_size} bytes")
    print(f"Compressed: {compressed_size} bytes")
    print(f"Compression Ratio: {ratio:.2f}%")