import pytest
@pytest.mark.usefixtures("setup")
class TestExample:
  def test_fixturedemo(self):
    print("I will execute steps in fixture demo method")

  def test_fixturedemo1(self):
    print("I will execute steps in fixture demo 1method")

  def test_fixturedemo2(self):
    print("I will execute steps in fixture demo 2method")

  def test_fixturedemo3(self):
    print("I will execute steps in fixture demo 3method")

