import re
import time
import unittest

from Data.parameters import Data


class SchoolwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon_of_schools(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        time.sleep(30)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
