import decompressor
import os
def get_files(folder_path,file_index):
       index=0
       for root,_,files in os.walk(folder_path):
              for file in files:
                     if index==file_index:
                            original_file_path=os.path.join(root,file)
                            return original_file_path
                     else:
                            index+=1
def decompress_folder(compressed_folder,output_folder,original_folder):
       for root,_,files in os.walk(compressed_folder):
              file_index=0
              for file in files:
                     input_file_path=os.path.join(root,file)
                     relative_path = os.path.relpath(input_file_path,compressed_folder)
                     original_filename=os.path.splitext(relative_path)[0]
                     output_file_path = os.path.join(output_folder, original_filename+".txt")
                     os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                     print(f"Decompressing: {input_file_path} -> {output_file_path}")
                     original_file_path=get_files(original_folder,file_index)
                     decompressor.decompress_file(input_file_path,output_file_path,original_file_path)
              file_index+=1
# decompress_folder("Compressed","Decompressed","testfiles")


def compare_folder(decompressed_folder,original_folder):
       decompressed_file_arr=[]
       original_file_arr=[]
       for root,_,files in os.walk(decompressed_folder):
              for file in files:
                     input_file_path=os.path.join(root,file)
                     decompressed_file_arr.append(input_file_path)       
       for root,_,files in os.walk(original_folder):
              for file in files:
                     input_file_path=os.path.join(root,file)
                     original_file_arr.append(input_file_path)
       if len(original_file_arr)!=len(decompressed_file_arr):
              print("Length of Decompressed and Original folder is mismatched")
       else:
              ans=[False]*len(original_file_arr)
              for i in range(len(original_file_arr)):
                     with open(original_file_arr[i],'r') as f1:
                            data_1=f1.read()
                     with open(decompressed_file_arr[i],'r') as f2:
                            data_2=f2.read()
                     ans[i]=True if data_1==data_2 else False
              return ans.count(True)==len(original_file_arr)
compare_folder("Decompressed","testfiles")




