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

	iterator = 0
	for inputImage in filenameList:
		topmost = 99999
		leftmost = 99999
		rightmost = 0
		bottommost = 0

		iterator += 1
		img = Image.open(indir + inputImage)
		pix = img.load()
		x, y = img.size
		if len(pix[0, 0]) == 4:
			for xi in range(x):
				for yi in range(y):
					if pix[xi, yi][3] != 0:
						if topmost > yi:
							topmost = yi
						if xi < leftmost:
							leftmost = xi
						if xi > rightmost:
							rightmost = xi
						if bottommost < yi:
							bottommost = yi
			img = img.crop((leftmost, topmost, rightmost, bottommost))
			img.save(outdir + inputImage)
					
		print("    ({}/{})".format(iterator, len(filenameList)))
	print("\n    Done!")