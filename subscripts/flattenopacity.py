from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd

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

	th = int(input("    Enter threshold opacity (0-255):"))

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
					pix[xi, yi] = (pc[0], pc[1], pc[2], 0 if pc[3] < th else 255)
		else:
			pass
		print("    ({}/{})".format(iterator, len(filenameList)))
		img.save(outdir + inputImage)
	print("\n    Done!")