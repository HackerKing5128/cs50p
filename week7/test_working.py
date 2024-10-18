#Working 9 to 5 (test_working.py)

from working import convert
import pytest

def test_1():
	assert convert("9 AM to 5 PM")=="09:00 to 17:00"
	assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
	assert convert("12:30 AM to 8:30 PM")=="00:30 to 20:30"

def test_2():
	assert convert("12 AM to 12 PM")=="00:00 to 12:00"
	assert convert("12:00 AM to 12:00 PM")=="00:00 to 12:00"

def test_3():
	with pytest.raises(ValueError):
		convert("12:70 AM to 2:60 PM")
	with pytest.raises(ValueError):
		convert("8:00 to 2:00 PM")
	with pytest.raises(ValueError):
		convert("9:30 AM to 17:00")
