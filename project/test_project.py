from project import encode, decode

def test_encode():
	assert encode("HI",20)=="BC"
	assert encode("HELLO",3)=="KHOOR"
	assert encode("WHERE ARE YOU?",6)=="CNKXK GXK EUA?"
	
def test_decode():
	assert decode("BC",20)=="HI"
	assert decode("KHOOR",3)=="HELLO"
	assert decode("ALERT")=="ALERT"
	
def test_code():
	assert encode("CALL ME",9)=="LJUU VN"
	assert decode("TJ50",17)=="CS50"
