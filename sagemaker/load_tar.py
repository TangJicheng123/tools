local_url = "/home/ec2-user/SageMaker/pricenss_pack/{00000000..00000046}.tar"

s3_url = "pipe:aws s3 cp s3://staging-g123-ai/users/tangjicheng/data/{00000000..00000046}.tar -"

import time
import datetime
import webdataset as wds
from torch.utils.data import DataLoader
from tqdm.auto import tqdm
from PIL import Image

def get_wds_loader(url):
    dataset = wds.WebDataset(url)
    dataloader = DataLoader(dataset, batch_size=1, num_workers=4)
    return dataloader

loader = get_wds_loader(s3_url)

def run_test(loader):
    i = 0
    for item in loader:
        short_prompt = item['short_prompt']
        long_prompt = item['long_prompt']
        img = item['img.jpg']
        cond_img = item['cond_img.jpg']
        image_pil = Image.open(img)
        width, height = image_pil.size
        i += 1
        if i % 100 == 0:
            print(f"[{i}] [{datetime.datetime.now()}] long_len:{len(long_prompt)}, {width}, {height}")

if __name__ == "__main__":
    print(f"[{datetime.datetime.now()}] start test")
    start_time = time.time()

    run_test(loader=loader)

    print(f"[{datetime.datetime.now()}] load end")
    end_time = time.time()

    print(f"cost: {end_time - start_time} s")