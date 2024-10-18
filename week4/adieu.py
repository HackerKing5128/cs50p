import inflect
p=inflect.engine()
Name=[]
while True:
	try:
		n=input("Name: ")
		Name.append(n)
	except EOFError:
		break
names=p.join(Name)
print("\nAdieu, adieu, to "+names)
