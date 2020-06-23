import time

from Data.parameters import Data


class click_schoolinfra():
    def __init__(self,driver):
        self.driver = driver
    def test_schoolinfra(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        if "school-infrastructure" in self.driver.current_url:
            print("School-infrastructure page")
        else:
            print("Not school-infrastructure page")
