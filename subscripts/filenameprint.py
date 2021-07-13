from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def start():
	path = getcwd()
	indir = path + "\\box\\"
	filenameList = GetFileList(indir)

	prefix = input("    Enter prefix:")
	suffix = input("    Enter suffix:")

	for file in filenameList:
		print(prefix + file + suffix)
	print("    Done!")