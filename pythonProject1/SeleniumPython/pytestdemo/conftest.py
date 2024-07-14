import pytest
@pytest.fixture(scope='class')
def setup():
    print("I will be exceuting first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataload():
    print("user profile data is being craeted")
    return ["Impaan","Gowda","You are Beautiful"]

# parameterization in fixtures
# when we run 3 times each one is considered as a tuple
@pytest.fixture(params=[('chrome','Rahul','Impana'),('firefox','Gowda'),'IE'])
def crossbrowser(request):
    return request.param



