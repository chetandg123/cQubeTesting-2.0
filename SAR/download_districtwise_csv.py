import os
import re
import time
import unittest

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class DistrictwiseCsv():

    def __init__(self, driver,year,month):
        self.driver = driver
        self.year = year.strip()
        self.month =month.strip()

    def click_download_icon_of_district(self):
        state = GetData()
        state.click_on_state(self.driver)
        time.sleep(2)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/District_wise_report_"+self.month+"_"+self.year+".csv"
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)
