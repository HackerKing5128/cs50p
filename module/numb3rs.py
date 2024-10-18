#numb3rs.py    validate IPv4 Address


def validate(ip):
	"""Validate the IPv4 Address  """
	try:
		numbers = ip.split(".")
	except error as e:
		return False
	flag = True			#assume output is True
	if len(numbers) != 4:
		return False
	else:
		for num in numbers:
			if int(num) not in range(256):
				flag = False
		return flag


