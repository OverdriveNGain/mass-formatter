from pathlib import Path
import imageio
import os
import time
from os.path import isfile, join
from apng import APNG

def GetFileList(mypath):
	return [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

def start():
    filename = "exported.apng"
    image_path = Path(os.getcwd() + "\\box")

    images = list(image_path.glob('*.png'))
    _loop = int(input("    Delay (default is 100):"))

    print("Please wait...")

    APNG.from_files(images, delay=_loop).save(filename)

    print("    APNG created!")