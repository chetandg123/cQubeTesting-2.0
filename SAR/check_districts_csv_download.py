import os
import time
import unittest

from selenium.webdriver.support.select import Select

from get_dir import pwd
from reuse_func import GetData


class DistrictCsvDownload():
    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()

    def check_districts_csv_download(self):
        state = GetData()
        state.click_on_state(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(20, len(select_district.options)):
            select_district.select_by_index(x)
            self.driver.find_element_by_id('download').click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/Block_per_district_report_" + self.month + "_" + self.year + ".csv"
            if not os.path.isfile(self.filename):
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            if os.path.isfile(self.filename):
                os.remove(self.filename)

        return count

