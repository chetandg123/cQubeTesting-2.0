import time

from Data.parameters import Data


class click_schoolinfra():
    def __init__(self,driver):
        self.driver = driver
    def test_schoolinfra(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
