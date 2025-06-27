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
