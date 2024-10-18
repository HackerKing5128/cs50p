import sys
import random
from pyfiglet import Figlet
figlet= Figlet()
List= sys.argv
s=input("Input: ")
if (len(sys.argv)==3):
	Font,Name=List[1],List[2]
	flist=figlet.getFonts()
	if((Font=='-f' or Font=='--font') and (Name in flist)):
		figlet.setFont(font=Name)
		print(figlet.renderText(s))
	else:
		print("Invalid usage")
		sys.exit()
elif (len(sys.argv)==1):
	Font=figlet.getFonts()
	Name=random.choice(Font)
	figlet.setFont(font=Name)
	print(figlet.renderText(s))
else:
	print("Invalid usage")
	sys.exit()

