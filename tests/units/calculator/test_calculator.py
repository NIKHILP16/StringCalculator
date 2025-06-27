import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_initialize_calculator(calculator):
    assert isinstance(calculator, Calculator)

def test_add_method_with_empty_string(calculator):
    result=calculator.add("")
    assert result==0

def test_add_method_with_single_number(calculator):
    result=calculator.add("1")
    assert result==1

def test_add_method_with_delimiters_multiple_number(calculator):
    result=calculator.add("1,2")
    assert result==3

def test_add_method_with_delimiters_multiple_number_2(calculator):
    result=calculator.add("1,2,3,4,5")
    assert result==15

def test_add_method_with_newline_delimiters(calculator):
    result=calculator.add("1\n2,3")
    assert result==6

def test_add_with_invalid_input(calculator):
    with pytest.raises(ValueError) as exc_info:
        calculator.add("1,\n")
    assert "Invalid input" in str(exc_info.value)
