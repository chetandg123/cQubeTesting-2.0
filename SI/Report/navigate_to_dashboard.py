import time

from Data.parameters import Data


class check_dashboard():
    def __init__(self,driver):
        self.driver = driver

    def test_menulist(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        self.driver.find_element_by_id(Data.Report).click()
        time.sleep(2)
