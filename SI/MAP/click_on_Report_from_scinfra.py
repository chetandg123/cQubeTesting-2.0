import time

from selenium.common import exceptions

from Data.parameters import Data


class click_report():
       def __init__(self,driver):
           self.driver = driver

       def test_infra(self):
           self.driver.find_element_by_xpath(Data.hyper_link).click()
           time.sleep(5)
           try:
               self.driver.find_element_by_id(Data.Dashboard).click()
               # text = self.driver.find_element_by_xpath(Data.header).text
               self.driver.find_element_by_xpath(Data.School_infra).click()
               time.sleep(3)
               self.driver.find_element_by_id(Data.Report).click()
               time.sleep(3)
               # return text
           except exceptions.ElementClickInterceptedException:
               print("school infra report page ")
           time.sleep(5)