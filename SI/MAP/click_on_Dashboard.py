import time

from Data.parameters import Data
from reuse_func import GetData


class click_dashboard():
    def __init__(self,driver):
        self.driver = driver
    def test_dashboard(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        text = self.driver.find_element_by_xpath(Data.header).text
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.Reportmap).click()
        time.sleep(5)
        return text

