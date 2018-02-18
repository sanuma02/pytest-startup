import mathexample
import pytest

#@pytest.mark.skipif(<if condition>, reason="the reason")
@pytest.mark.skip(reason="Need to skip now")
def test_sum():
	result = mathexample.sum(4,5)
	assert result == 9

@pytest.mark.mul
def test_mul():
	result = mathexample.mult(3,10)
	assert result == 30

@pytest.mark.parametrize("test_input,expected_output",[(5,25),(9,81),(10,100)])
def test_square(test_input,expected_output):
	result = mathexample.square(test_input)
	assert result == expected_output