import argparse
import json
import sys
import functools
import operator

def shape2size(shape):
    size = 1
    for iter in shape:
        if iter <= 0:
            print("some shape <= 0")
            continue
        else:
            size *= iter
    return size

def parse_safetensors(safetensors_model, output_json):
    with open(safetensors_model, 'rb') as f:
        byte_data = f.read(8)  # read 8 bytes for unsigned int64
        # or 'big' depending on your data
        length = int.from_bytes(byte_data, byteorder='little')

        json_data = f.read(length).decode('utf-8')
        data = json.loads(json_data)

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=4)

    sum_size = 0
    for item in data:
        if "shape" in data[item]:
            size = functools.reduce(operator.mul, data[item]["shape"], 1)
            if size <= 0:
                print("some shape <= 0")
            sum_size += max(1, size)

    print(f"model size is {sum_size/(1000*1000*1000.0):.2f} billion, {sum_size}")
    print(f"model information saved to {output_json}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse safetensors model file.')
    parser.add_argument('-i', '--safetensors', type=str,
                        help='the safetensors file to parse')
    parser.add_argument('-o', '--json', type=str,
                        help='the file to save model json data')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    parse_safetensors(args.safetensors, args.json)
