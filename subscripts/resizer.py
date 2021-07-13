from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]
def ResizeViaWidth(img, w):
	return img.resize((int(w), int(w * (img.size[1] / img.size[0]))), Image.ANTIALIAS)
def ResizeViaHeight(img, h):
	return img.resize((int(h * (img.size[0] / img.size[1])), int(h)), Image.ANTIALIAS)
def ResizeViaWidthAndHeight(img, h, w):
	return img.resize((w,h), Image.ANTIALIAS)
def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	print('    LAR is - locked aspect ratio')

	print("    Enter input mode:")
	print("    1 - Scale all by a factor (LAR)")
	print("    2 - Scale to a certain width (LAR)")
	print("    3 - Scale to a certain height (LAR)")
	print("    4 - Scale according to the kodigo file (LAR)")
	print("    5 - Scale according to the kodigo file (LAR) (INCHES)")
	print("    6 - Scale by width and height")
	inputMode = input("\n    :")

	filenameList = GetFileList(indir)

	if inputMode == "1":
		inputScale = float(input("\n    Enter scaling factor:"))
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			img = img.resize((int(img.size[0] * inputScale), int(img.size[1] * inputScale)), Image.ANTIALIAS)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage) 
	elif inputMode == "2":
		setWidth = float(input("\n    Enter set width:"))
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			img = ResizeViaWidth(img, setWidth)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage)
	elif inputMode == "3":
		setHeight = float(input("\n    Enter set height:"))
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			img = ResizeViaHeight(img, setHeight)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage)
	elif inputMode == "4":
		kodigo = open("kodigo.txt", "r")
		kodigo = [line for line in kodigo.readlines()]
		for i in range(len(kodigo)):
			j = kodigo[i].split()
			kodigo[i] = (j[0], j[1])
		dictt = dict(kodigo)
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			v = dictt[inputImage]
			k = v[0]
			n = int(v[1:])
			if k == "h":
				img = ResizeViaHeight(img, n)
			elif k == "w":
				img = ResizeViaWidth(img, ns)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage)
	elif inputMode == "5":
		ppi = int(input("\n    Enter ppi (pixels per inch):"))
		kodigo = open("kodigo.txt", "r")
		kodigo = [line for line in kodigo.readlines()]
		for i in range(len(kodigo)):
			j = kodigo[i].split()
			kodigo[i] = (j[0], j[1])
		dictt = dict(kodigo)
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			v = dictt[inputImage]
			k = v[0]
			n = int(float(v[1:]) * ppi)
			if k == "h":
				img = ResizeViaHeight(img, n)
			elif k == "w":
				img = ResizeViaWidth(img, n)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage)
	elif inputMode == "6":
		setHeight = int(input("\n    Enter set height:"))
		setWidth = int(input("\n    Enter set width:"))
		iterator = 0
		for inputImage in filenameList:
			iterator += 1
			img = Image.open(indir + inputImage)
			img = ResizeViaWidthAndHeight(img, setWidth,setHeight)
			print("    ({}/{}).".format(iterator, len(filenameList)))
			img.save(outdir + inputImage)
	print("\n    Done!")