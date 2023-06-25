import boto3
import threading
import os

# 配置S3连接
s3 = boto3.client('s3')

# 定义下载的S3对象和线程数
bucket_name = 'staging-g123-ai'
object_key = 'sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-lv2-SailorVenus-novelai.safetensors'
num_threads = 8

# 获取文件的大小
response = s3.head_object(Bucket=bucket_name, Key=object_key)
file_size = response['ContentLength']

# 计算每个线程要下载的块大小
chunk_size = file_size // num_threads
remainder = file_size % num_threads

# 定义下载块的函数
def download_chunk(start_byte, end_byte, thread_id):
    # 设置下载范围
    range_header = f"bytes={start_byte}-{end_byte}"

    # 发起S3请求，获取文件块
    response = s3.get_object(Bucket=bucket_name, Key=object_key, Range=range_header)
    chunk_data = response['Body'].read()

    # 将块数据存储在相应的位置
    with open(f"chunk_{thread_id}.bin", "wb") as file:
        file.write(chunk_data)

# 创建并启动下载线程
threads = []
for i in range(num_threads):
    start_byte = i * chunk_size
    end_byte = start_byte + chunk_size - 1

    # 最后一个线程处理剩余的字节
    if i == num_threads - 1:
        end_byte += remainder

    thread = threading.Thread(target=download_chunk, args=(start_byte, end_byte, i))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 将下载的块合并为最终的文件
with open("final_file.bin", "wb") as final_file:
    for i in range(num_threads):
        with open(f"chunk_{i}.bin", "rb") as chunk_file:
            final_file.write(chunk_file.read())

# 删除临时的块文件
for i in range(num_threads):
    os.remove(f"chunk_{i}.bin")
