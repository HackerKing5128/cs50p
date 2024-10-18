import csv
import sys
with open(f"{sys.argv[1]}", "r") as f1:
				data = csv.reader(f1)
				for row in data:
					print(row[0])
