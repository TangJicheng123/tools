tar_dir = "/home/ec2-user/SageMaker/pricenss_pack"
url = "/home/ec2-user/SageMaker/pricenss_pack/{00000000..00000046}.tar"

import time
import webdataset as wds
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

def get_wds_loader():
    dataset = wds.WebDataset(url)
    dataloader = DataLoader(dataset, batch_size=8)
    return dataloader

loader = get_wds_loader()

def run_test(loader):
    i = 0
    for item in loader:
        short = item['short_prompt']
        print(f"[{i}] {len(short)}")
        i += 1

if __name__ == "__main__":
    run_test(loader=loader)