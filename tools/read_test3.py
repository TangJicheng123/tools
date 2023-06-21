import os
import time
import argparse
import sys
import multiprocessing

def read_file(filename, k):
    start_time = time.time()
    # Read file content into memory
    with open(filename, 'rb', buffering=200*1024*1024) as file:
        content = file.read()
    file_size = sys.getsizeof(content)
    end_time = time.time()
    read_time = end_time - start_time
    print(f"[process {k}] file [{os.path.basename(filename)}] read time: {read_time:.2f} seconds, size: {file_size / (1024*1024)} MB")
    return read_time

def read_files_in_folder(folder_path, k, N):
    for filename in os.listdir(folder_path)[k::N]:
        full_filepath = os.path.join(folder_path, filename)
        if os.path.isfile(full_filepath):
            read_file(full_filepath, k)

if __name__ == "__main__":
    # usage: python this.py --path /your/file/path --task numbers_of_processes

    parser = argparse.ArgumentParser(description='File Read Time Test')
    parser.add_argument('--path', type=str, help='Path of the file to read')
    parser.add_argument('--task', type=int, help='Numbers of processes')
    args = parser.parse_args()
    N = args.task
    folder_path = args.path

    processes = []
    for k in range(N):
        p = multiprocessing.Process(target=read_files_in_folder, args=(folder_path, k, N))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()