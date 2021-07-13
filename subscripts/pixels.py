def start():
	validCommands = ["removeduplicates", "sort","enumerate"]
	while True:
		newCommand = input("    Text Format Mode. Listening:")
		if newCommand == "quit":
			break

		if newCommand == "removeduplicates":
			removeduplicates()
		elif newCommand == "sort":
			textsort()
		elif newCommand == "enumerate":
			enumerate()
		elif newCommand == "help":
			print("    The valid commands are:")
			for c in validCommands:
				print("        - " + c)
		else:
			print("    Invalid command. Enter \'help\' for a list of valid commands")

def removeduplicates():
	f = open("box.txt", "r")
	l = f.read().split("\n")
	f.close()

	l = list(set(l))

	f2 = open("box.txt", "w")
	f2.writelines("\n".join(l))
	f2.close()
	print("        Success!")
def textsort():
	f = open("box.txt", "r")
	l = f.read().split("\n")
	f.close()

	l.sort()
	
	f2 = open("box.txt", "w")
	f2.writelines("\n".join(l))
	f2.close()
	print("        Success!")
def enumerate():
	f = open("box.txt", "r")
	l = f.read().split("\n")
	f.close()

	counter = 1
	numberFormat = input("        Enter enumeration format (include # for number):")
	for li in range(len(l)):
		l[li] = numberFormat.replace("#", str(counter))+ l[li]
		counter += 1
	
	f2 = open("box.txt", "w")
	f2.writelines("\n".join(l))
	f2.close()
	print("        Success!")