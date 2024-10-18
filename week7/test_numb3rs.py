from numb3rs import validate

def test_1():
	assert validate("127.0.0.1")==True
	assert validate("258.6.9.28")==False
	assert validate("1.2.3.1000")==False

def test_2():
	assert validate("cat")==False
	assert validate("255.255.255.255")==True
	assert validate("512.512.512.512")==False


