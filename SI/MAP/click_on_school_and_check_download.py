import time

from selenium.common import exceptions

from Data.parameters import Data



class school_wise_download():
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

    def test_schoolwise(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        try:
            self.driver.find_element_by_id(Data.scm_school).click()
            time.sleep(25)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(4)
            count =len(dots)-1
            time.sleep(3)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            return count
        except exceptions.ElementClickInterceptedException:
            print("School level csv downloaded!")