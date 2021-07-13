from pathlib import Path
# from pygifsicle import optimize
import imageio
import os
import time
from os.path import isfile, join

#https://medium.com/swlh/python-animated-images-6a85b9b68f86
def GetFileList(mypath):
	return [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

def start():
	filename = "exported.gif"
	image_path = Path(os.getcwd() + "\\box")

	images = list(image_path.glob('*.png'))
	image_list = []
	for fn in images:
	    image_list.append(imageio.imread(fn))

	_loop = int(input("    Loop count (0 for infinite):"))
	_fps = int(input("    Fps (default is 10):"))

	for i in GetFileList(os.getcwd() + "\\box"):
		if i[-3:] == "png":
			os.remove(os.getcwd() + "\\box" + "\\" + i)
		print("    Adding frame {}".format(i))

	imageio.mimwrite(str(image_path) + "\\" + filename, image_list, loop= _loop, fps= _fps)
	print("    GIF created! Optimize at this url:{}".format("https://ezgif.com/optimize"))

# time.sleep(5)

# create a new one
# newP = os.getcwd() + "\\" + filename
# print(newP)
# optimize(newP)

# print("GIF success!")
# input()