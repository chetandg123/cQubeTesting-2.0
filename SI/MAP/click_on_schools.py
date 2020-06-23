import time

from Data.parameters import Data


class click_schoolwise():
    def __init__(self,driver):
        self.driver =driver

    def test_dots(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.scm_school).click()
        time.sleep(25)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots)-1
        return count
