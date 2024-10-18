amt=50
while True:
	print("Amount Due: ",amt)
	coin=int(input("Insert Coin: "))
	if coin in [5,10,25]:
		amt=amt - coin
		if amt<0:
			print("Change Owned: ", abs(amt))
			break
		elif amt ==0:
			print("Change Owned: 0")
			break
