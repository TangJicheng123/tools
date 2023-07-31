import base64

def encode_base64(data):
    encoded_bytes = base64.b64encode(data)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_data = decoded_bytes.decode('utf-8')
    return decoded_data

# Base64编码示例
data = b'Hello, World!'  # 要编码的数据（字节字符串）
encoded_string = encode_base64(data)
print("Base64编码结果:", encoded_string)

print("encoded data type: ", type(encoded_string))

# Base64解码示例
decoded_data = decode_base64(encoded_string)
print("Base64解码结果:", decoded_data)
