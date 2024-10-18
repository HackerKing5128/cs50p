ques=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ") 
ques=ques.strip().lower() 
if ques in ["42","forty-two","forty two"]: 
    print("Yes") 
else: 
    print("No")
