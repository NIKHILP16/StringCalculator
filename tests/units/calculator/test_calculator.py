import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_initialize_calculator(calculator):
    assert isinstance(calculator, Calculator)
