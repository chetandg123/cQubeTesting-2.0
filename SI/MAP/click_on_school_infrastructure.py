import time

from Data.parameters import Data


class School_infra_test():
    def __init__(self,driver):
        self.driver = driver

    def test_dashboard_option(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.Reportmap).click()
        time.sleep(5)



   