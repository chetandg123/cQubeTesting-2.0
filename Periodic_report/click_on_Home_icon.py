import time

from Data.parameters import Data
from reuse_func import GetData


class Home():
    def __init__(self, driver):
        self.driver = driver

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        cal.page_loading(self.driver)


    def click_HomeButton(self):
        count = 0
        self.driver.find_element_by_id(Data.home).click()
        cal = GetData()
        cal.page_loading(self.driver)
        if 'home' in self.driver.current_url:
            print('Landing page is displayed')
        else:
            print('Home btn is not working ')
            count = count + 1
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_id('patReport').click()
        time.sleep(4)
        return count






