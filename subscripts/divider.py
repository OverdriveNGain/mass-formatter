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
	print("    Modes:")
	print("        1 - Divide by cell count")
	print("        2 - Divide by cell size")
	mode = int(input("    Enter divider mode:"))
	if (mode == 1):
		cols = int(input("    Enter column count:"))
		rows = int(input("    Enter rows count:"))
	else:
		cWidth = int(input("    Enter cell width:"))
		cHeight = int(input("    Enter cell height:"))

	filenameList = GetFileList(indir)

	iterator = 0
	for inputImage in filenameList:
		img = Image.open(indir + inputImage)
		pix = img.load()
		w, h = img.size

		if mode == 1:
			iterator = 0
			for yi in range(rows):
				for xi in range(cols):
					leftX = round(w * (float(xi) / cols))
					rightX = round(w * (float(xi + 1) / cols))
					upY = round(h * (float(yi) / rows))
					downY = round(h * (float(yi + 1) / rows))
					sz = (rightX - leftX, downY - upY)
					temp = Image.new(mode = ("RGBA" if len(pix[0,0]) == 4 else "RGB"), size = sz,color = (0, 0, 0, 0))
					tempix = temp.load()
					for xii in range(leftX, rightX, 1):
						for yii in range(upY, downY, 1):
							tempix[xii - leftX, yii - upY] = pix[xii, yii]
					print("    {}_{} exported!".format(iterator,inputImage))
					temp.save(outdir + "{}_{}".format(iterator,inputImage))
					iterator += 1

		else:
			print("    Divide by cell size mode not yet implemented.")

		# iterator += 1
		# img = Image.open(indir + inputImage)
		# pix = img.load()
		# x, y = img.size
		# for xi in range(x):
		# 	for yi in range(y):
		# 		if pix[xi, yi][3] != 0:
		# 			if topmost > yi:
		# 				topmost = yi
		# 			if xi < leftmost:
		# 				leftmost = xi
		# 			if xi > rightmost:
		# 				rightmost = xi
		# 			if bottommost < yi:
		# 				bottommost = yi

		# img = img.crop((leftmost, topmost, rightmost, bottommost))
		# print("({}/{}).".format(iterator, len(filenameList)), end = "")
		# img.save(outdir + inputImage)
	print("\n    Done!")