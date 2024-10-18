import requests
import sys
if (len(sys.argv)!=2):
	print("Mising command-line argument")
	sys.exit()
elif (type(float(sys.argv[1]))==0):
	print("Command-line argument is not a number")
	sys.exit()
else:
	url="https://api.coindesk.com/v1/bpi/currentprice.json"
	try:
		response=(requests.get(url)).json()
		rate= response["bpi"]["USD"]["rate_float"]
		n=float(sys.argv[1])
		amount = rate*n
		print(f"${amount:,.4f}")
	except requests.RequestException:
		sys.exit()
