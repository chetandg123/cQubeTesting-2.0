import time

from Data.parameters import Data
from reuse_func import GetData


class schoolinfra_logout():
    def __init__(self,driver):
        self.driver =driver
    def test_logout(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.logout).click()

