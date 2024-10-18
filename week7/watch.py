import re

def main():
	print(parse(input("HTML: ")))

def parse(s):
	if "youtube.com" in s:
		pattern= r'src="[^"]*/([^"]+)"'
		result=re.search(pattern, s)
		if result is None:
			return None
		else:
			out = "https://youtu.be/" + result[1]
			return out
	else:
		return None

if __name__ == "__main__" :
	main()
