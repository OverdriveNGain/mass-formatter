from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	filenameList = GetFileList(indir)

	topmost = int(input("Top crop:"))
	leftmost = int(input("Left crop:"))
	rightmost = int(input("Right crop:"))
	bottommost = int(input("Bottom crop:"))

	iterator = 1
	for inputImage in filenameList:
		img = Image.open(indir + inputImage)
		w,h = img.size
		img = img.crop((leftmost, topmost, w - rightmost, h -bottommost))
					
		print("({}/{}).".format(iterator, len(filenameList)))
		img.save(outdir + inputImage)
		iterator += 1
	print("\n    Done!")