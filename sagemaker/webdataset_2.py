import os
import time
import torch
import webdataset as wds
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader


def get_ori_loader(disk, num_workers):
    def read_bytes(path):
        with open(path, "rb") as f:
            return f.read()

    root = "/mnt/extend/imagenet/train" if disk == "hdd" else "/home/chenyaofo/webdataset-test/train"

    dataset = ImageFolder(root,  loader=read_bytes, is_valid_file=lambda x: True)
    dataloader = DataLoader(dataset, num_workers=num_workers, shuffle=True, batch_size=128)
    return dataloader


def get_wds_loader(disk, num_workers):
    url = "/mnt/extend/tars/imagenet-1k-{000000..000256}.tar" if disk == "hdd" else "/home/chenyaofo/webdataset-test/tars/imagenet-1k-{000000..000256}.tar"

    def my_decoder(key, value):
        if not key.endswith(".jpg"):
            return None
        assert isinstance(value, bytes)
        return value

    dataset = wds.WebDataset(url).shuffle(1000).decode(my_decoder)
    dataloader = DataLoader(dataset, num_workers=num_workers, batch_size=128)
    return dataloader


def run_test(loader, disk):
    N_stop = 30000 if disk == "hdd" else 300000
    start = time.perf_counter()
    total_batch_size = 0
    total_bytes = 0
    for items in loader:
        if isinstance(items, dict):
            batch_size = len(items['jpeg.cls'])
            n_bytes = sum(map(lambda x: len(x), items['jpeg.jpg']))
        else:
            batch_size = len(items[1])
            n_bytes = sum(map(lambda x: len(x), items[0]))
        total_batch_size += batch_size
        # print(total_batch_size)
        total_bytes += n_bytes

        if total_batch_size > N_stop:
            end = time.perf_counter()
            return total_batch_size, total_bytes, end-start


for disk in ["ssd", "hdd"]:
    for get_loader in [get_ori_loader, get_wds_loader]:
        for num_workers in [1, 2, 4, 6, 8]:
            os.system("sync; echo 3 > /proc/sys/vm/drop_caches")
            loader = get_loader(disk, num_workers)
            total_batch_size, total_bytes, time_cost = run_test(loader, disk)
            print(f"{disk}, {get_loader.__name__}, num_workers={num_workers}, fps={total_batch_size/time_cost:.2f}, throughput={total_bytes/(1024)**2/time_cost:.2f} MB/s")