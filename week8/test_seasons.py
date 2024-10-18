import seasons as s

def test_1():
	assert s.minutes("April 10, 2005")=="Invalid date"
	assert s.minutes("21-07-1997")=="Invalid date"
	
def test_2():
	assert s.minutes("2022-12-31")=="Five hundred twenty-five thousand, six hu⁸ndred minutes"
	assert s.minutes("2021-12-31")=="One million, fifty-one thousand, two hundred minutes"
