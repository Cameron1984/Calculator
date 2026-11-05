from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2,3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(7, 3) == 4

def test_multiply():
	assert multiply(3, 4) == 12

#Test edge cases
def test_zero_multiplication():
	#arrange
	a, b = 5, 0
	#act
	result = multiply(a, b)
	#assert
	assert result == 0
