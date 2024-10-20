#working 9 to 5 (working.py)

import re

def main():
	print(convert(input("Hours: ")))

def convert(s):
	pattern= r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
	time = re.search(pattern, s, re.IGNORECASE)
	if time:
		#ValueErrors
		if time.group(2):
			if int(time.group(2)) >= 60:
				raise ValueError
		if time.group(5):
			if int(time.group(5)) >= 60:
				raise ValueError

		#Time1
		hour1 = int(time.group(1))
		if time.group(3)=="PM" and hour1!=12:
			hour1 += 12
		elif time.group(3)=="AM" and hour1==12:
			hour1 -= 12
		if time.group(2) == None:
			time1 = f"{hour1:02}:00"
		else:
			time1 = f"{hour1:02}:{time.group(2)}"

		#Time2
		hour2 = int(time.group(4))
		if time.group(6)=="PM" and hour2!=12:
			hour2 += 12
		elif time.group(6)=="AM" and hour2==12:
			hour2 -= 12
		if time.group(5) == None:
			time2 = f"{hour2:02}:00"
		else:
			time2 = f"{hour2:02}:{time.group(5)}"

		#return 24hr  time 
		return f"{time1} to {time2}"
	else:
		raise ValueError


if __name__ == "__main__":
	main()
