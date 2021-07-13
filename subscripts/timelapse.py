from PIL import Image, ImageGrab 
import time
import os
import math

def start():
	delay = float(input("    Enter your screenshot delay in seconds:"))
	print("    For the new file name:")
	print("        - Put a single # in the file name to represent the numbers")
	print("        - Don't include the file type")
	print("        - Don't include the period")
	fn = input("    Enter new file name:")

	timestart = time.time() 
	timetotal = 0
	timemark = time.time()

	counter = 0

	output = os.getcwd()+"\\box\\"

	runningname = os.getcwd() + "\\RUNNING.txt"
	CreateRunningFile(runningname)
	while(True):
		b = ImageGrab.grab()

		newName = fn.replace("#", "{}".format(("{:0" + "{}".format(6) +"d}").format(counter)))
		b.save(output + newName +".png")

		counter += 1
		time.sleep(delay)
		# print("    " + SecsFormat(time.time() - timemark) + " : timelapse : " + str(counter))
		print("    Total:{} | Elapsed:{} | Frame:{}".format(SecsFormat(time.time() - timestart), SecsFormat(timetotal + time.time() - timemark), counter))

		if (not os.path.isfile(runningname)):
			timetotal += time.time() - timemark
			input("\n    Paused. Press Enter to continue.\n") 
			timemark = time.time()
			CreateRunningFile(runningname)

def SecsFormat(secs):
	secsfloor = math.floor(secs)
	hh = secsfloor // 3600
	hh = str(hh) if hh > 9 else ("0" + str(hh))
	mm = (secsfloor % 3600) // 60
	mm = str(mm) if mm > 9 else ("0" + str(mm))
	ss = secsfloor % 60
	ss = str(ss) if ss >= 10 else ("0" + str(ss))
	return ("{}:{}:{}".format(hh, mm, ss))

def CreateRunningFile(path_fn):
	file = open(path_fn, "w") 
	file.write("RUNNING") 
	file.close() 