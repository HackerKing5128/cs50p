from um import count

def test_1():
	assert count("um.")==1

def test_2():
	assert count("UM, um. yummy")==2
	assert count("yummy")==0

def test_3():
	assert count("um, thanks for the album.")==1
	assert count("hello, duniya")==0
