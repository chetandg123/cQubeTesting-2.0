import re
import time

from selenium.common import exceptions

from Data.parameters import Data


class Block_school_count():
    def __init__(self,driver):
        self.driver = driver

    def test_counter(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        try:
            school = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            res = re.sub('\D', "", school)
            time.sleep(3)
            self.driver.find_element_by_id(Data.scm_block).click()
            time.sleep(6)
            bschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            bres = re.sub('\D',"",bschool)
            time.sleep(3)

            self.driver.find_element_by_id(Data.scm_cluster).click()
            time.sleep(10)
            cschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            time.sleep(2)
            cres = re.sub('\D', "", cschool)

            time.sleep(3)
            self.driver.find_element_by_id(Data.scm_school).click()
            time.sleep(25)
            sschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            time.sleep(3)
            sres = re.sub('\D', "", sschool)
            time.sleep(5)
            return res ,bres ,cres,sres
        except exceptions.ElementClickInterceptedException :
            print("no of schools are same ")
            time.sleep(5)