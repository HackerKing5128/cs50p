import random
while True:
	n=input("Level: ")
	if(n.isdigit() and int(n)>0):
		break
comp=random.randint(1,int(n))
while True:
	guess=input("Guess: ")
	if((guess.isdigit() and int(guess)>0) == 0):
		continue
	guess=int(guess)
	if (guess> comp):
		print("Too large!")
	elif (guess<comp):
		print("Too small")
	else:
		print("Just right!")
		break
