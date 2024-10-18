def main():
	plate=input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")

def is_valid(s):
	c1=(2 <= len(s) <= 6)
	c2=s.isalpha()
	c3=s.isalnum()
	c4=s[:1].isalpha()
	if c1 and c2 and c4:
		return True
	elif c1 and c3 and c4 and chk_num(s):
		return True
	else:
		return False

def chk_num(s):
	for i in range(len(s)):
		if s[i].isdigit():
			if s[i:].isdigit():
				if s[i] == "0" or s[-2].isalpha():
					return False
				else:
					return True
	return False			
				
main()
