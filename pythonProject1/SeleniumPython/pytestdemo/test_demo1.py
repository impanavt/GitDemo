# any pytest file should start or end with _test or test_
# pytest methods should start with test
# Any code should be wrapped in method only
# In pytest every method is treated as one test case with two lone spaces
# Multiple test cases should not with same method name othewrise it ovverrides
# method name should be meaningful
# -k stands for method names execution -s stands for logs -v for more info
# you can marks tests as pytest.mark.smoke then run with -m
# you can skip tests with skip
# whatever printed after yield be executed last
# fixtures are used as setup and tear down methods for test cases -conftest for file to generalize fixtures and make it available to all files
# data driven and parameterization can be done with return statement with tuple parameterization
# when scope is defines as class in fixture after every class it runs


import pytest
# def test_demo1():
#     print("Hello World!")
# @pytest.mark.smoke
# @pytest.mark.xfail
# def test_creditcardnumber():
#     print("Hey,Impana you just beautiful")
#
#
# def test_fixtureDemo(setup):
#     print("I will execute tests in fixtureDemo")

def testcrossbrowser(crossbrowser):
    print(crossbrowser[1])
