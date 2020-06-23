import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from get_dir import pwd


class login_with_wrong_values():
    def __init__(self,driver):
        self.driver = driver

    def test_wrongvalues(self):

        self.driver.find_element_by_id(Data.email).send_keys("tibil@yahoo.com")
        self.driver.find_element_by_id(Data.passwd).send_keys("tib")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[2]/div[2]/form/div[2]/div/label").text
        time.sleep(2)
        self.driver.find_element_by_id(Data.email).clear()
        self.driver.find_element_by_id(Data.passwd).clear()
        time.sleep(2)
        return errormsg

