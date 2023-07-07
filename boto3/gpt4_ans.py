import boto3
import io
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def download_part(s3_client, bucket, key, byte_range):
    return s3_client.get_object(Bucket=bucket, Key=key, Range=f"bytes={byte_range[0]}-{byte_range[1]}")['Body'].read()

def download_file(bucket, key, num_threads=10, part_size=1024*1024*5):  # part_size is 5 MB by default
    s3_client = boto3.client('s3')

    # 获取文件大小
    metadata = s3_client.head_object(Bucket=bucket, Key=key)
    file_size = metadata['ContentLength']

    # 计算每一部分的字节范围
    parts = [(i, min(i + part_size, file_size)) for i in range(0, file_size, part_size)]

    # 创建一个线程池
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        download_part_partial = partial(download_part, s3_client, bucket, key)
        file_parts = list(executor.map(download_part_partial, parts))

    # 在内存中合并文件部分
    file_in_memory = io.BytesIO()
    for part in file_parts:
        file_in_memory.write(part)
    
    # 移动内存文件指针至开始
    file_in_memory.seek(0)
    
    # 返回文件对象
    return file_in_memory

# 使用方式:
bucket_name = 'staging-g123-ai'
file_key = 'sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-lv2-SailorVenus-novelai.safetensors'
file_in_memory = download_file(bucket_name, file_key)
