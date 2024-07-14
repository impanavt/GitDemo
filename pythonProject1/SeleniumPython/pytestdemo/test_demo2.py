import pytest
@pytest.mark.smoke
def test_firstProgram(setup):
    msg="Hello"
    assert msg=="Hi","Test failed because strings do not match"

def test_creditcardnumber():
    a=2
    b=4
    assert a+2==4,"do not match"