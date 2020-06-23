import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class blocklevel_csv():
    def __init__(self,driver):
        self.driver =driver

    def test_search(self):

        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        # select_district =Select(self.driver.find_element_by_name('myDistrict'))
        # count = 0
        # p = pwd()
        # for x in range(1, len(select_district.options)):
        #     select_district.select_by_index(x)
        #     time.sleep(2)
        #     self.driver.find_element_by_id('download').click()
        #     time.sleep(4)
        #     filename = p.get_download_dir() + "/blockPerDistrict_report.csv"
        #     if os.path.isfile(filename) != True:
        #         print("District" + select_district.first_selected_option.text + "csv is not downloaded")
        #         count = count + 1
        #     if os.path.isfile(filename) == True:
        #         os.remove(filename)
        #
        # return count




