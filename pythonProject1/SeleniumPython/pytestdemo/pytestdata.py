import pytest
from pytestdemo.baseclass import BaseClass

@pytest.mark.usefixtures("dataload")
class TestExample(BaseClass):

    def test_editProfile(self,dataload):
        log=self.getLogger()
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload[2])
