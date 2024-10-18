from datetime import datetime, date
import sys
import inflect

def main():
	print(minutes(input("Date of Birth: ")))

def minutes(birth):
	if chkdate(birth) is False:
		sys.exit("Invalid date")
	#convert input date to date object
	y,m,d= birth.split("-")
	birthday= date(int(y), int(m), int(d))
	today= date.today()
	#calculate total duration minutes
	duration=abs(today - birthday)
	days = duration.days
	minutes = days * 1440   #1day=1440mins
	return convert(minutes)

def chkdate(date_str):
    date_format='%Y-%m-%d'
    try:
        obj=datetime.strptime(date_str,date_format)
        return True
    except ValueError:
        return False
        
def convert(min):
        p= inflect.engine()
        words = p.number_to_words(min, andword="")
        return (words + " minutes").capitalize()
        
if __name__ == "__main__":
	main()
