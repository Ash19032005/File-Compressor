import compressor
import os
def compress_folder(input_folder,output_folder):
       for root, _,files in os.walk(input_folder):
              for file in files:
                     input_file_path=os.path.join(root,file)
                     relative_path = os.path.relpath(input_file_path, input_folder)
                     output_file_path = os.path.join(output_folder, relative_path[:-4] + ".fcomp")
                     os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                     print(f"Compressing: {input_file_path} -> {output_file_path}")
                     compressor.compress_file(input_file_path,output_file_path)         

