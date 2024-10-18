# Cookie Jar (test_jar.py)
from jar import Jar

def test_init():
	jar1 = Jar()
	assert jar1.capacity == 12
	jar2 = Jar(10)
	assert jar2.capacity ==10
	
def test_str():
	jar = Jar()
	assert str(jar) == ""
	jar.deposit(1)
	assert str(jar) == "🍪"
	jar.deposit(11)
	assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
	
def test_deposit():
	jar = Jar()
	assert jar.size == 0
	jar.deposit(4)
	assert jar.size == 4
		

def test_withdraw():
	jar = Jar()
	jar.deposit(12)
	assert jar.size == 12
	jar.withdraw(6)
	assert jar.size == 6
	
