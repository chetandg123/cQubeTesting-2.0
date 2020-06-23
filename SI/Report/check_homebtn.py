import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data


class home_button():
    def __init__(self,driver):
        self.driver = driver
    def test_home(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        time.sleep(3)
        self.driver.find_element_by_id(Data.homeicon).click()
        down =  self.driver.find_element_by_id(Data.Download)
        return down.is_displayed()

