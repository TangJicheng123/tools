import argparse
import json


def parse_safetensors(safetensors_model, output_json):
    with open(safetensors_model, 'rb') as f:
        byte_data = f.read(8)  # read 8 bytes for unsigned int64
        # or 'big' depending on your data
        length = int.from_bytes(byte_data, byteorder='little')

        json_data = f.read(length).decode('utf-8')
        data = json.loads(json_data)

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"model information saved to {output_json}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse safetensors model file.')
    parser.add_argument('--safetensors', type=str,
                        help='the safetensors file to parse')
    parser.add_argument('--json', type=str,
                        help='the file to save model json data')

    args = parser.parse_args()

    parse_safetensors(args.safetensors, args.json)
