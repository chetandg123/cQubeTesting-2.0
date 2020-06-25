import re
import time


from Data.parameters import Data



class school_count():
   def __init__(self,driver):
       self.driver = driver

   def test_count(self):
       self.driver.find_element_by_xpath(Data.hyper_link).click()
       time.sleep(5)
       self.driver.find_element_by_xpath(Data.hyper_link).click()
       time.sleep(5)
       self.driver.find_element_by_id(Data.scm_block).click()
       time.sleep(10)
       schools = self.driver.find_element_by_id(Data.sc_no_of_schools).text
       time.sleep(3)
       res = re.sub("\D", "", schools)
       time.sleep(5)
       return res



