local_url = "/home/ec2-user/SageMaker/pricenss_pack/{00000000..00000046}.tar"

s3_url = "pipe:aws s3 cp s3://staging-g123-ai/users/tangjicheng/data/{00000000..00000046}.tar -"

import time
import datetime
import webdataset as wds
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

def get_wds_loader(url):
    dataset = wds.WebDataset(url)
    dataloader = DataLoader(dataset, batch_size=8, num_workers=4)
    return dataloader

loader = get_wds_loader(s3_url)

def run_test(loader):
    i = 0
    for item in loader:
        short = item['short_prompt']
        i += 1
        if i % 100 == 0:
            print(f"[{i}] {short}")

if __name__ == "__main__":
    print(f"[{datetime.datetime.now()}] start test")
    start_time = time.time()

    run_test(loader=loader)

    print(f"[{datetime.datetime.now()}] load end")
    end_time = time.time()

    print(f"cost: {end_time - start_time} s")