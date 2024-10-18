x=input("Enter: ")
if x.islower():
	print(x)
else:
	for i in x:
		if i.islower():
			print(i,end="")
		else:
			print("_"+i.lower(),end="")
	print()
