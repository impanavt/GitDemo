import pytest

class Calculator():
    def __init__(self):
        self.result=0

    def add(self,a,b):
        self.result=a+b
        return  self.result

@pytest.fixture
def calculator():
    calc=Calculator()
    yield calc

    

def test_add_method(calculator):
    result=calculator.add(5,6)
    assert result==8

def test_add_method_with_zero(calculator):
    result=calculator.add(0,6)
    assert result==6
