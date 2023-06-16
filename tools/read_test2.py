import os
import time
import argparse
import sys

def read_file(filename):
    start_time = time.time()
    if os.path.basename(filename) == "Lyriel-1.5.safetensors":
        return None
    # Read file content into memory
    with open(filename, 'rb', buffering=200*1024*1024) as file:
        content = file.read()
    file_size = sys.getsizeof(content)
    end_time = time.time()
    read_time = end_time - start_time
    print(f"file [{os.path.basename(filename)}] read time: {read_time:.2f} seconds, size: {file_size / (1024*1024)} MB")
    return read_time

def read_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        full_filepath = os.path.join(folder_path, filename)
        if os.path.isfile(full_filepath):
            read_file(full_filepath)
            time.sleep(10)

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description='File Read Time Test')
    # Add file path argument
    parser.add_argument('--path', type=str, help='Path of the file to read')
    # Parse command-line arguments
    args = parser.parse_args()

    folder_path = args.path
    read_files_in_folder(folder_path)
