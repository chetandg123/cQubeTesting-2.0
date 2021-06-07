
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class last7day_timeperiod():
    def __init__(self, driver):
        self.driver = driver

    def test_last7day_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('blockbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('clusterbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('schoolbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            scount = len(markers)
            self.data.page_loading(self.driver)
            return bcount, ccount, scount
