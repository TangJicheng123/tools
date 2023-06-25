import boto3
import concurrent.futures

def download_part(bucket, key, part_number, part_size):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key, 
                             RequestPayer='requester', 
                             PartNumber=part_number,
                             Range=f'bytes={part_number * part_size}-'
                                   f'{(part_number + 1) * part_size - 1}')
    return response['Body'].read()

# 配置 AWS 认证凭据和区域
# 如果你已经在环境中配置了 AWS 认证凭据和默认区域，下面这些代码可以省略
# 请确保已经安装了 Boto3 和 concurrent.futures 模块，可以使用 pip install boto3 futures 命令进行安装

# 替换为你的 AWS 访问密钥 ID
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'

# 替换为你的 AWS 访问密钥
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'

# 替换为你想要使用的 AWS 区域
aws_region = 'us-east-1'

# 配置认证凭据和区域
boto3.setup_default_session(aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name=aws_region)

# 要下载的 S3 存储桶和文件的键
bucket = 'YOUR_S3_BUCKET_NAME'
file_key = 'YOUR_S3_FILE_KEY'

# 设置分块大小（以字节为单位）
part_size = 1024 * 1024  # 1MB

# 创建 S3 客户端
s3 = boto3.client('s3')

# 获取文件信息
response = s3.head_object(Bucket=bucket, Key=file_key)
file_size = response['ContentLength']
num_parts = (file_size + part_size - 1) // part_size

# 使用线程池进行并发下载
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 遍历分块进行并发下载
    download_futures = []
    for part_number in range(num_parts):
        future = executor.submit(download_part, bucket, file_key, part_number, part_size)
        download_futures.append(future)

    # 等待下载任务完成
    downloaded_parts = [future.result() for future in concurrent.futures.as_completed(download_futures)]

# 将下载的分块内容合并为完整的文件内容
file_content = b''.join(downloaded_parts)

# 示例：打印文件内容
print(f"File: {file_key}")
print(file_content)
