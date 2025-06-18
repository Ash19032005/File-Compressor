# Count the frequencies of the character from the file
from collections import Counter
import heapq

# main function of compressor.py
def compress_file(file_path,output_file):
       # main code
       char_freq=count_frequencies(file_path)
       # print(char_freq)
       tree_root=build_huffman_tree(char_freq)
       assign_huffman_codes(tree_root,code='')
       encoded_format=encode_file(file_path,code_map)
       print("encoded format",encoded_format)
       save_compressed_file(output_file, encoded_format, char_freq)


def count_frequencies(filepath):
       with open(filepath,'rb') as f:
              data=f.read()
              freq=Counter(data)
       return freq

# Node
class Node:
       def __init__(self,symbol,freq,left=None,right=None):
              self.symbol=symbol
              self.freq=freq
              self.left=left
              self.right=right
       def __lt__(self,other):
              return self.freq<other.freq

def build_huffman_tree(freq):
       heap=[Node(symbol=byte,freq=cnt) for byte,cnt in freq.items()]
       heapq.heapify(heap)
       while len(heap)>1:
              min_node_1=heapq.heappop(heap)
              min_node_2=heapq.heappop(heap)
              merged_node=Node(symbol=None,
                               freq=min_node_1.freq+min_node_2.freq,
                               left=min_node_1,right=min_node_2)
              heapq.heappush(heap,merged_node)
       return heap[0]



code_map={}
def assign_huffman_codes(node,code):
       global code_map
       if node is None:
              return 
       if node.symbol is not None:
              code_map[node.symbol]=code
              return code
       assign_huffman_codes(node.left,code+'0')
       assign_huffman_codes(node.right,code+'1')






# encode the file using the huffman codes
def encode_file(filepath,codes):
       with open(filepath,'rb') as f:
              data=f.read()
       bit_string=''.join([code_map[byte] for byte in data])
       # To represent the bits in bytes we are doing padding here
       extra_padding = 8 - len(bit_string) % 8
       bit_string += '0' * extra_padding
       padded_info = f"{extra_padding:08b}"
       bit_string = padded_info + bit_string
       # convert the bit_string to bytes
       b=bytearray()
       for i in range(0,len(bit_string),8):
              current_byte=bit_string[i:i+8]
              b.append(int(current_byte,2))
       return b



import json
def save_compressed_file(output_path, compressed_bytes, freq_table):
    # Convert frequency table to JSON string
    freq_json = json.dumps({str(k): v for k, v in freq_table.items()})
    freq_bytes = freq_json.encode('utf-8')
    freq_size = len(freq_bytes)
    with open(output_path, 'wb') as out:
        # First 4 bytes: size of frequency table (so we know where compressed data starts)
        out.write(freq_size.to_bytes(4, byteorder='big'))
        # Next: frequency table itself
        out.write(freq_bytes)
        # Finally: compressed data
        out.write(compressed_bytes)








