import datetime

from torchdata.datapipes.iter import IterableWrapper, S3FileLoader

dp_s3_urls = IterableWrapper(['s3://staging-g123-ai/users/tangjicheng/p2.tar']).list_files_by_s3()
print(f"[{datetime.datetime.now()}] dp_s3_urls: {dp_s3_urls}")
# In order to make sure data are shuffled and sharded in the
# distributed environment, `shuffle`  and `sharding_filter`
# are required. For detail, please check our tutorial in:
# https://pytorch.org/data/main/tutorial.html#working-with-dataloader
sharded_s3_urls = dp_s3_urls.shuffle().sharding_filter()

dp_s3_files = S3FileLoader(sharded_s3_urls)
i = 0
# for url, fd in dp_s3_files: # Start loading data
#     data = fd.read()

print(f"[{datetime.datetime.now()}] Functional API")
print(f"sharded_s3_urls.load_files_by_s3: {sharded_s3_urls.load_files_by_s3}")
# Functional API
dp_s3_files = sharded_s3_urls.load_files_by_s3(buffer_size=256)
for url, fd in dp_s3_files:
    data = fd.read()
    i += 1
    print(f"i: {i}")

print(f"[{datetime.datetime.now()}] End")