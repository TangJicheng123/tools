from torchdata.datapipes.iter import IterableWrapper, S3FileLister

s3_prefixes = IterableWrapper(['s3://staging-g123-ai/staging-g123-ai/sagemaker/datasets/anime-image/train_data/canny_250k/princess'])

dp_s3_urls = S3FileLister(s3_prefixes)
for d in dp_s3_urls:
    print(d)
    pass

print("****test2*****")

# Functional API
dp_s3_urls = s3_prefixes.list_files_by_s3(request_timeout_ms=100)
for d in dp_s3_urls:
    print(d)
    pass