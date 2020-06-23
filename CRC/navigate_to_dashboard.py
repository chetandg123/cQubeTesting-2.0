import time

from selenium import webdriver

from Data.parameters import Data


class Dashboard_menu():
    def __init__(self,driver):
        self.driver = driver
    def test_dashboard(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        print("Navigated to dashboard menu ")
        time.sleep(2)
        self.driver.find_element_by_id(Data.CRC).click()
        time.sleep(3)


