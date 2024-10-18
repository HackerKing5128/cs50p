def main():
    message=input("Enter your message: ")
    message=convert(message)
    print(message)

def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text
    
main()
