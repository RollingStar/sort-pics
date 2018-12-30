import os
from PIL import Image
from shutil import move

WIDE_STR = 'wide'
TALL_STR = 'tall'
SQUARE_STR = 'square'
PIC_DIR = r'C:\PATH_HERE'

def sort_images(folder):
    folder = os.fsencode(folder)
    for leaf in os.scandir(folder):
        if leaf.is_file():
            aspect = get_aspect(leaf.path)
            new_path = os.path.join(os.fsdecode(folder), aspect, os.fsdecode(leaf.name))
            print(new_path)
            move(leaf.path, new_path)

def get_aspect(file):
    im = Image.open(file)
    width, height = im.size
    if width > height:
        return WIDE_STR
    elif width < height:
        return TALL_STR
    elif width == height:
        return 'square'
    else:
        return 'error'

def make_folders(parent_dir):
    #not making three if/else statements for this
    try:
        os.mkdir(os.path.join(parent_dir, WIDE_STR))
        os.mkdir(os.path.join(parent_dir, TALL_STR))
        os.mkdir(os.path.join(parent_dir, SQUARE_STR))
    except:
        pass

def main():
    make_folders(PIC_DIR)
    sort_images(PIC_DIR)

if __name__ == "__main__":
    main()
