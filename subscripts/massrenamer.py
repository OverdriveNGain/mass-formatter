from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd
import os

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	filenameList = GetFileList(indir)

	mode = 0
	while True:
		print("    Choose rename mode:")
		print("        1 - File name with counter")
		print("        2 - First occurence replace")
		mode = int(input("    Mode: "))
		if 1 <= mode <= 2:
			break
	if mode == 1:
		print("    For the new file name:")
		print("        - Put a single # in the file name to represent the numbers")
		print("        - Include the file type and period")
		fn = input("    Enter new file name:")
		print("    Counter starts at what number?")
		iteratorStart = int(input("    Enter number:"))

		iterator = iteratorStart
		zeroCount = len(str(len(filenameList) - 1))
		for inputImage in filenameList:
			newName = fn.replace("#", "{}".format(("{:0" + "{}".format(zeroCount) +"d}").format(iterator)))
			os.rename(indir+inputImage, outdir+ newName)
			iterator += 1
	elif mode == 2:
		searched = input("    Enter search string:")
		replaced = input("    Enter replaced string:")
		for inputImage in filenameList:
			if searched in inputImage:
				newName = inputImage.replace(searched, replaced)
				os.rename(indir+inputImage, outdir+ newName)
	print("\n    Done!")