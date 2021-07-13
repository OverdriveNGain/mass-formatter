from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd
from os import remove
import time

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return [_HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]]

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]
def Group(blobs, indexStartsAt):
	for i in range(len(blobs)):
		for j in range(len(blobs[i])):
			blobs[i][j] -= indexStartsAt

	components = []
	searched = [False] * len(blobs)
	component = []

	def GetUnusedVertex():
		for i in range(len(searched)):
			if not searched[i]:
				return i
	def GetUnusedConnectedVertex():
		for i in range(len(searched)):
			if (not searched[i]) and (i in component):
				return i

	while True:
		if len(component) == 0: #new component
			v = GetUnusedVertex()
			if v == None:
				break
		else:
			v = GetUnusedConnectedVertex()
			if v == None: #component finished
				components.append(component)
				component = []
				continue
		searched[v] = True
		for i in blobs[v]:
			if i not in component:
				component.append(i)

	for i in range(len(components)):
		for j in range(len(components[i])):
			components[i][j] += indexStartsAt

	return components

def SeperateAndExport(img, filename, autocrop):
	pix = img.load()
	x, y = img.size
	# Opacity Map Creation:
	print("    Creating opacity map...")
	oMap = [0] * (x * y)
	for xi in range(x):
		for yi in range(y):
			if pix[xi, yi][3] != 0:
				oMap[yi * x + xi] = 1
	print("    ...Done!")
	# Horizontal Groupings
	print("    Creating horizontal groupings...")
	groupNumber = 2
	lastState = 0
	for i in range(len(oMap)):
		if oMap[i] == 1:
			oMap[i] = groupNumber
			if (groupNumber == 1803):
				print("({},{})".format(i % x, i // x))
			lastState = 1
		elif oMap[i] == 0 and lastState == 1:
			groupNumber += 1
			lastState = 0
	if lastState == 1:
		groupNumber += 1
	print("    Last group number is " + str(groupNumber))
	print("    ...Done!")
	# Vertical Grouping
	print("    Creating vertical groupings!")
	connections = [set()] * (groupNumber - 2)
	for i in range(len(oMap)):
		if oMap[i] != 0:
			if oMap[i] == 1803:
				print("hello")
				print(oMap[i + x])
			try:
				if oMap[i + x] != 0:
					n1 = oMap[i] - 2
					n2 = oMap[i + x] - 2
					connections[n1] = connections[n1] | {n2 + 2}
					connections[n2] = connections[n2] | {n1 + 2}
			except IndexError:
				break
	print("    ...Done!")
	# Connection Grouping
	print("    Creating blobs...")
	for i in range(len(connections)):
		connections[i] = list(connections[i])
	connections = Group(connections, 2)
	print(connections)
	print("    ...Done! {} shapes detected".format(len(connections)))
	# Group Assignment
	print("    Assigning groups...")
	groupDict = dict()
	groupDict[0] = 0
	if autocrop:
		lefts = [99999] * (len(connections) + 1)
		rights = [-1] * (len(connections) + 1)
		ups = [99999] * (len(connections) + 1)
		downs = [-1] * (len(connections) + 1)
	for i in range(len(connections)):
		for j in range(len(connections[i])):
			groupDict[connections[i][j]] = i + 1
	groupCount = [0] * len(groupDict)
	print(groupDict)
	for xi in range(x):	
		for yi in range(y):
			m = oMap[yi * x + xi]
			v = groupDict[m]
			oMap[yi * x + xi] = v
			if v != 0:
				groupCount[v] += 1
			if autocrop and v != 0:
				if xi > rights[v]:
					rights[v] = xi
				if xi < lefts[v]:
					lefts[v] = xi
				if yi > downs[v]:
					downs[v] = yi
				if yi < ups[v]:
					ups[v] = yi
	print("    ...Done!")
	# Get Most Used Group
	mug = groupCount.index(max(groupCount))
	# Record Original Alphas
	print("    Recording alphas...")
	origAlphas = [0] * len(oMap)
	for xi in range(x):
		for yi in range(y):
			origAlphas[yi * x + xi] = pix[xi,yi][3]
	print("    ...Done!")
	#Selective Export
	print("    Exporting...")
	files = []
	for c in range(len(connections)):
		if c + 1 != mug:
			continue
		if not autocrop:
			for xi in range(x):
				for yi in range(y):
					pixel = pix[xi,yi]
					a = 0
					if oMap[yi * x + xi] == c + 1:
						a = origAlphas[yi * x + xi]
					pix[xi,yi] = (pixel[0], pixel[1], pixel[2], a)
			fileandpath = getcwd() + "\\box\\{}_{}".format(c,filename)
			img.save(fileandpath)
			files.append(fileandpath)
			print("    ...{} exported!".format("{}_{}".format(c,filename)))
		else:
			d = c + 1
			bl = lefts[d]
			br = rights[d] + 1
			bu = ups[d]
			bd = downs[d] + 1
			newimg = Image.new(mode="RGBA", size= (br - bl, bd - bu), color = (0, 0, 0,0))
			newpix = newimg.load()
			nW, nH = newimg.size
			for xi in range(bl, br, 1):
				for yi in range(bu, bd, 1):
					if oMap[yi * x + xi] == d:
						pixel = pix[xi, yi]
						newpix[xi - bl,yi - bu] = (pixel[0], pixel[1], pixel[2], origAlphas[yi * x + xi])
			fileandpath = getcwd() + "\\box\\{}_{}".format(c,filename)
			newimg.save(fileandpath)
			# files.append(fileandpath)
			print("    ...{} exported!".format("{}_{}".format(c,filename)))
def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	filenameList = GetFileList(indir)
	autocrop = input("    Crop automatically? (faster) (y/n):").lower() == "y"
	deleteorig = True
	iterator = 0
	for inputImage in filenameList:
		if inputImage[-3:] != "png":
			continue
		iterator += 1
		img = Image.open(indir + inputImage)
		SeperateAndExport(img, inputImage, autocrop)
		if deleteorig:
			remove(indir + inputImage)
	print("\n    Done!")