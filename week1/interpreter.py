exp=input("Expression: ") 
x,y,z=exp.split(" ") 
if y=="/" and z==0: 
    print("No") 
else: 
    ans=float(eval(exp)) 
    print(ans,end='')
