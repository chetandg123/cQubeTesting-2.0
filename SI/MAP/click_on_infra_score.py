import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.parameters import Data


class click_on_infrascores():
    def __init__(self,driver):
        self.driver=driver
    def test_infrascores(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        count = len(chooseinfra.options)-1
        time.sleep(3)
        for x in range(1, len(chooseinfra.options)):
            time.sleep(2)
            chooseinfra.select_by_index(x)
            time.sleep(3)
        return count