import boto3
from io import BytesIO

import time

# 配置认证凭据和区域
boto3.setup_default_session()

# 要下载的 S3 存储桶和文件的键
bucket = 'staging-g123-ai'
file_key = 'sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-lv2-SailorVenus-novelai.safetensors'

# 创建 S3 客户端
s3 = boto3.client('s3')

# 设置下载分块大小（以字节为单位）
chunk_size = 1024 * 1024  # 1MB

start_time = time.time()

# 创建 BytesIO 对象，用于保存文件内容
file_object = BytesIO()

# 下载文件到内存中，设置分块大小
response = s3.get_object(Bucket=bucket, Key=file_key, 
                         RequestPayer='requester', 
                         PartSize=chunk_size)

# 分块读取并写入到 BytesIO 对象中
for chunk in response['Body'].iter_chunks(chunk_size=chunk_size):
    file_object.write(chunk)

# 将文件对象指针重置到文件开头
file_object.seek(0)

# 使用文件对象进行进一步处理
# 示例：打印文件内容
print(f"File: {file_key}")
file_content = file_object.read()
# print(file_content)

end_time = time.time()

print(f"cost: {end_time - start_time}")