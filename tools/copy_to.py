import os
import shutil
import time

def copy_files_with_prefix_suffix(source_dir, destination_dir, prefix, suffix):
    os.makedirs(destination_dir, exist_ok=True)

    i = 0
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.startswith(prefix) and file.endswith(suffix):
                start_time = time.time()
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_dir, file)
                shutil.copy2(source_file_path, destination_file_path)
                end_time = time.time()

                print(f"[{i}] copy file : {source_file_path} -> {destination_file_path} , cost: {end_time-start_time}s")
                i += 1
                if i > 20:
                    return

source_directory = "/s3/mount/sagemaker/model/diffusion_model/deploy/Stable-diffusion"
destination_directory = "/content/models"
prefix_to_match = "artifex-testapp"
suffix_to_match = ".safetensors"

copy_files_with_prefix_suffix(source_directory, destination_directory, prefix_to_match, suffix_to_match)
