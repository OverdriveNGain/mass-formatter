from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd
import math

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return [_HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]]

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]
def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	level = int(input("    Enter lightening level (0-100) (normal is 50):")) / 100
	level = 2*level - 1
	if level >= 0:
		func = lambda x: (1 - level) * (x - 1) + 1
	else:
		func = lambda x: (level + 1) * x
	filenameList = GetFileList(indir)

	iterator = 0
	for inputImage in filenameList:
		iterator += 1
		img = Image.open(indir + inputImage)
		pix = img.load()
		x, y = img.size
		if len(pix[0, 0]) == 4:
			for xi in range(x):
				for yi in range(y):
					pc = pix[xi, yi]
					pix[xi, yi] = (
						pc[0] + math.floor(func(pc[0] / 255) * (255 - pc[0])),
						pc[1] + math.floor(func(pc[1] / 255) * (255 - pc[1])),
						pc[2] + math.floor(func(pc[2] / 255) * (255 - pc[2])),pc[3])
					# if pc[0] == incol[0] and pc[1] == incol[1] and pc[2] == incol[2]:
					# 	pix[xi, yi] = (outputcol[0], outputcol[1], outputcol[2], pc[3])
		else:
			for xi in range(x):
				for yi in range(y):
					pc = pix[xi, yi]
					pix[xi, yi] = (
						pc[0] + math.floor(func(pc[0] / 255) * (255 - pc[0])),
						pc[1] + math.floor(func(pc[1] / 255) * (255 - pc[1])),
						pc[2] + math.floor(func(pc[2] / 255) * (255 - pc[2])))
		print("    ({}/{})".format(iterator, len(filenameList)))
		img.save(outdir + inputImage)
	print("\n    Done!")