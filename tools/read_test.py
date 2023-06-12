import argparse
import time

def read_file(file_path):
    # Read file content into memory
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description='File Read Time Test')

    # Add file path argument
    parser.add_argument('--file', type=str, help='Path of the file to read')

    # Parse command-line arguments
    args = parser.parse_args()

    N = 10
    for i in range(N):
        # Record start time
        start_time = time.time()
        # Read file content
        content = read_file(args.file)
        # Calculate read time
        end_time = time.time()
        read_time = end_time - start_time
        # Output read time
        print(f"File read time: {read_time:.2f} seconds")
