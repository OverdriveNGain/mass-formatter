from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd
from os import remove

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	filenameList = GetFileList(indir)
	_quality = int(input('Quality? (1 - 100):'))
	iterator = 1
	for inputImage in filenameList:
		img = Image.open(indir + inputImage)
		img = img.convert('RGB')

		remove(indir + inputImage)

		img.save(outdir + inputImage[:inputImage.index('.')] + '.jpg', quality = _quality)	
		print("    ({}/{})".format(iterator, len(filenameList)))
		iterator += 1
	print("\n    Done!")