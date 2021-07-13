import os, shutil

def backup():
	clearfolder(os.getcwd()+"\\backup")
	copytree(os.getcwd()+"\\box\\",os.getcwd()+"\\backup\\")
	print("    Backup created!")
def restore():
	clearfolder(os.getcwd()+"\\box")
	copytree(os.getcwd()+"\\backup\\",os.getcwd()+"\\box\\")
	print("    Backup restored!")
def clear():
	clearfolder(os.getcwd()+"\\box")
	print("    Box cleared!")
def clearfolder(src):
	for item in os.listdir(src):
		os.remove(src + "\\" + item)
def copytree(src, dst, symlinks=False, ignore=None):
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isdir(s):
			shutil.copytree(s, d, symlinks, ignore)
		else:
			shutil.copy2(s, d)