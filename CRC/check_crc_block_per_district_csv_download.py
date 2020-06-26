import os
import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class blockwise():

    def __init__(self, driver):
        self.driver = driver
        self.filename = ''

    def test_blocklevel(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(3)
            self.driver.find_element_by_id('download').click()
            time.sleep(3)
            p = pwd()
            p.get_download_dir()
            self.filename = p.get_download_dir() + "/Block_level_CRC_Report.csv"
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            if os.path.isfile(self.filename) == True:
                os.remove(self.filename)

        return count
