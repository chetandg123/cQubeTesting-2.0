import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class blocklevel_csv():
    def __init__(self,driver):
        self.driver =driver
        self.filename=''
    def test_each_district(self):
        self.driver.find_element_by_css_selector('p >span').click()
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        p = pwd()
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(5)
            self.driver.find_element_by_id('download').click()
            time.sleep(5)
            self.filename = p.get_download_dir() + "/blockPerDistrict_report.csv"
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            if os.path.isfile(self.filename) == True:
                os.remove(self.filename)
            time.sleep(2)
        return count


