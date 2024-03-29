import os
import time
import datetime
from tqdm.auto import tqdm
from PIL import Image
from PIL import ImageFile
import glob
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

def load_dataset(data_dir):
    """
    Load dataset to entries.
    Format of entry: (img_path, cond_img_path, prompt)
    """

    entries = {}
    for txt_path in tqdm(glob.glob(f"{data_dir}/*_canny_short.txt"), desc=f"Loading image and captions"):
        img_path = txt_path.replace('_canny_short.txt', '.jpg')
        cond_img_path = txt_path.replace('_canny_short.txt', '_canny.jpg')
        long_txt_path = txt_path.replace('_canny_short.txt', '.txt')

        with open(txt_path, 'r', buffering=20*1024*1024) as file:
            short_prompt = file.read().rstrip()

        with open(long_txt_path, 'r', buffering=20*1024*1024) as file:
            long_prompt = file.read().rstrip()

        if not os.path.exists(img_path) or not os.path.exists(cond_img_path):
            continue

        with open(img_path, 'rb') as file:
            img = file.read()

        with open(cond_img_path, 'rb') as file:
            cond_img = file.read()

        entry = (img_path, cond_img_path, short_prompt, long_prompt)
        # entries.append(entry)
        entries[txt_path] = entry

    return entries


def get_id_res_map(entries):
    id_res_map = {}
    for entry_id in tqdm(entries, desc=f"Loading resolutions"):
        entry = entries[entry_id]
        with Image.open(entry[0]) as img:
            size = img.size
        id_res_map[entry_id] = size
    return id_res_map

data_dir = '/home/ec2-user/SageMaker/s3mount/sagemaker/datasets/anime-image/train_data/canny_250k/princess'
data_dir = '/home/ec2-user/SageMaker/pricenss'


print(f"[{datetime.datetime.now()}] data_dir: {data_dir}")
start_time = time.time()

entries = load_dataset(data_dir=data_dir)

print(f"[{datetime.datetime.now()}] load end")
end_time = time.time()

print(f"cost: {end_time - start_time} s")