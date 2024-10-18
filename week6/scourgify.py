import sys
import csv

if len(sys.argv)<3:
	print("Too few command-line arguments")
	sys.exit()
elif len(sys.argv)>3:
	print("Too many command-line arguments")
	sys.exit()
else:
	if (sys.argv[1]).endswith(".csv") and (sys.argv[2]).endswith(".csv") :
		newRecords=[["first", "last", "house"]]
		try:
			with open(f"{sys.argv[1]}", "r") as f1:
				data = csv.reader(f1)
				next(data)
				for row in data:
					last, first = row[0].split(", ")
					rec = [first, last, row[1]]
					newRecords.append(rec)
		except FileNotFoundError:
				print(f"Could not read {sys.argv[1]}")
				sys.exit()
		with open(f"{sys.argv[2]}", "w") as f2:
				fobj = csv.writer(f2)
				fobj.writerows(newRecords)
	else:
		print("Not a CSV file")
		sys.exit()
