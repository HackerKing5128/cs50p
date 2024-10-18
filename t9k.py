# WAP to implement T9 Keyboard

dict = {'2':"ABC", '3':"DEF", '4':"GHI", '5':"JKL", 
	'6':"MNO", '7':"PQRS", '8':"TUV", '9':"WXYZ"}
	
num = input("Enter number: ").strip()

if len(num)==1:
	if num in dict:
		print(list(dict[num]))
	else:
		print(list())

else:
	numbers = [key for key in list(num) if key in dict]
	strings = [dict[i] for i in numbers]
	result = [""]
	for string in strings:
		result = [x + y for x in result for y in string]
	print(result)
