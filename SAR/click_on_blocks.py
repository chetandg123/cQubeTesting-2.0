import time

from Data.parameters import Data


class Blocks():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        time.sleep(15)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots