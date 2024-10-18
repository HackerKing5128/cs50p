dict={}
while True:
	try:
		item=input().upper()
		if item in dict:
			dict[item] += 1
		else:
			dict[item]=1
	except EOFError:
		break
keys=[]
for i in dict:
	keys.append(i)
keys.sort()
for key in keys:
	print(dict[key]," ",key)
