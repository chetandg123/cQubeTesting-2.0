import time

from Data.parameters import Data


class Dashboard():
    def __init__(self, driver):
        self.driver = driver

    def click_on_dashboard(self):
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.SAR).click()
