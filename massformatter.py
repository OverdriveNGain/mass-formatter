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

validCommands = ["replacecolor", "autocrop", "resizer", "pdf2img", "img2pdf","gifmaker",
 "boxbackup", "boxrestore","separator","outliner","divider","masscrop","massrenamer","lighten",
 "flattenopacity", "retainmain", "timelapse","imagestitch", "boxclear","txt","pixels","filenameprint","help","jpgcompress", "pdfstitch"]
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
while True:
	newCommand = input("Listening:")
	if newCommand == "quit":
		break

	if newCommand == "replacecolor":
		replacecolor.start()
	elif newCommand == "autocrop":
		autocrop.start()
	elif newCommand == "resizer":
		resizer.start()
	elif newCommand == "pdf2img":
		pdf2img.pdf2img()
	elif newCommand == "img2pdf":
		pdf2img.img2pdf()
	elif newCommand == "gifmaker":
		gifmaker.start()
	elif newCommand == "boxbackup":
		boxbackup.backup()
	elif newCommand == "boxrestore":
		boxbackup.restore()
	elif newCommand == "separator":
		separator.start()
	elif newCommand == "outliner":
		outliner.start()
	elif newCommand == "divider" :
		divider.start()
	elif newCommand == "masscrop" :
		masscrop.start()
	elif newCommand == "massrenamer" :
		massrenamer.start()
	elif newCommand == "lighten":
		lighten.start()
	elif newCommand == "flattenopacity":
		flattenopacity.start()
	elif newCommand == "retainmain":
		retainmain.start()
	elif newCommand == "timelapse":
		timelapse.start()
	elif newCommand == "imagestitch":
		imagestitch.start()
	elif newCommand == "boxclear":
		boxbackup.clear()
	elif newCommand == "txt":
		txt.start()
	elif newCommand == "pixels":
		pixels.start()
	elif newCommand == "filenameprint":
		filenameprint.start()
	elif newCommand == 'jpgcompress':
		jpgcompress.start()
	elif newCommand == 'pdfstitch':
		pdf2img.pdfstitch()
	elif newCommand == "help":
		print("    The valid commands are:")
		for c in validCommands:
			print("    - " + c)
	else:
		print("Invalid command. Enter \'help\' for a list of valid commands")