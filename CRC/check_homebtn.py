import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class Homebutton():
   def __init__(self,driver):
       self.driver = driver

   def test_homeicon(self):
       self.driver.find_element_by_xpath(Data.hyper).click()
       time.sleep(5)
       dist = Select(self.driver.find_element_by_name("myDistrict"))
       dist.select_by_index(1)
       time.sleep(3)
       self.driver.find_element_by_id(Data.homeicon).click()
       time.sleep(4)
       down =  self.driver.find_element_by_id(Data.Download)
       time.sleep(5)
       return down.is_displayed()

