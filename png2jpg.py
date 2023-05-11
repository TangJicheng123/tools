import argparse
from PIL import Image
import os

def convert_images(src_dir, dst_dir):
    # 遍历源目录中的所有 PNG 图片
    for filename in os.listdir(src_dir):
        if filename.endswith('.png'):
            # 生成目标文件名
            basename = os.path.splitext(filename)[0]
            dst_filename = basename + '.jpg'
            dst_path = os.path.join(dst_dir, dst_filename)

            # 打开 PNG 文件并保存为 JPG 格式
            src_path = os.path.join(src_dir, filename)
            with Image.open(src_path) as img:
                img = img.convert('RGB')
                img.save(dst_path)

            print(f'Converted {src_path} to {dst_path}')

if __name__ == '__main__':
    # 定义命令行参数
    parser = argparse.ArgumentParser(description='Convert PNG images to JPG format')
    parser.add_argument('--src_dir', help='source directory containing PNG images')
    parser.add_argument('--dst_dir', help='destination directory to save JPG images')
    args = parser.parse_args()

    # 调用 convert_images 函数
    convert_images(args.src_dir, args.dst_dir)
