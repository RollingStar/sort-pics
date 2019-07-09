import argparse
import os
from collections import Counter
from shutil import move
from PIL import Image

#if no dir is specified on the command line
DEFAULT_DIR = r'C:\\PATH_HERE'
WIDE_STR = 'wide'
TALL_STR = 'tall'
SQUARE_STR = 'square'

def sort_images(folder):
    folder = os.fsencode(folder)
    counts = []
    for leaf in os.scandir(folder):
        if leaf.is_file():
            aspect = get_aspect(leaf.path)
            counts.append(aspect)
            new_path = os.path.join(os.fsdecode(folder), aspect, os.fsdecode(leaf.name))
            print(new_path)
            move(leaf.path, new_path)
    print(Counter(counts))

def get_aspect(file):
    im = Image.open(file)
    width, height = im.size
    if width > height:
        return WIDE_STR
    elif width < height:
        return TALL_STR
    elif width == height:
        return SQUARE_STR
    else:
        return 'error'

def make_folders(parent_dir):
    strings = [WIDE_STR, TALL_STR, SQUARE_STR]
    for string in strings:
        os.makedirs(os.path.join(parent_dir, string), exist_ok=True)


if __name__ == "__main__":
    help_str = 'read the path.'
    parser = argparse.ArgumentParser(description=help_str)
    parser.add_argument('path', help=help_str, default = DEFAULT_DIR)
    args = parser.parse_args()
    pic_dir = args.path
    make_folders(pic_dir)
    sort_images(pic_dir)
    