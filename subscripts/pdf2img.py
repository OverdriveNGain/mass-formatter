import fitz
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
import time
import math
from PyPDF2 import PdfFileMerger, PdfFileReader
import os

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return [_HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]]
def GetFileList(mypath):
	return [f for f in listdir(mypath) if isfile(join(mypath, f))]
def GetPdfList(mypath):
	return [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f[-3:] == "pdf")]
def img2pdf():
	path = os.getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"
	subPdfCount = int(input("    Enter sub PDF count (-1 for none):"))
	if subPdfCount == -1:
		fileList = [Image.open(indir + i).convert('RGB') for i in GetFileList(indir)]
		fileList[0].save(outdir + "pdfExported.pdf", save_all = True, append_images = fileList[1:])
		print ("    Exported pdfExported.pdf!")
	else:
		pdfList = []
		fileList = GetFileList(indir)
		print("    Generating sub PDF files...")
		for i in range(math.ceil(len(fileList) / float(subPdfCount))):
			images = [None for i in range(subPdfCount)]
			for j in range(subPdfCount):
				try:
					images[j] = Image.open(indir + fileList[i * subPdfCount + j]).convert('RGB')
				except IndexError:
					break
			newName = "#_pdfExported.pdf".replace("#", "{}".format(("{:0" + "{}".format("5") +"d}").format(i)))
			pdfList.append(newName)
			images[0].save(outdir+ newName, save_all = True, append_images = [k for k in images[1:] if k != None])
		print("    Merging sub PDF files...")
		mergedObject = PdfFileMerger()
		for fileName in pdfList:
			mergedObject.append(PdfFileReader(outdir+fileName, 'rb'))
		mergedObject.write(outdir + "pdfExported.pdf")
		print("    Deleting temporary sub PDF files...")
		for fileName in pdfList:
			os.remove(outdir + fileName)
		print ("    Exported pdfExported.pdf!")

def pdf2img():
	path = os.getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"
	filenameList = GetFileList(indir)

	isTemplate = input("    Convert to silhouette template?(y/n):").lower() == "y"
	if isTemplate:
		templateCol = rgb(input("    Enter template hex color value:"))
	zoom = int(input("    Enter resolution (default is 5; the higher, the clearer):"))

	for file in filenameList:
		if file[-4:] != ".pdf":
			continue

		fullPath = indir + file

		doc = fitz.open(fullPath)
		pageI = 0
		percentage = -1
		print("    " + file)
		while True:
			try:
				page = doc.loadPage(pageI)
			except ValueError:
				break

			mat = fitz.Matrix(zoom,zoom)
			pix = page.getPixmap(matrix = mat)

			if isTemplate:
				for x in range(0, pix.width, 1):
					newP = round(x * 100 / pix.width)
					if newP != percentage:
						percentage = newP

					for y in range(0, pix.height, 1):
						if pix.pixel(x,y) == templateCol:
							pix.setPixel(x, y,(255, 255, 255))
						else:
							pix.setPixel(x, y,(0, 0, 0))

			pageI += 1
			pix.writePNG(outdir + "{}_{}.{}".format(str(pageI).zfill(5),file[-3:],"png"))
			print("    Page {}".format(pageI - 1))
	print ("    Done")

def pdfstitch():
	path = os.getcwd()
	indir = path + "\\box\\"
	outdir = path + "\\box\\"
	pdfList = GetFileList(indir)
	pdfList.sort()
	print("    Merging sub PDF files...")
	mergedObject = PdfFileMerger()
	for fileName in pdfList:
		mergedObject.append(PdfFileReader(outdir+fileName, 'rb'))
	mergedObject.write(outdir + "pdfExported.pdf")
	print ("    Exported pdfExported.pdf!")