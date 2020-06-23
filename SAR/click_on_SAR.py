import time

from selenium.common.exceptions import ElementClickInterceptedException

from Data.parameters import Data
from reuse_func import GetData


class DahboardSar():
    def __init__(self, driver):
        self.driver = driver

    def click_on_sar(self):
        try:
            state = GetData()
            state.click_on_state(self.driver)
            time.sleep(2)
            self.driver.find_element_by_id(Data.Dashboard).click()
            time.sleep(5)
            self.driver.find_element_by_id(Data.SAR).click()
            return self.driver.page_source
        except ElementClickInterceptedException:
            print("Element not found and test failed")



