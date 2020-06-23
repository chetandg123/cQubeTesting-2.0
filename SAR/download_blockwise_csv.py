import re
import time
import unittest


from Data.parameters import Data
class BlockwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon_of_blocks(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        time.sleep(15)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
