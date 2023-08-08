import os
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


entries = load_dataset(
    '/home/ec2-user/SageMaker/s4mount/staging-g123-ai/sagemaker/datasets/anime-image/train_data/canny_250k/princess')
