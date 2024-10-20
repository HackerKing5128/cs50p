import sys
from PIL import Image, ImageOps
import os

if len(sys.argv)<3:
	sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
	sys.exit("Too many command-line arguments")
else:
	extensions=[".jpg",".jpeg",".png"]
	ext1=os.path.splitext(sys.argv[1])
	ext2=os.path.splitext(sys.argv[2])
	
	if ext1[1]==ext2[1] and ext1[1] in extensions:
		try:
			user_image=Image.open(sys.argv[1])
		except FileNotFoundError:
			sys.exit("Input does not exist")
		shirt=Image.open("shirt.png")
		size = shirt.size
		user_image=ImageOps.fit(user_image, size)
		user_image.paste(shirt, shirt)
		user_image.save(sys.argv[2])
	elif ext1[1] != ext2[1]:
		sys.exit("Input and output have different extensions")
	else:
		if ext1[1] not in extensions:
			sys.exit("Invalid input")
		else:
			sys.exit("Invalid output")
