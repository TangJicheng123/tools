import boto3
import time 
from io import BytesIO

chunk_size = 1024 * 1024

def download_file_from_s3(bucket_name, key):
    s3 = boto3.resource('s3')
    # obj = s3.Object(bucket_name, key)
    # response = obj.get()
    # content = response['Body'].read()
    file_object = BytesIO()
    response = s3.get_object(Bucket=bucket, Key=file_key, 
                            RequestPayer='requester', 
                            PartSize=chunk_size)
    for chunk in response['Body'].iter_chunks(chunk_size=chunk_size):
        file_object.write(chunk)
    file_object.seek(0)
    return file_object

boto3.setup_default_session()

bucket = 'staging-g123-ai'
file_key = 'sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-lv2-SailorVenus-novelai.safetensors'

start_time = time.time()

file_content = download_file_from_s3(bucket, file_key)

end_time = time.time()

# print(file_content)
print(f"ok, cost: {end_time - start_time}")
