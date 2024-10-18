months=["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
	date=input("Date: ")
	if ("/" in date):
		m,d,y=date.split("/")
		m,d,y=int(m),int(d),int(y)
	elif ("," in date):
		m,d,y=date.split()
		y,d = int(y), int(d[:-1])
		m=months.index(m)+1
	else:
		continue
	if (m<=12 and d<=31):
		print(f"Date: {y}-{m:02}-{d:02}")
		break
	else:
		continue
		
