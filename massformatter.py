import sys
import os
pathname = os.path.dirname(sys.argv[0]).replace('\\','/')
sys.path.append(pathname + '/subscripts')

import replacecolor
import autocrop
import resizer
import pdf2img
import gifmaker
import boxbackup
import separator
import divider
import outliner
import masscrop
import massrenamer
import lighten
import flattenopacity
import retainmain
import timelapse
import imagestitch
import txt
import pixels
import filenameprint
import jpgcompress

# validCommands = ["replacecolor", "autocrop", "resizer", "pdf2img", "img2pdf","gifmaker",
#  "boxbackup", "boxrestore","separator","outliner","divider","masscrop","massrenamer","lighten",
#  "flattenopacity", "retainmain", "timelapse","imagestitch", "boxclear","txt","pixels","filenameprint","help","jpgcompress", "pdfstitch"]
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
	"replacecolor": lambda : replacecolor.start(),
	"autocrop": lambda : autocrop.start(),
	"resizer": lambda : resizer.start(),
	"pdf2img": lambda : pdf2img.pdf2img(),
	"img2pdf": lambda : pdf2img.img2pdf(),
	"gifmaker": lambda : gifmaker.start(),
	"boxbackup": lambda : boxbackup.backup(),
	"boxrestore": lambda : boxbackup.restore(),
	"separator": lambda : separator.start(),
	"outliner": lambda : outliner.start(),
	"divider": lambda : divider.start(),
	"masscrop": lambda : masscrop.start(),
	"massrenamer": lambda : massrenamer.start(),
	"lighten": lambda : lighten.start(),
	"flattenopacity": lambda : flattenopacity.start(),
	"retainmain": lambda : retainmain.start(),
	"timelapse": lambda : timelapse.start(),
	"imagestitch": lambda : imagestitch.start(),
	"boxclear": lambda : boxbackup.clear(),
	"txt": lambda : txt.start(),
	"pixels": lambda : pixels.start(),
	"filenameprint": lambda : filenameprint.start(),
	"jpgcompress": lambda : jpgcompress.start(),
	"pdfstitch": lambda : pdf2img.pdfstitch(),
	"help": lambda : helpAction(commandMap),

}

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