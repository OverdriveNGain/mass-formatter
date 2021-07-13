from PIL import Image
from os import listdir
from os.path import isfile, join
from os import getcwd

def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]
def GetBrush(level):
	indir = getcwd() + "\\brushes\\"
	return Image.open(indir + "{}_brush.png".format(level - 1))
def ExpandImage(img, sideincrease):
	w, h = img.size[0], img.size[1]
	temp = Image.new(mode="RGBA", size=(round(w + sideincrease * 2), round(h + sideincrease * 2)), color = (0, 0, 0, 0))
	temp.paste(img, (round(sideincrease), round(sideincrease)))
	return temp
def BrushTrace(em, brush):
	x, y = em.size
	empix = em.load()
	temp = Image.new(mode="RGBA", size=em.size, color = (0, 0, 0, 0))
	for xi in range(x):
		for yi in range(y):
			if empix[xi, yi][0] == 0:
				ac = Image.new(mode="RGBA", size=em.size, color = (0, 0, 0, 0))
				ac.paste(brush, (xi, yi), brush)
				temp = Image.alpha_composite(brush, temp)
	return temp
def GetEdgeMap(img):
	pix = img.load()
	x, y = img.size
	temp = Image.new(mode="RGB", size=(x, y), color = (255, 255, 255, 255))
	temppix = temp.load()
	for xi in range(x):
		for yi in range(y):
			up = False
			down = False
			left = False
			right = False
			try:
				if pix[xi, yi - 1][3] != 0:
					up = True
			except IndexError:
				pass
			try:
				if pix[xi, yi + 1][3] != 0:
					down = True
			except IndexError:
				pass
			try:
				if pix[xi - 1, yi][3] != 0:
					left = True
			except IndexError:
				pass
			try:
				if pix[xi + 1, yi][3] != 0:
					right = True
			except IndexError:
				pass
			if not (up == down == left == right):
				temppix[xi, yi]= (0, 0, 0, 255)
	return temp



def start():
	path = getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"

	filenameList = GetFileList(indir)

	level = int(input("    Level of outline (1 - 20):"))
	brush = GetBrush(level)
	brushd = brush.size[0]

	for inputImage in filenameList:
		img = Image.open(indir + inputImage)
		pix = img.load()
		x, y = img.size

		expanded = ExpandImage(img, brushd / 2)
		edgemap = GetEdgeMap(expanded)
		brushtrace = BrushTrace(edgemap, brush)
		# final = Combine(brushtrace, expanded)

		# for xi in range(x):
		# 	for yi in range(y):
		# img = img.crop((leftmost, topmost, rightmost, bottommost))
					
		brushtrace.save(outdir + "___" + inputImage)
	print("\n    Done!")
