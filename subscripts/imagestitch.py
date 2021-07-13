import cv2
import numpy as np
import glob
import os

def start():
	output = os.getcwd()+"\\box\\"
	ff = input("    Enter your file name (don't include extension type):")
	ext = input("    Enter your input images' extension (don't include period):")
	fps = int(input("    Enter your fps:"))
	glob__ = glob.glob(output + '*.{}'.format(ext))
	globlen = len(glob__)
	counter = 1

	img = cv2.imread(glob__[0])
	height, width, layers = img.shape
	size = (width,height)
	out = cv2.VideoWriter(output+ ff+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
	print("    Working... (1/100)".format(globlen))


	for i in range(1, globlen):
		filename = glob__[i]
		if counter <=  (i * 100 // globlen):
			print("    Working... ({}/100)".format(counter + 1))
			counter = (i * 100 // globlen) + 1
		out.write(cv2.imread(filename))
	print("    Success!")
	out.release()