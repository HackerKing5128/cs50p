def main(): 
    time=input("What time is it? ") 
    now=convert(time) 
    if 7.00<=now<=8.00: 
        print("breakfast time") 
    elif 12.00<=now<=13.00: 
        print("lunch time") 
    elif 18.00<=now<=19.00: 
        print("dinner time") 
  
  
def convert(str): 
    hr,min=str.split(":") 
    min=float(min)/60 
    time=float(hr)+min 
    return time 
 
if __name__=="__main__": 
    main()
