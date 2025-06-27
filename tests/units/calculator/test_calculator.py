import pytest
from calculator import Calculator
from constants import Errors
@pytest.fixture
def calculator():
    return Calculator()

def test_initialize_calculator(calculator):
    assert isinstance(calculator, Calculator)

def test_add_method_with_empty_string(calculator):
    expected=0
    result=calculator.add("")
    assert expected==result

def test_add_method_with_single_number(calculator):
    expected=1
    result=calculator.add("1")
    assert expected==result

def test_add_method_with_delimiters_multiple_number(calculator):
    expected=3
    result=calculator.add("1,2")
    assert expected==result

def test_add_method_with_delimiters_multiple_number_2(calculator):
    expected=15
    result=calculator.add("1,2,3,4,5")
    assert expected==result

def test_add_method_with_newline_delimiters(calculator):
    expected=6
    result=calculator.add("1\n2,3")
    assert expected==result

def test_add_with_invalid_input(calculator):
    expected=Errors.EMPTY_INPUT
    with pytest.raises(ValueError) as exc_info:
        calculator.add("1,\n")
    
    assert  expected== str(exc_info.value)

@pytest.mark.parametrize("input_str, expected", [
    ("//;\n1;2", 3),
    ("//|\n4|0|6", 10),
    ("//:\n7:8\n9", 24)
])
def test_add_method_with_custom_delimeter(calculator,input_str, expected):
    assert expected==calculator.add(input_str)

def test_add_method_with_negative_numbers(calculator):
    expected=Errors.NEGATIVE_NUMBERS.format([-2])
    with pytest.raises(ValueError) as exc_info:
        calculator.add("//;\n1;-2")
    assert expected == str(exc_info.value)