import time

from Data.parameters import Data


class SemesterReport():
    def __init__(self, driver):
        self.driver = driver

    def click_on_semester(self):
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.sr_by_xpath).click()
        time.sleep(3)
        return self.driver.page_source


