#Caesar Cipher (project.py)

#Importing Required Libraries
import os
import time
import platform as pt


# Creating Caesar Class for  'Caesar Cipher' logic
class Caesar():
    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                self.translated = self.translated + self.LETTERS[num]
            else:
                self.translated = self.translated + symbol

        return self.translated
     
	#Caesar Class - encrypt method
    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')
        
	#Caesar Class - decrypt method
    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')


#Creating Required Functions
def main():
	print(("*"*25).center(90))
	print("---> CAESAR CIPHER <---".center(90))
	print(("*"*25).center(90))
	print("\n")
	menu()
	
def encode(message, key=0):
	cipher= Caesar()
	return cipher.encrypt(message,key)

def decode(message, key=0):
	cipher= Caesar()
	return cipher.decrypt(message,key)
	
def get_key():
	key = input("Enter Key: ").strip()
	if (key.isdigit()) and (0 <= int(key) <= 25):
		return int(key)
	else:
		print("\n \tInvalid Key")
		menu2()

# Creating Additional Functions
def clear():
	if pt.system()=="Windows":
		os.system("cls")
	else:
		os.system("clear")

def welcome():
	print(("*"*25).center(90))
	print("---> CAESAR CIPHER <---".center(90))
	print(("*"*25).center(90))
	print("\n")
	menu()

def menu():
	print("\nThese are the operation you can perform with this program-\n \n 1-> Encrypt Message \n 2-> Decrypt Message \n 3-> Exit")
	choice=input('\nEnter the operation you want to perform [1/2/3]-  ').strip()
	match(choice):
		case "1":
			print('\n',"---> MESSAGE ENCRYPTION <---".center(80))
			message=input("MESSAGE: ")
			key=get_key()
			print(encode(message, key))
		case "2":
			print('\n',"---> MESSAGE DECRYPTION <---".center(80))
			message=input("MESSAGE: ")
			key=get_key()
			print(decode(message, key))
		case "3":
			Exit()
		case _:
			print('\n \tInvalid Operation')
	menu2()

def menu2():
    a=input('\nDo you want to perform any other operation, Enter "Yes" if you wish. If no enter any number or word- ')
    a=(a.strip()).lower()
    if a=='yes':
        time.sleep(1)
        clear()
        welcome()
    else:
        Exit()
        
def Exit():
	print('\n')
	print("---> THANKS FOR USING THIS PROGRAM <---".center(90))
	exit()


#Driver Code
if __name__ == "__main__":
	main()
