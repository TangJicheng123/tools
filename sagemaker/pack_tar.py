import os
from webdataset import TarWriter, ShardWriter
from tqdm.auto import tqdm
from PIL import Image
from PIL import ImageFile
import glob
import re

# 使用正则表达式提取数字部分
def extract_numbers_from_string(input_string):
    numbers = re.findall(r'\d+', input_string)
    numbers_as_integers = [int(num) for num in numbers]
    if len(numbers_as_integers) > 0:
        return numbers_as_integers[-1]
    return -1

def pack_tar():
    data_dir = "/home/ec2-user/SageMaker/pricenss"
    output_tar = "/home/ec2-user/SageMaker/pricenss_pack/%08d.tar"
    iter_id = 0
    tar_stream = ShardWriter(output_tar, maxcount=1024)
    for txt_path in tqdm(glob.glob(f"{data_dir}/*_canny_short.txt"), desc=f"Loading image and captions"):
        img_path = txt_path.replace('_canny_short.txt', '.jpg')
        cond_img_path = txt_path.replace('_canny_short.txt', '_canny.jpg')
        long_txt_path = txt_path.replace('_canny_short.txt', '.txt')

        if not os.path.exists(img_path) or not os.path.exists(cond_img_path):
            continue

        with open(txt_path, 'r', buffering=20*1024*1024) as file:
            short_prompt = file.read().rstrip()

        with open(long_txt_path, 'r', buffering=20*1024*1024) as file:
            long_prompt = file.read().rstrip()

        with open(img_path, 'rb') as file:
            img = file.read()

        with open(cond_img_path, 'rb') as file:
            cond_img = file.read()

        sample_id = extract_numbers_from_string(txt_path)

        sample = {
            "__key__": str(iter_id),
            "short_prompt": short_prompt,
            "long_prompt": long_prompt,
            "img.jpg": img,
            "cond_img.jpg": cond_img,
            "sample_id": str(sample_id),
        }

        tar_stream.write(sample)
        iter_id += 1

if __name__ == "__main__":
    pack_tar()