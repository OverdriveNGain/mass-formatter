from subscripts import replacecolor
from subscripts import autocrop
from subscripts import resizer
from subscripts import pdf2img
from subscripts import gifmaker
from subscripts import boxbackup
from subscripts import separator
from subscripts import divider
from subscripts import outliner
from subscripts import masscrop
from subscripts import massrenamer
from subscripts import lighten
from subscripts import flattenopacity
from subscripts import retainmain
from subscripts import timelapse
from subscripts import imagestitch
from subscripts import txt
from subscripts import filenameprint
from subscripts import jpgcompress

print('''
  ███    ███  █████  ███████ ███████
  ████  ████ ██   ██ ██      ██     
  ██ ████ ██ ███████ ███████ ███████
  ██  ██  ██ ██   ██      ██      ██
  ██      ██ ██   ██ ███████ ███████ by Jeremy Amon

  ███████  ██████  ██████  ███    ███  █████  ████████ ████████ ███████ ██████  
  ██      ██    ██ ██   ██ ████  ████ ██   ██    ██       ██    ██      ██   ██ 
  █████   ██    ██ ██████  ██ ████ ██ ███████    ██       ██    █████   ██████  
  ██      ██    ██ ██   ██ ██  ██  ██ ██   ██    ██       ██    ██      ██   ██ 
  ██       ██████  ██   ██ ██      ██ ██   ██    ██       ██    ███████ ██   ██ 
''')

commandMap = {
	"replacecolor": 
		{
			"execute": lambda : replacecolor.start(),
			"desciption": "Replaces all occurances of a certin color within an image by another color.",
		},
	"autocrop": 
		{
			"execute": lambda : autocrop.start(),
			"desciption": "Automatically removes transparent margins around opaque blobs in a png image through cropping.",
		},
	"resizer": 
		{
			"execute": lambda : resizer.start(),
			"desciption": "Resizes multiple images in bulk.",
		},
	"pdf2img": 
		{
			"execute": lambda : pdf2img.pdf2img(),
			"desciption": "Creates image files from the pages of a PDF file.",
		},
	"img2pdf": 
		{
			"execute": lambda : pdf2img.img2pdf(),
			"desciption": "Creates a pdf file from multiple image files.",
		},
	"gifmaker": 
		{
			"execute": lambda : gifmaker.start(),
			"desciption": "Creates a gif image from multiple image files.",
		},
	"boxbackup": 
		{
			"execute": lambda : boxbackup.backup(),
			"desciption": "Performs a backup on the files currently in the box folder",
		},
	"boxrestore": 
		{
			"execute": lambda : boxbackup.restore(),
			"desciption": "Restores the box folder with a previous box backup.",
		},
	"separator": 
		{
			"execute": lambda : separator.start(),
			"desciption": "Seperates multiple opaque blobs that exists within a single image into multiple images.",
		},
	"outliner": 
		{
			"execute": lambda : outliner.start(),
			"desciption": "",
		},
	"divider": 
		{
			"execute": lambda : divider.start(),
			"desciption": "Slices an image into several smaller images.",
		},
	"masscrop": 
		{
			"execute": lambda : masscrop.start(),
			"desciption": "Crops all images by certain crop values.",
		},
	"massrenamer": 
		{
			"execute": lambda : massrenamer.start(),
			"desciption": "Renames files by a set filename and a set iteration value.",
		},
	"lighten": 
		{
			"execute": lambda : lighten.start(),
			"desciption": "Simple lightening of image using linear interpolation of RGB values.",
		},
	"flattenopacity": 
		{
			"execute": lambda : flattenopacity.start(),
			"desciption": "Manipulates the alpha values of each pixel of an image by assigning either a value of 0 or a value of 255, depending on a certain threshold.",
		},
	"retainmain": 
		{
			"execute": lambda : retainmain.start(),
			"desciption": "Isolates the biggest non-opaque blob of pixels from other blobs within the same image.",
		},
	"timelapse": 
		{
			"execute": lambda : timelapse.start(),
			"desciption": "Takes screenshots of your computer screen with a set periodic time.",
		},
	"imagestitch": 
		{
			"execute": lambda : imagestitch.start(),
			"desciption": "Creates an .avi video file from a multiple images.",
		},
	"boxclear": 
		{
			"execute": lambda : boxbackup.clear(),
			"desciption": "Clears box folder.",
		},
	"txt": 
		{
			"execute": lambda : txt.start(),
			"desciption": "Provides functions for bulk manipulation of text.",
		},
	"filenameprint": 
		{
			"execute": lambda : filenameprint.start(),
			"desciption": "Lists out file names with optional prefix and suffix strings.",
		},
	"jpgcompress": 
		{
			"execute": lambda : jpgcompress.start(),
			"desciption": "Compresses image files into jpg files with variable quality.",
		},
	"pdfstitch": 
		{
			"execute": lambda : pdf2img.pdfstitch(),
			"desciption": "",
		},
	"help": 
		{
			"execute": lambda : helpAction(commandMap),
			"desciption": "Lists out the available commands.",
		},
}
print("Version 1.0. Type 'help' for available commands")
def helpAction(commandMap):
	print("    The valid commands are:")
	for c in commandMap:
		print("    - " + c)

while True:
	newCommand = input("\nListening:")
	
	if newCommand == "quit":
		break

	try:
		commandMap[newCommand]()
	except KeyError:
		print("Invalid command. Enter \'help\' for a list of valid commands")