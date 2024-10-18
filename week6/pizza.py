import csv
import sys
from tabulate import tabulate

if len(sys.argv)<2:
	print("Too few command-line arguments")
	sys.exit()
elif len(sys.argv)>2:
	print("Too many command-line arguments")
	sys.exit()
else:
	if (sys.argv[1]).endswith(".csv"):
		try:
			file=open(f"{sys.argv[1]}", "r")
			lines = []
			CsvRead = csv.reader(file)
			for row in CsvRead:
				lines.append(row)
			print(tabulate(lines, headers="firstrow", tablefmt="grid"))
		except FileNotFoundError:
			print("File does not exist")
			sys.exit()
	else:
		print("Not a CSV file")
		sys.exit()
