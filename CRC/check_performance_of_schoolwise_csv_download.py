import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class download_schoollevel_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
       self.driver.find_element_by_xpath(Data.hyper).click()
       time.sleep(5)
       p = pwd()
       District_wise = Select(self.driver.find_element_by_id("downloader"))
       District_wise.select_by_visible_text(" School_Wise Report ")
       time.sleep(3)
       self.driver.find_element_by_id(Data.Download).click()
       time.sleep(35)
       self.filename = p.get_download_dir() + "/School_level_CRC_Report.csv"
       time.sleep(4)
       return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)



