import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class download_districtwise():
    def __init__(self,driver):
        self.driver = driver

    def test_donwload(self):
        p = pwd()
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        dist = Select(self.driver.find_element_by_name(Data.select_district))
        dist.select_by_index(10)
        time.sleep(4)
        self.driver.find_element_by_id(Data.Download)
        time.sleep(3)
        self.filename = p.get_download_dir() + "/blockPerDistrict_report.csv"
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)

