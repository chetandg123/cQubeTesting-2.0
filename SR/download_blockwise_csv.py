import os
import re
import time
import unittest


from Data.parameters import Data
from get_dir import pwd


class BlockwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon_of_blocks(self):
        self.driver.find_element_by_css_selector('p >span').click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        time.sleep(30)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/Block_wise_report.csv"
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)

