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
from subscripts import pixels
from subscripts import filenameprint
from subscripts import jpgcompress

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