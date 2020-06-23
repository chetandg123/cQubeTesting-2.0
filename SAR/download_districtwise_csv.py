import re
import time
import unittest

from Data.parameters import Data


class DistrictwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon_of_district(self):
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
