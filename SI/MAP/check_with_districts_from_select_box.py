import time

from Data.parameters import Data


class District_names():
    def __init__(self,driver):
        self.driver = driver

    def test_districtlist(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        time.sleep(3)
        count =  len(Districts)-1
        return count

