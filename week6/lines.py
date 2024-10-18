import sys
if len(sys.argv)<2:
	print("Too few command-line arguments")
	sys.exit()
elif len(sys.argv)>2:
	print("To many command-line arguments")
	sys.exit()
else:
	if (sys.argv[1]).endswith(".py") is True:
		try:
			file=open(f"{sys.argv[1]}", "r")
			lines=file.readlines()
			count=0
			for line in lines:
				if (line.isspace()==False) and ((line.lstrip()).startswith("#") == False):
					count += 1
			print(count)
		except FileNotFoundError:
			print("File does not exist")
			sys.exit()
	else:
		print("Not a Python file")
		sys.exit()
