while True:
	try:
		a,b=input("Fraction: ").split("/")
		a,b=int(a),int(b)
		if(a>b):
			continue
		out=int((a/b)*100)
		if (out<=1):
			print("E")
		elif (out>=99):
			print("F")
		else:
			print(f"{out}%")
		break
	except(ValueError, ZeroDivisionError):
		continue
