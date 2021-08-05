from PIL import Image, UnidentifiedImageError
import os, sys


def set_quality():
    f = os.getcwd()
    for file in os.listdir(f):
        try:
            f_img = f+"/"+file
            img=Image.open(f_img)
            img.save(f_img,quality = 20)
        except UnidentifiedImageError as e:
            sys.stdout.write("Not an image, skipping.\n")

if __name__ == "__main__":
    set_quality()
