vowels=["A","a","E","e","I","i","O","o","U","u"]
txt=input("Input: ")
print("Output: ",end="")
for i in txt:
	if i not in vowels:
		print(i ,end="")
print()
