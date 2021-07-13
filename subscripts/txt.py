def start():
	validCommands = ["removeduplicates", "sort","enumerate", "changecase"]
	while True:
		print("    Text Format Mode")
		newCommand = input("    Listening:")
		if newCommand == "quit":
			break

		if newCommand == "removeduplicates":
			removeduplicates()
		elif newCommand == "sort":
			textsort()
		elif newCommand == "enumerate":
			enumerate()
		elif newCommand == "changecase":
			changecase()
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
def changecase():
	def uCamelCase(_s):
		s = _s
		s = s.lower()
		s = list(s)
		if len(s) == 0:
			return ""
		if len(s) == 1:
			s = s.upper()
		else:
			if 'a' <= s[0] <= 'z':
				s[0] = s[0].upper()
			for i in range(len(_s) - 1):
				if s[i] == " " and ('a'<= s[i+1] <= 'z'):
					s[i+1] = s[i+1].upper()
		return "".join(s)
	def lCamelCase(_s):
		s = _s
		s = s.lower()
		s = list(s)
		counter = 0
		if len(s) == 0:
			return ""
		if len(s) == 1:
			s = s.lower()
		else:
			if 'a' <= s[0] <= 'z':
				counter += 1
			for i in range(len(s) - 1):
				if s[i] == ' ' and ('a'<= s[i+1] <= 'z'):
					if counter > 0:
						print(f"at {i+1}")
						s[i+1] = s[i+1].upper()
					else:
						counter += 1
		return "".join(s)


	while True:
		print("        Enter case format:")
		print("            0 - Upper Case")
		print("            1 - Lower Case")
		print("            2 - Upper Camel Case")
		print("            3 - Lower Camel Case")
		print("            4 - Snake Case")
		print("            5 - Snake Case to Lower Case")
		print("           -1 - Exit")
		numberFormat = int(input("        format:"))

		if (numberFormat == -1):
			return
		elif (0 <= numberFormat <= 3):
			f = open("box.txt", "r")
			l = f.read().split("\n")
			f.close()

			for li in range(len(l)):
				if numberFormat == 0:
					l[li] = l[li].upper()
				elif numberFormat == 1:
					l[li] = l[li].lower()
				if numberFormat == 2:
					l[li] = uCamelCase(l[li])
				elif numberFormat == 3:
					l[li] = lCamelCase(l[li])
				elif numberFormat == 4:
					l[li] = l[li].lower().replace(' ', '_')
				elif numberFormat == 5:
					l[li] = l[li].lower().replace('_', ' ')
			break
	
	f2 = open("box.txt", "w")
	f2.writelines("\n".join(l))
	f2.close()
	print("        Success!")